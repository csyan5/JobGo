package com.sfu.dior.RabbitMQ;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.UUID;

import org.slf4j.Logger;
import org.springframework.amqp.AmqpException;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessagePostProcessor;
import org.springframework.amqp.rabbit.connection.CorrelationData;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
//import org.springframework.amqp.rabbit.support.CorrelationData;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.sfu.dior.utils.CommonUtils;

@Component
public class SendCallback implements RabbitTemplate.ConfirmCallback {

	private Logger logger = CommonUtils.getLogger();
	
    private RabbitTemplate rabbitTemplate;

    /**
     * 构造方法注入
     */
    @Autowired
    public SendCallback(RabbitTemplate rabbitTemplatecallback) {
        this.rabbitTemplate = rabbitTemplatecallback;
        rabbitTemplate.setConfirmCallback(this); //rabbitTemplate如果为单例的话，那回调就是最后设置的内容
    }

    /**
     *	发送消息
     */
    public void sendMsg(String content) {
        CorrelationData correlationId = new CorrelationData(UUID.randomUUID().toString());
        logger.info("content:"+content);
        logger.info("correlationId:"+correlationId);
        String context = "now date ".concat(new SimpleDateFormat("yyyy-MM-dd HH:mm:dd").format(new Date()));
        logger.info("sent at: " + context);
        rabbitTemplate.convertAndSend("job5", "jobQueue5", content, new MessagePostProcessor(){
            @Override
            public Message postProcessMessage(Message message) throws AmqpException {
                message.getMessageProperties().setReplyTo("replyQueue");
                return message;
            }
        }, correlationId);
    }


    /**
     * 回调
     */
    public void confirm(CorrelationData correlationData, boolean ack, String cause) {
        logger.info(" 回调id:" + correlationData);
        if (ack) {
            logger.info("消息成功消费");
        } else {
            logger.info("消息消费失败:" + cause);
        }
    }

}