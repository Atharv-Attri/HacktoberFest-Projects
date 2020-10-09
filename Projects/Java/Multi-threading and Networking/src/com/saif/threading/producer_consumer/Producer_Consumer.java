package com.saif.threading.producer_consumer;

import com.saif.threading.ThreadColor;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.locks.ReentrantLock;

/*
  Buffer acts as the shared resource(critical section) between the two threads.
  The producer produces new items and places them on the buffer.
  The consumer threads consume the items if buffer is not empty.
  All threads access the shared buffer concurrently.
  The bufferLock ensures there is mutual exclusion while accessing the buffer.
*/

public class Producer_Consumer {

    public static void main(String[] args) {

        List<Integer> buffer = new ArrayList<>(); // ArrayList is an unsynchronized and non thread-safe data structure
        ReentrantLock bufferLock = new ReentrantLock();
        MyProducer producer = new MyProducer(ThreadColor.ANSI_CYAN, buffer, bufferLock);
        MyConsumer consumer1 = new MyConsumer(ThreadColor.ANSI_YELLOW, buffer, bufferLock);
        MyConsumer consumer2 = new MyConsumer(ThreadColor.ANSI_PURPLE, buffer, bufferLock);

        new Thread(producer).start();
        new Thread(consumer1).start();
        new Thread(consumer2).start();
    }

}

class MyProducer implements Runnable {
    private final String color;
    private List<Integer> buffer;
    private ReentrantLock bufferLock;

    public MyProducer(String color, List<Integer> buffer, ReentrantLock bufferLock) {
        this.color = color;
        this.buffer = buffer;
        this.bufferLock = bufferLock;
    }

    @Override
    public void run() {
        Random random = new Random();
//        String[] nums = {"1","2","3","4","5",};

        while (true) {
            try {
                int num = random.nextInt(100);
                System.out.println(color + "Adding " + num + " to buffer");
                bufferLock.lock();
                try {
                    buffer.add(num);
                } finally {
                    bufferLock.unlock();
                }
                Thread.sleep(random.nextInt(1000)); // milliseconds
            } catch (InterruptedException e) {
                System.out.println("Producer was interrupted");
            }
        }
//        System.out.println("Adding EOF and exiting");
//        bufferLock.lock();
//        try{
//            buffer.add(EOF);
//        }finally{
//            bufferLock.unlock();
//        }
    }
}

class MyConsumer implements Runnable {
    private final String color;
    private List<Integer> buffer;
    private ReentrantLock bufferLock;

    public MyConsumer(String color, List<Integer> buffer, ReentrantLock bufferLock) {
        this.color = color;
        this.buffer = buffer;
        this.bufferLock = bufferLock;
    }

    @Override
    public void run() {
        while (true) {
            bufferLock.lock();
            try {
                if (!buffer.isEmpty()) {
                    System.out.println(color + "Removed " + buffer.remove(0));
                }
//                if(buffer.get(0).equals(EOF)){
//                    System.out.println(color + "Exiting");
//                    break;
//                }
            } finally {
                bufferLock.unlock();
            }
        }
    }
}
