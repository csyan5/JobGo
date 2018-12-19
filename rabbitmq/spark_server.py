import pika
import sys
import json
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, SQLContext, functions, types, Row

conf = SparkConf().setAppName('JobSearch')
sc = SparkContext(conf=conf)
assert sc.version >= '2.3'
spark = SparkSession.builder.config(conf=conf).getOrCreate()
sqlContext = SQLContext(sc)
sc.setLogLevel('WARN')


def loadSalaryData():
    job = sqlContext.read.format('jdbc').options(
        url='jdbc:mysql://nml-cloud-231.cs.sfu.ca:3306/job_search?characterEncoding=UTF-8&verifyServerCertificate=false&useSSL=false&requireSSL=false',
        driver='com.mysql.jdbc.Driver',
        dbtable='job',
        user='dior',
        password='dior').load()

    salary = sqlContext.read.format('jdbc').options(
        url='jdbc:mysql://nml-cloud-231.cs.sfu.ca:3306/job_search?characterEncoding=UTF-8&verifyServerCertificate=false&useSSL=false&requireSSL=false',
        driver='com.mysql.jdbc.Driver',
        dbtable='salary',
        user='dior',
        password='dior').load()

    jobwant = job.select(job['comp_id'], job['job_id'], job['title'], job['city'], job['avg_salary'], job['type'])
    salarywant = salary.select(salary['comp_id'], salary['salary_id'], salary['job_title'], salary['avg_salary'],
                               salary['job_type'])
    distribution = jobwant.join(salarywant,
                                [jobwant.comp_id == salarywant.comp_id, jobwant.title == salarywant.job_title]).select(
        jobwant['comp_id'], jobwant['title'], jobwant['city'], jobwant['type'], salarywant['salary_id'],
        salarywant['avg_salary'])
    distribution.cache()
    distribution.registerTempTable("distribution")


def get_all_job_avgsalary(input):
    job_list = input.split('|')

    loadSalaryData()
    result = {}
    for job in job_list:
        allresult = spark.sql("select avg_salary from distribution where type like '%{}%'".format(job))
        allresult.registerTempTable("allresult")
        all_average=spark.sql("select AVG(avg_salary) from allresult").collect()[0][0]
        all_average=round(all_average,2)
        result[job] = all_average
    return json.dumps(result)


def get_avg_by_location(input):
    job = input.split(',')[0]
    city_list = input.split(',')[1].split('|')

    loadSalaryData()
    placeholder = '('
    for city in city_list:
        placeholder = placeholder + '\'' + city + '\'' + ','
    placeholder = placeholder[0:-1] + ')'
    temp1 = spark.sql("select * from distribution where type like '%{}%' and city in {}".format(job, placeholder))

    temp2 = temp1.groupby('city').agg(functions.avg('avg_salary'))

    L=temp2.collect()

    result={}
    for l in L:
        d=l.asDict()
        value=d.get('avg(avg_salary)')
        #value=ronud(value,2)
        key=d.get('city')
        result[key]=value
    return json.dumps(result)


#handle the message from the queue
def messageHandler(ch, method, props, body):
    print(props);
    msg = str(body, 'utf-8')
    print(" [x] Received msg: " + msg)

    analysisType = msg.split('@')[0]
    msgContent = msg.split('@')[1]
    print('AnalysisType:' + analysisType)
    print('MsgContent:' + msgContent)

    output = ''
    print ('task start processing...')

    try:
        if analysisType == '1':
            output = get_all_job_avgsalary(msgContent)
        elif analysisType == '2':
            output = get_avg_by_location(msgContent)
    except:
        output = 'task failed'
    else:
        print('task successed')
    
    print(output);

    # Send back the output and keep program listening RabbitMQ
    ch.basic_publish(exchange='',
                 routing_key=props.reply_to,
                 properties=pika.BasicProperties(correlation_id = \
                                                     props.correlation_id),
                 body=output)
                 #str(body, 'utf-8')
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print(" [x] has sent the response back---------------------")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("[x] is listenning to new request now......")


def main():
    credentials = pika.PlainCredentials('hza89', 'dior')
    parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       'hza89_vhost',
                                       credentials)

    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue='jobQueue5', durable='false')

    channel.exchange_declare(exchange='job5',
                         exchange_type='direct', durable='false')

    channel.queue_bind(exchange='job5',
                   queue='jobQueue5')

    #print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(messageHandler, queue='jobQueue5')

    print(" [x] Awaiting RPC requests")
    channel.start_consuming()

if __name__ == '__main__':
    main()

#spark-submit correlate_logs.py nasa-logs-2