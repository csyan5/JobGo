package com.sfu.dior.RabbitMQ;

import org.springframework.amqp.core.Binding;
import org.springframework.amqp.core.BindingBuilder;
import org.springframework.amqp.core.DirectExchange;
import org.springframework.amqp.core.Queue;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
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

//    @Bean
//    public Binding binding(DirectExchange exchange,
//                           Queue jobQueue) {
//        return BindingBuilder.bind(jobQueue)
//                .to(exchange)
//                .with("amq");
//    }

//    @Bean
//    public RabbitTemplate fixedReplyQRabbitTemplate() {
//        RabbitTemplate template = new RabbitTemplate(this.rabbitConnectionFactory);
//        template.setExchange(ex().getName());
//        template.setRoutingKey("test");
//        template.setReplyQueue(replyQueue());
//        return template;
//    }






}
