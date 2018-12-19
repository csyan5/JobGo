package com.sfu.dior.utils;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;
import javax.servlet.annotation.WebListener;

import org.springframework.stereotype.Component;

@WebListener
@Component
public class MyContextListener implements ServletContextListener {
	
	private SSHConnection conexionssh;
	
	
	public MyContextListener()
	{
	    super();
	}
	
	/**
	 * @see ServletContextListener#contextInitialized(ServletContextEvent)
	 */
	public void contextInitialized(ServletContextEvent arg0) 
	{
	    System.out.println("Context initialized ... !");
	    try 
	        {
	            conexionssh = new SSHConnection();
	        } 
	    catch (Throwable e) 
	        {
	            e.printStackTrace(); // error connecting SSH server
	        }
	}
	
	/**
	 * @see ServletContextListener#contextDestroyed(ServletContextEvent)
	 */
	public void contextDestroyed(ServletContextEvent arg0) 
	{
	    System.out.println("Context destroyed ... !");
	    conexionssh.closeSSH(); // disconnect
	}
}
