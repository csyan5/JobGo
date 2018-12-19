package com.sfu.dior.RabbitMQ;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.DirectExchange;
import org.springframework.amqp.core.Queue;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;

@Configuration
@PropertySource("classpath:application.properties")
public class RabbitConfig {
    @Bean
    public Queue dateQueue() {
        return new Queue("date");
    }

    @Bean
    public Queue objQueue() {
        return new Queue("object");
    }

    @Bean
    public Queue pythonQueue() {
        return new Queue("pythonConnection");
    }

    @Bean
    public DirectExchange exchange() {
        return new DirectExchange("job5");
    }

    @Bean
    public Queue jobQueue() {
        return new Queue("jobQueue5");
    }

    @Value("${spring.rabbitmq.host:127.0.0.1}")
    public String rabbitHost;
    
    @Value("${spring.rabbitmq.port:5672}")
    public String rabbitPort;
    
    @Value("${spring.rabbitmq.username:hza89}")
    public String rabbitUser;
    
    @Value("${spring.rabbitmq.password:dior}")
    public String rabbitPass;
    
    @Value("${spring.rabbitmq.addresses:127.0.0.1:5672}")
    public String rabbitAddress;
    
    @Value("${spring.rabbitmq.virtual-host:hza89_vhost}")
    public String rabbitVhost;


}
