package com.sfu.dior.RabbitMQ;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RabbitTest {


    @Autowired   private SendCallback sendFunc;

    //fanout exchange类型rabbitmq测试
    @GetMapping("/send")
    public void send() {
        sendFunc.sendMsg("1000");
    }
}