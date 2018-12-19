package com.sfu.dior.RabbitMQ;


import org.springframework.amqp.core.AmqpTemplate;
import org.springframework.amqp.core.DirectExchange;
import org.springframework.amqp.core.Queue;
import org.springframework.amqp.rabbit.core.RabbitTemplate;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;

@Component
public class HelloSender {
    @Autowired
    private Queue dateQueue;
    @Autowired
    private Queue objQueue;
    @Autowired
    private AmqpTemplate rabbitTemplate;

    @Autowired
    private Queue pythonQueue;

    @Autowired
    private Queue jobQueue;

    @Autowired
    private DirectExchange exchange;

    @Autowired
    private RabbitTemplate template;



    public void send() {
        String context = "now date ".concat(new SimpleDateFormat("yyyy-MM-dd HH:mm:dd").format(new Date()));
        System.out.println("Sender : " + context);
        rabbitTemplate.convertAndSend(dateQueue.getName(), context);

    }

    public void sendPython() {
        String context = "now date ".concat(new SimpleDateFormat("yyyy-MM-dd HH:mm:dd").format(new Date()));
        System.out.println("Sender : " + context);
        rabbitTemplate.convertAndSend(pythonQueue.getName(), context);
        //rabbitTemplate.convertAndSend("jobQueue", context);
    }

    public void sendObj(User user) {
        System.out.println("Sender : " + user);
        rabbitTemplate.convertAndSend(objQueue.getName(), user);
    }

    @Scheduled(fixedDelay = 1000, initialDelay = 500)
    public void sendWithResponse(){
//        Integer response = (Integer)template.convertSendAndReceive
//                (exchange.getName(), "jobQueue", 0);

        byte[] response = (byte[]) rabbitTemplate.convertSendAndReceive
                (exchange.getName(), "jobQueue4", "8");
//        for (int i = 0; i < response.length; i++) {
//            System.out.println("Receiving response bytes at index : " + i);
//            System.out.println("Receiving response : " + response[i]);
//        }

        //convert the byte array(encoded in ascii code) into string(utf-8)
        String res = null;
        try {
            res = new String(response, "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        System.out.println("Receiving response : " + res);

        //System.out.println("Receiving response : " + response[0]);

    }

    



}
