package com.sfu.dior.RabbitMQ;

import org.slf4j.Logger;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.connection.CachingConnectionFactory;
import org.springframework.amqp.rabbit.connection.ConnectionFactory;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.amqp.rabbit.listener.SimpleMessageListenerContainer;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.config.ConfigurableBeanFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Scope;

import com.sfu.dior.utils.CommonUtils;

import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;


@Configuration
public class RabbitmqCallBackConfig {
	private Logger logger = CommonUtils.getLogger();
	
	@Autowired
	private RabbitConfig rabbitConfig;
	
    @Bean
    public Queue ReplyQueue() {
        return new Queue("replyQueue");
    }

    @Bean
    public ConnectionFactory connectionFactory() {
        CachingConnectionFactory connectionFactory = new CachingConnectionFactory();
        logger.info("------------rabbitMQ Config-------------");
        logger.info(rabbitConfig.rabbitAddress);
        logger.info(rabbitConfig.rabbitUser);
        logger.info(rabbitConfig.rabbitPass);
        logger.info(rabbitConfig.rabbitVhost);
        connectionFactory.setAddresses(rabbitConfig.rabbitAddress);
        connectionFactory.setUsername(rabbitConfig.rabbitUser);
        connectionFactory.setPassword(rabbitConfig.rabbitPass);
        connectionFactory.setVirtualHost(rabbitConfig.rabbitVhost);
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
//
    @Bean
    public SimpleMessageListenerContainer messageListenerContainer() {
        SimpleMessageListenerContainer container = new SimpleMessageListenerContainer();
        container.setConnectionFactory(connectionFactory());
        container.setQueueNames("replyQueue");
        container.setMessageListener(exampleListener());
        return container;
    }

    @Bean
    public MessageListenerImpl exampleListener() {
        return new MessageListenerImpl();
    }



}