package com.sfu.dior.RabbitMQ;


import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Component;

@Component
public class HelloReceiver {
    @RabbitListener(queues = "date")
    public void processDate(String date){
        System.out.println("Receiver ==================: " + date);
    }

    @RabbitListener(queues = "object")
    public void processObj(User user) {
        System.out.println("Receiver ==================: " + user);
        System.out.println("Receiver ==================: " + user.getName());
        System.out.println("Receiver ==================: " + user.getId());


    }


}
