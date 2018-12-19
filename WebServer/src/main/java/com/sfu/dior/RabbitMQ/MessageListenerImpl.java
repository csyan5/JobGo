package com.sfu.dior.RabbitMQ;
import java.io.UnsupportedEncodingException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.slf4j.Logger;
import org.springframework.amqp.core.Message;
import org.springframework.amqp.core.MessageListener;

import com.sfu.dior.utils.CommonUtils;

public class MessageListenerImpl implements MessageListener {
	private Logger logger = CommonUtils.getLogger();
	private boolean finished = false;
	private String res;
	
	@Override
	public void onMessage(Message message) {
		// TODO Auto-generated method stub
		logger.info("received: " + message);
        try {
            String res = new String(message.getBody(), "UTF-8");
            String context = "now date ".concat(new SimpleDateFormat("yyyy-MM-dd HH:mm:dd").format(new Date()));
            logger.info("received at: " + context);
            logger.info("received data: " + res);
            this.finished = true;
            this.res = res;
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
	}
	
	public String getRes() {
		return this.res;
	}
	
	public boolean isFinished() {
		return this.finished;
	}
	
	public void reset() {
		this.res = "";
		this.finished = false;
	}
}
