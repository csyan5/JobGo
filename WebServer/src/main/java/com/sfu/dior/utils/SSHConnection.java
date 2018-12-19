package com.sfu.dior.utils;
import com.jcraft.jsch.JSch;
import com.jcraft.jsch.Session;

public class SSHConnection {

private final static String S_PATH_FILE_PRIVATE_KEY = "/Users/mad/.ssh/sfukey"; //windows absolut path of our ssh private key locally saved
private final static String S_PATH_FILE_KNOWN_HOSTS = "/Users/mad/.ssh/known_hosts";
private final static String S_PASS_PHRASE = "";
private final static int LOCAl_PORT = 3306; 
private final static int REMOTE_PORT = 3306; 
private final static int SSH_REMOTE_PORT = 22; 
private final static String SSH_USER = "ubuntu";
private final static String SSH_REMOTE_SERVER = "nml-cloud-231.cs.sfu.ca";
private final static String MYSQL_REMOTE_SERVER = "127.0.0.1";

private Session session; //represents each ssh session

public void closeSSH ()
{
    session.disconnect();
}

public SSHConnection () throws Throwable
{

    JSch jsch = null;

        jsch = new JSch();
        jsch.setKnownHosts(S_PATH_FILE_KNOWN_HOSTS);
        jsch.addIdentity(S_PATH_FILE_PRIVATE_KEY, S_PASS_PHRASE.getBytes());

        session = jsch.getSession(SSH_USER, SSH_REMOTE_SERVER, SSH_REMOTE_PORT);
        session.setConfig("StrictHostKeyChecking", "no");
        session.connect(); //ssh connection established!

        //by security policy, you must connect through a fowarded port          
        session.setPortForwardingL(LOCAl_PORT, MYSQL_REMOTE_SERVER, REMOTE_PORT); 

}
}