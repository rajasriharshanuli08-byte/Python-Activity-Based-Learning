# ==============================================================================
# Case Study 10: ATM Menu-Driven Banking Simulation System
# Syllabus elements used: Computational thinking, while loops, for loops,
# conditional statements, lists, tuples, tuple unpacking, variables, formatting.
# ==============================================================================

class ATMSystem:
    def __init__(self, account_no, pin, holder_name, initial_balance=10000.0):
        self.account_no = account_no
        self.pin = pin
        self.holder_name = holder_name
        self.balance = initial_balance
        self.daily_withdrawn = 0.0
        self.daily_limit = 25000.0
        self.min_balance = 1000.0
        self.is_locked = False

        # Transaction log stored as a list of tuples:
        # (tx_id, tx_type, amount, closing_balance, status)
        self.transactions = []
        self.tx_counter = 1001

        # Initial opening deposit log
        self.transactions.append((f"TX{self.tx_counter}", "OPENING", initial_balance, initial_balance, "SUCCESS"))
        self.tx_counter += 1

    def authenticate(self, entered_pin):
        if self.is_locked:
            return (False, "Account is currently LOCKED due to security lockout.")
        if entered_pin == self.pin:
            return (True, "Authentication Successful.")
        else:
            return (False, "Invalid PIN entered.")

    def deposit(self, amount):
        if amount <= 0:
            return (False, "Deposit amount must be strictly positive.")
        if amount % 100 != 0:
            return (False, "Deposit amount must be in multiples of Rs. 100.")

        self.balance += amount
        tx_id = f"TX{self.tx_counter}"
        self.tx_counter += 1
        self.transactions.append((tx_id, "DEPOSIT", amount, self.balance, "SUCCESS"))
        return (True, f"Rs. {amount:.2f} deposited successfully. New Balance: Rs. {self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            return (False, "Withdrawal amount must be strictly positive.")
        if amount % 100 != 0:
            return (False, "Amount must be in valid cash denominations (multiples of Rs. 100).")

        # Check daily withdrawal limit
        if (self.daily_withdrawn + amount) > self.daily_limit:
            remaining_limit = self.daily_limit - self.daily_withdrawn
            tx_id = f"TX{self.tx_counter}"
            self.tx_counter += 1
            self.transactions.append((tx_id, "WITHDRAW", amount, self.balance, "FAILED: LIMIT EXCEEDED"))
            return (False, f"Daily withdrawal limit exceeded! Remaining limit today: Rs. {remaining_limit:.2f}")

        # Check minimum balance constraint
        if (self.balance - amount) < self.min_balance:
            tx_id = f"TX{self.tx_counter}"
            self.tx_counter += 1
            self.transactions.append((tx_id, "WITHDRAW", amount, self.balance, "FAILED: LOW BALANCE"))
            return (False, f"Insufficient funds! Minimum balance of Rs. {self.min_balance:.2f} must be maintained.")

        # Execute withdrawal
        self.balance -= amount
        self.daily_withdrawn += amount
        tx_id = f"TX{self.tx_counter}"
        self.tx_counter += 1
        self.transactions.append((tx_id, "WITHDRAW", amount, self.balance, "SUCCESS"))
        return (True, f"Please collect your cash: Rs. {amount:.2f}. Available Balance: Rs. {self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def print_mini_statement(self, last_n=5):
        print("\n" + "=" * 65)
        print(f"             HDFC BANK ATM MINI-STATEMENT")
        print("=" * 65)
        print(f"Account No : {self.account_no:<20} Holder: {self.holder_name}")
        print(f"Current Available Balance : Rs. {self.balance:,.2f}")
        print("-" * 65)
        print(f"{'TX ID':<10} {'Type':<12} {'Amount (Rs)':<14} {'Closing Bal':<14} {'Status'}")
        print("-" * 65)

        # Slice last n transactions
        recent_txs = self.transactions[-last_n:]
        for tx in recent_txs:
            t_id, t_type, t_amt, t_bal, t_stat = tx
            print(f"{t_id:<10} {t_type:<12} {t_amt:<14.2f} {t_bal:<14.2f} {t_stat}")

        print("=" * 65)

def run_automated_simulation():
    """Runs a deterministic automated test bench demonstrating all ATM features."""
    print("=" * 80)
    print("           AUTOMATED ATM BANKING TEST BENCH & SIMULATION")
    print("=" * 80)

    atm = ATMSystem("100293849102", "4821", "Siddharth Malhotra", initial_balance=15000.0)
    print(f"Account Initialized: Holder: {atm.holder_name} | Balance: Rs. {atm.get_balance():,.2f}")

    # 1. Test Incorrect PIN Authentication
    print("\n[Step 1] Attempting authentication with wrong PIN '0000'...")
    auth_ok, msg = atm.authenticate("0000")
    print(f"Result: {msg}")

    # 2. Test Correct PIN Authentication
    print("\n[Step 2] Authenticating with correct PIN '4821'...")
    auth_ok, msg = atm.authenticate("4821")
    print(f"Result: {msg}")

    # 3. Test Invalid Cash Denomination Deposit
    print("\n[Step 3] Attempting deposit of Rs. 455 (not multiple of 100)...")
    ok, msg = atm.deposit(455)
    print(f"Result: {msg}")

    # 4. Test Valid Deposit
    print("\n[Step 4] Depositing valid Rs. 8,000 cash...")
    ok, msg = atm.deposit(8000)
    print(f"Result: {msg}")

    # 5. Test Valid Withdrawal
    print("\n[Step 5] Withdrawing Rs. 5,000 cash...")
    ok, msg = atm.withdraw(5000)
    print(f"Result: {msg}")

    # 6. Test Minimum Balance Constraint Violation
    print("\n[Step 6] Attempting excessive withdrawal of Rs. 18,000 (leaving < Rs. 1000 min balance)...")
    ok, msg = atm.withdraw(18000)
    print(f"Result: {msg}")

    # 7. Test Second Valid Withdrawal
    print("\n[Step 7] Withdrawing Rs. 10,000 cash...")
    ok, msg = atm.withdraw(10000)
    print(f"Result: {msg}")

    # 8. Test Daily Limit Exceeded (Daily Limit = 25,000)
    print("\n[Step 8] Attempting withdrawal of Rs. 15,000 (exceeding daily limit 25,000)...")
    ok, msg = atm.withdraw(15000)
    print(f"Result: {msg}")

    # 9. Output Mini-Statement
    atm.print_mini_statement(last_n=6)

if __name__ == "__main__":
    run_automated_simulation()
