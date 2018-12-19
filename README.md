# JobGo -- 2018Fall Final project for CMPT732

## Files Intruduction:

### Database/

 - ER Diagram of our database
 - DDL sql scripts
 - Python code that use to import our ETLed Data into database

### DataCollect/
- BeautifulSoup/
	- Python code that use to etl our scraped raw HTML files into clean json files.
	- Results of the clean json files.
- Scrapy/
	- Code that used to scrape data from Glassdoor, Linkedin and Indeed.

### Rabbitmq/
- spark_server.py
	- Program that runs an long-running spark context which can keep listening to messages from Rabbitmq, do the calculating, and sending the results back to the client(Spring Boot Server).
- client-springboot/
	- Some demo code we tried to connect Springboot with Rabbitmq.

### Spark Config/
- Configurations that we used to set up the spark-submit environment in our Virtual Machine.

### WebServer/
- Our Sprintboot Web Server code. Java code and all static resources included. Maven based project.