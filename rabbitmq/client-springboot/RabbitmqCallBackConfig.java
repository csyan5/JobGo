package com.sfu.dior.RabbitMQ;

import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.beans.factory.config.ConfigurableBeanFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;


@Configuration
public class RabbitmqCallBackConfig {

    @Bean
    public Queue ReplyQueue() {
        return new Queue("replyQueue");
    }

    @Bean
    public ConnectionFactory connectionFactory() {
        CachingConnectionFactory connectionFactory = new CachingConnectionFactory();
        connectionFactory.setAddresses("127.0.0.1:5672");
        connectionFactory.setUsername("hza89");
        connectionFactory.setPassword("dior");
        connectionFactory.setVirtualHost("hza89_vhost");
        connectionFactory.setPublisherConfirms(true); //必须要设置
        return connectionFactory;
    }

    @Bean
    @Scope(ConfigurableBeanFactory.SCOPE_PROTOTYPE)
    //必须是prototype类型
    public RabbitTemplate rabbitTemplatecallback() {
        RabbitTemplate template = new RabbitTemplate(connectionFactory());
        return template;
    }

//    @Bean
//    public RabbitTemplate RabbitReplyTemplate() {
//        RabbitTemplate template2 = new RabbitTemplate(connectionFactory());
//        return template2;
//    }

    @Bean
    public SimpleMessageListenerContainer messageListenerContainer() {
        SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
        container.setConnectionFactory(connectionFactory());
        container.setQueueNames("replyQueue");
        container.setMessageListener(exampleListener());
        return container;
    }

    @Bean
    public MessageListener exampleListener() {
        return new MessageListener() {
            public void onMessage(Message message) {
                System.out.println("received: " + message);
                try {
                    String res = new String(message.getBody(), "UTF-8");
                    String context = "now date ".concat(new SimpleDateFormat("yyyy-MM-dd HH:mm:dd").format(new Date()));
                    System.out.println("received at: " + context);
                    System.out.println("received data: " + res);
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }

            }
        };
    }



}