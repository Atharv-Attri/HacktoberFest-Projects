package com.saif.threading;

/*
  Simulating concurrent bank transactions using multi-threading
*/

public class Main {

    public static void main(String[] args) {

        String mainThreadColor = ThreadColor.ANSI_WHITE;
        BankAccount account = new BankAccount("12345678", 10000.00);
        BankAccount anotherAccount = new BankAccount("987654321", 15000.00);

        Thread t1 = new Thread() {
            String color = ThreadColor.ANSI_BLUE;

            @Override
            public void run() {
                account.tryLockDeposit(2000.00);
                System.out.println(color + account.getBalance() + " after termination of "
                        + Thread.currentThread().getName());
            }
        };

        Thread t2 = new Thread() {
            String color = ThreadColor.ANSI_RED;

            @Override
            public void run() {
                account.tryLockWithdraw(4000.00);
                System.out.println(color + account.getBalance() + " after termination of "
                        + Thread.currentThread().getName());
            }
        };

        t1.setName("Thread 1");
        t2.setName("Thread 2");

        // both threads make concurrent transactions on the same account
        t1.start();
        t2.start();

        System.out.println(mainThreadColor + account.getBalance() + " from main thread");


        System.out.println(mainThreadColor + "Account: " + account.getAccountNumber()
                + " balance: " + account.getBalance());
        System.out.println(mainThreadColor + "Account: " + anotherAccount.getAccountNumber()
                + " balance: " + anotherAccount.getBalance());

        Thread t3 = new Thread(new Runnable() {
            String color = ThreadColor.ANSI_PURPLE;

            @Override
            public void run() {
                account.transfer(anotherAccount, 6000.00);
                System.out.println(color + "Account: " + account.getAccountNumber()
                        + " balance: " + account.getBalance());
                System.out.println(color + "Account: " + anotherAccount.getAccountNumber()
                        + " balance: " + anotherAccount.getBalance());
            }
        }, "Transaction 1");

        Thread t4 = new Thread(new Runnable() {
            String color = ThreadColor.ANSI_YELLOW;

            @Override
            public void run() {
                anotherAccount.transfer(account, 3000.00);
                System.out.println(color + "Account: " + account.getAccountNumber()
                        + " balance: " + account.getBalance());
                System.out.println(color + "Account: " + anotherAccount.getAccountNumber()
                        + " balance: " + anotherAccount.getBalance());
            }
        }, "Transaction 2");


        // Start Transactions Concurrently on different account transfers
        t3.start(); // transfers from account to anotherAccount
        t4.start(); // transfers from anotherAccount to account


        System.out.println(mainThreadColor + "Account: " + account.getAccountNumber()
                + " balance: " + account.getBalance());
        System.out.println(mainThreadColor + "Account: " + anotherAccount.getAccountNumber()
                + " balance: " + anotherAccount.getBalance());

    }
}
