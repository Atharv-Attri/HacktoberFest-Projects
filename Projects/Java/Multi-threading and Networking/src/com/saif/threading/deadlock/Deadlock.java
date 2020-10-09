package com.saif.threading.deadlock;

import com.saif.threading.ThreadColor;

/*
  t1 and t2 are two threads. lock1 and lock2 are the locks for two shared resources.
  t1 tries to acquire lock1 first and then lock2.
  t2 does the opposite and tries to acquire lock2 before lock1.
  Both threads acquire their first respective locks and then wait for the other thread
  to release its lock leading to a deadlock situation.
*/

public class Deadlock {

    public static Object lock1 = new Object();
    public static Object lock2 = new Object();

    public static void main(String[] args) {
        t1.start();
        t2.start();
    }

    public static Thread t1 = new Thread(new Runnable() {
        String color = ThreadColor.ANSI_GREEN;

        @Override
        public void run() {
            synchronized (lock1) {
                System.out.println(color + Thread.currentThread().getName() + " has acquired lock1");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println(color + Thread.currentThread().getName() + " is now waiting for lock2");
                synchronized (lock2) {
                    System.out.println(color + Thread.currentThread().getName() + " has acquired both lock1 and lock2");
                }
                System.out.println(color + Thread.currentThread().getName() + " has released lock2");
            }
            System.out.println(color + Thread.currentThread().getName() + " has released lock1");
        }
    }, "Thread 1");

    public static Thread t2 = new Thread(new Runnable() {
        String color = ThreadColor.ANSI_CYAN;

        @Override
        public void run() {
            synchronized (lock2) {
                System.out.println(color + Thread.currentThread().getName() + " has acquired lock2");
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println(color + Thread.currentThread().getName() + " is now waiting for lock1");
                synchronized (lock1) {
                    System.out.println(color + Thread.currentThread().getName() + " has acquired both lock1 and lock2");
                }
                System.out.println(color + Thread.currentThread().getName() + " has released lock1");
            }
            System.out.println(color + Thread.currentThread().getName() + " has released lock2");
        }
    }, "Thread 2");

}
