public class BankAccountFixed {
    private double balance;
    private String owner;

    public BankAccountFixed(String owner, double initialBalance) {
        this.owner = owner;
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        balance += amount;
    }

    public boolean withdraw(double amount) {
        if (amount > balance) {
            return false;
        }
        balance -= amount;
        return true;
    }

    public double getBalance() {
        return balance;
    }

    public static void main(String[] args) {
        BankAccountFixed account = new BankAccountFixed("Alice", 1000.0);
        account.deposit(500.0);
        System.out.println("After deposit: " + account.getBalance());
        account.withdraw(200.0);
        System.out.println("After withdrawal: " + account.getBalance());
        boolean result = account.withdraw(99999.0);
    }
}
