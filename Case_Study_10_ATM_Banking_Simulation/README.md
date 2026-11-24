# Case Study 10: ATM Menu-Driven Banking Simulation System

## 1. Problem Statement
Automated Teller Machine (ATM) software controllers require strictly audited procedural execution. Financial operations must guarantee state consistency, pin authorization, denomination verification (multiples of Rs. 100), minimum reserve thresholds, daily velocity limits, and transaction immutability. The objective is to build a menu-driven banking engine that enforces balance constraints and outputs mini-statements.

## 2. Objectives
- Model account state and immutable transaction history using Python tuples.
- Implement security validation: PIN verification and daily velocity capping (Rs. 25,000 limit).
- Enforce statutory reserve requirements: Maintain a mandatory Rs. 1,000 minimum balance on all debit requests.
- Validate currency denominations: Reject deposits and withdrawals not divisible by Rs. 100.
- Render formatted mini-statements displaying historical transactions and running closing balances.

## 3. Assumptions
- Account balances and transaction amounts are represented as non-negative floating-point values.
- Currency dispensation occurs only in valid multiples of Rs. 100.
- Daily withdrawal caps reset after 24 hours.

## 4. Algorithm
1. Initialize account parameters: `account_no`, `pin`, `holder_name`, `balance`, `daily_limit` (Rs. 25,000), and `min_balance` (Rs. 1,000).
2. Authenticate user PIN; reject if credentials fail.
3. For Deposit:
   - Check if amount $> 0$ and amount $\pmod{100} == 0$.
   - Add amount to balance and log successful deposit tuple `(tx_id, "DEPOSIT", amount, new_balance, "SUCCESS")`.
4. For Withdrawal:
   - Check if amount $> 0$ and amount $\pmod{100} == 0$.
   - If $(\text{daily\_withdrawn} + \text{amount}) > \text{daily\_limit}$, reject with limit violation.
   - If $(\text{balance} - \text{amount}) < \text{min\_balance}$, reject with insufficient funds violation.
   - Otherwise, deduct amount from balance, add to daily withdrawn total, and append successful withdrawal tuple.
5. For Mini-Statement:
   - Slice the last 5 transactions from the transaction list and print tabular receipt.

## 5. Flowchart
```mermaid
flowchart TD
    Start([Start ATM Operation]) --> Auth{PIN Valid?}
    Auth -- No --> Deny[Deny Access & Increment Failed Attempts]
    Auth -- Yes --> Menu[Display ATM Options Menu]
    Menu --> Choice{Select Action}
    Choice -- Deposit --> DepCheck{Amount > 0 AND Divisible by 100?}
    DepCheck -- Yes --> ExecDep[Credit Balance & Append TX Tuple]
    DepCheck -- No --> RejDep[Reject Invalid Denomination]
    Choice -- Withdraw --> WithCheck{Divisible by 100?}
    WithCheck -- No --> RejWith[Reject Invalid Denomination]
    WithCheck -- Yes --> LimitCheck{Daily Limit Exceeded?}
    LimitCheck -- Yes --> RejLimit[Log FAILED: LIMIT EXCEEDED]
    LimitCheck -- No --> MinBalCheck{(Balance - Amount) >= 1000?}
    MinBalCheck -- No --> RejBal[Log FAILED: LOW BALANCE]
    MinBalCheck -- Yes --> ExecWith[Dispense Cash & Update TX Log]
    Choice -- Mini-Statement --> PrintStmt[Print Last 5 Transactions Ledger]
    Choice -- Exit --> End([End Session])
    ExecDep --> Menu
    RejDep --> Menu
    RejWith --> Menu
    RejLimit --> Menu
    RejBal --> Menu
    ExecWith --> Menu
    PrintStmt --> Menu
```

## 6. Pseudocode
```text
BEGIN
    FUNCTION Withdraw(amount):
        IF amount % 100 != 0 THEN RETURN "Invalid Denomination"
        IF (daily_withdrawn + amount) > 25000 THEN
            LOG ("WITHDRAW", amount, balance, "FAILED: LIMIT")
            RETURN "Daily Limit Exceeded"
        END IF
        IF (balance - amount) < 1000 THEN
            LOG ("WITHDRAW", amount, balance, "FAILED: LOW BAL")
            RETURN "Minimum Balance Violated"
        END IF
        balance -= amount
        daily_withdrawn += amount
        LOG ("WITHDRAW", amount, balance, "SUCCESS")
        RETURN "Collect Cash"
    END FUNCTION
END
```

## 7. Python Source Code
Refer to the complete script in [`atm_simulation.py`](file:///c:/Users/Harsha/Downloads/New%20folder/Python-Activity-Based-Learning/Case_Study_10_ATM_Banking_Simulation/atm_simulation.py).

## 8. Test Cases
| Test ID | Operation | Amount | Expected Result | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | PIN Authentication | `0000` | Rejected: Invalid PIN | Access control verification |
| **TC-02** | Cash Deposit | Rs. 455 | Rejected: Not multiple of 100 | Currency denomination filter |
| **TC-03** | Cash Deposit | Rs. 8,000 | Success (Balance updated) | Credit ledger audit |
| **TC-04** | Cash Withdrawal | Rs. 18,000 | Rejected: Min balance Rs 1,000 violated | Overdraft protection |
| **TC-05** | Daily Limit Check | Rs. 15,000 | Rejected: Daily limit Rs 25,000 exceeded | Velocity threshold check |

## 9. Sample Output Run
```text
================================================================================
           AUTOMATED ATM BANKING TEST BENCH & SIMULATION
================================================================================
Account Initialized: Holder: Siddharth Malhotra | Balance: Rs. 15,000.00

[Step 1] Attempting authentication with wrong PIN '0000'...
Result: Invalid PIN entered.

[Step 2] Authenticating with correct PIN '4821'...
Result: Authentication Successful.

[Step 3] Attempting deposit of Rs. 455 (not multiple of 100)...
Result: Deposit amount must be in multiples of Rs. 100.

[Step 4] Depositing valid Rs. 8,000 cash...
Result: Rs. 8000.00 deposited successfully. New Balance: Rs. 23000.00

[Step 5] Withdrawing Rs. 5,000 cash...
Result: Please collect your cash: Rs. 5000.00. Available Balance: Rs. 18000.00

[Step 6] Attempting excessive withdrawal of Rs. 18,000 (leaving < Rs. 1000 min balance)...
Result: Insufficient funds! Minimum balance of Rs. 1000.00 must be maintained.

[Step 7] Withdrawing Rs. 10,000 cash...
Result: Please collect your cash: Rs. 10000.00. Available Balance: Rs. 8000.00

[Step 8] Attempting withdrawal of Rs. 15,000 (exceeding daily limit 25,000)...
Result: Daily withdrawal limit exceeded! Remaining limit today: Rs. 10000.00

=================================================================
             HDFC BANK ATM MINI-STATEMENT
=================================================================
Account No : 100293849102         Holder: Siddharth Malhotra
Current Available Balance : Rs. 8,000.00
-----------------------------------------------------------------
TX ID      Type         Amount (Rs)    Closing Bal    Status
-----------------------------------------------------------------
TX1002     DEPOSIT      8000.00        23000.00       SUCCESS
TX1003     WITHDRAW     5000.00        18000.00       SUCCESS
TX1004     WITHDRAW     18000.00       18000.00       FAILED: LOW BALANCE
TX1005     WITHDRAW     10000.00       8000.00        SUCCESS
TX1006     WITHDRAW     15000.00       8000.00        FAILED: LIMIT EXCEEDED
=================================================================
```

## 10. Conclusion
The ATM banking simulation demonstrates control-flow discipline using while loops, transaction list tuples, conditional safeguards, and stateful ledger management aligned with financial application patterns.
