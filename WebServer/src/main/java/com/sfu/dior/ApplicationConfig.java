package com.sfu.dior;

import java.util.Map;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.deploy.yarn.Client;
import org.apache.spark.deploy.yarn.ClientArguments;

import org.apache.spark.sql.SparkSession;
import org.slf4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import com.sfu.dior.utils.CommonUtils;

@Configuration
@PropertySource("classpath:application.properties")
public class ApplicationConfig {
	
	@Autowired
	private SparkConfig sparkConfig;
	
	private Logger logger = CommonUtils.getLogger();
	
	@Value("${app.name:test}")
    private String appName;

    @Bean
    public SparkConf sparkConf() {
    	logger.info("Web Name is " + appName);
    	logger.info(sparkConfig.getSparkConfig().toString());
    	
        SparkConf sparkConf = new SparkConf()
                .setAppName(appName);
        for (String key : sparkConfig.getSparkConfig().keySet()) {
        	sparkConf.set(key, sparkConfig.getSparkConfig().get(key));
        }
        
        return sparkConf;
    }

    @Bean
    public JavaSparkContext javaSparkContext(){
        return new JavaSparkContext(sparkConf());
    }

    @Bean
    public SparkSession sparkSession(){
        return SparkSession
                .builder()
                .sparkContext(javaSparkContext().sc())
                .getOrCreate();
    }
    
    public String getAppName() {
    	return this.appName;
    }
}
