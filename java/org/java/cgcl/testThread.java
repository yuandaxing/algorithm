package org.java.cgcl;
import java.io.IOException;
public class testThread extends Thread {

public testThread() {
}
/** *//**
* 线程的run方法，它将和其他线程同时运行
*/
    public void run(){
for(int i = 1; i <= 100; i++){
try{
Thread.sleep(100);

} catch (InterruptedException ex){
ex.printStackTrace();
}
System.out.println(i);
}
}
public static void main(String [] args){
testThread test = new testThread();
test.setDaemon(true);
test.start();
System.out.println("isDaemon = " + test.isDaemon());
try {
System.in.read(); // 接受输入，使程序在此停顿，一旦接收到用户输入，main线程结束，守护线程自动结束
} catch (IOException ex) {
ex.printStackTrace();
}
}
}