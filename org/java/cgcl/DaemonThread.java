package org.java.cgcl;

public class DaemonThread {
public static void main(String[] args) {
Thread thread = new Thread(
// 这是匿名类的写法
new Runnable() {
public void run() {
while(true) {
System.out.print("T");
}
}
});
// 设置为Daemon线程
thread.setDaemon(true);
thread.start();
}
}
