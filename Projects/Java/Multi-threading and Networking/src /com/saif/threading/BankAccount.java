package com.saif.threading;

import java.util.concurrent.TimeUnit;
import java.util.concurrent.locks.ReentrantLock;

public class BankAccount {
    private String accountNumber;
    private double balance;
    private ReentrantLock vault;

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
        this.vault = new ReentrantLock();
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    // read-only methods are thread-safe
    public double getBalance() {
        return balance;
    }

    // non thread-safe method
    public boolean unsafeDeposit(double amount) {
        if (amount < 0) {
            System.out.println("Invalid Amount");
            return false;
        } else {
            this.balance += amount;
            return true;
        }
    }

    // non thread-safe method
    public boolean unsafeWithdraw(double amount) {
        if (amount < 0) {
            System.out.println("Invalid Amount");
        } else if (amount > this.balance) {
            System.out.println("Not enough balance");
        } else {
            this.balance -= amount;
            return true;
        }
        return false;
    }

    // thread-safe implementation using synchronized key word
    public synchronized boolean deposit(double amount) {
        return unsafeDeposit(amount);
    }

    // thread-safe implementation using synchronized key word
    public synchronized boolean withdraw(double amount) {
        return unsafeWithdraw(amount);
    }

    // thread-safe implementation using synchronization block
    public void syncDeposit(double amount) {
        if (amount < 0) {
            System.out.println("Invalid Amount");
        } else {
            synchronized (this) {
                this.balance += amount;
            }
        }
    }

    // thread-safe implementation using synchronization block
    public boolean syncWithdraw(double amount) {
        synchronized (this) {
            if (amount < 0) {
                System.out.println("Invalid Amount");
            } else if (amount > this.balance) {
                System.out.println("Not enough balance");
            } else {
                this.balance -= amount;
                return true;
            }
        }
        return false;
    }

    // thread-safe implementation using Reentrant Lock
    public boolean depositWithLock(double amount) {
        if (amount < 0) {
            System.out.println("Invalid Amount");
        } else {
            vault.lock();
            try {
                this.balance += amount;
                return true;
            } finally {
                vault.unlock();
            }
        }
        return false;
    }

    // thread-safe implementation using Reentrant Lock
    public boolean withdrawWithLock(double amount) {
        vault.lock();
        try {
            if (amount < 0) {
                System.out.println("Invalid Amount");
            } else if (amount > this.balance) {
                System.out.println("Not enough balance");
            } else {
                this.balance -= amount;
                return true;
            }
        } finally {
            vault.unlock();
        }
        return false;
    }

    // thread-safe implementation using Reentrant Lock and tryLock method
    public boolean tryLockDeposit(double amount) {
        try {
            if (vault.tryLock(1000, TimeUnit.MILLISECONDS)) {
                try {
                    return unsafeDeposit(amount);
                } finally {
                    vault.unlock();
                }
            } else {
                System.out.println("Couldn't get lock due to timeout");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return false;
    }

    // thread-safe implementation using Reentrant Lock and tryLock method
    public boolean tryLockWithdraw(double amount) {
        try {
            if (vault.tryLock(1000, TimeUnit.MILLISECONDS)) {
                try {
                    return unsafeWithdraw(amount);
                } finally {
                    vault.unlock();
                }
            } else {
                System.out.println("Couldn't get lock due to timeout");
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        return false;
    }

    // thread-safe implementation for transferring amounts from one account to another account
    public void transfer(BankAccount destination, double amount) {
        if (this.withdraw(amount)) {
            if (destination.deposit(amount)) {
                System.out.println("Transfer Completed on " + Thread.currentThread().getName());
            } else {
                System.out.println("Transfer failed on " + Thread.currentThread().getName());
                System.out.println("Returning amount " + amount + " to account " + this.accountNumber);
            }
        } else {
            System.out.println("Transfer failed on " + Thread.currentThread().getName());
        }
    }

}
