# ==============================================================================
# Master Test Runner: Python Activity-Based Learning (10 Case Studies)
# ==============================================================================
import os
import sys
import subprocess

CASE_STUDIES = [
    ("Case Study 01: University Scholarship Allocation", 
     "Case_Study_01_University_Scholarship", "scholarship_allocation.py"),
    ("Case Study 02: Progressive Electricity Billing", 
     "Case_Study_02_Progressive_Electricity_Billing", "electricity_billing.py"),
    ("Case Study 03: Employee Payroll & Deduction Analysis", 
     "Case_Study_03_Employee_Payroll_Analysis", "payroll_analysis.py"),
    ("Case Study 04: Railway Fare & Reservation Calculator", 
     "Case_Study_04_Railway_Fare_Calculator", "railway_fare.py"),
    ("Case Study 05: Retail Billing with Multiple Discounts", 
     "Case_Study_05_Retail_Billing_Discount", "retail_billing.py"),
    ("Case Study 06: Advanced Numeric Pattern Generator", 
     "Case_Study_06_Numeric_Pattern_Generator", "pattern_generator.py"),
    ("Case Study 07: Password Policy Validation Engine", 
     "Case_Study_07_Password_Policy_Validation", "password_validator.py"),
    ("Case Study 08: Student Performance Trend & Marks Matrix", 
     "Case_Study_08_Student_Marks_Matrix_Analysis", "marks_matrix_analysis.py"),
    ("Case Study 09: Tuple-Based Shift Conflict Detection", 
     "Case_Study_09_Tuple_Shift_Conflict_Detection", "shift_conflict_detection.py"),
    ("Case Study 10: ATM Menu-Driven Banking Simulation", 
     "Case_Study_10_ATM_Banking_Simulation", "atm_simulation.py")
]

def run_suite():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print("=" * 85)
    print("       PYTHON ACTIVITY-BASED LEARNING: AUTOMATED 10 CASE STUDIES RUNNER")
    print("=" * 85)
    print(f"Executing with Python: {sys.version.split()[0]} | Working Dir: {base_dir}")
    print("-" * 85)

    passed = 0
    failed = 0

    for idx, (title, folder, script) in enumerate(CASE_STUDIES, 1):
        script_path = os.path.join(base_dir, folder, script)
        print(f"\n[{idx}/10] RUNNING: {title} ...")
        print("-" * 85)
        
        if not os.path.exists(script_path):
            print(f"[-] ERROR: Script not found: {script_path}")
            failed += 1
            continue

        try:
            # Execute script
            res = subprocess.run([sys.executable, script_path], capture_output=True, text=True, check=True)
            print(res.stdout)
            passed += 1
            print(f"[+] {title} completed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"[-] FAILED with Exit Code {e.returncode}:")
            print(e.stderr)
            failed += 1

    print("\n" + "=" * 85)
    print("                              TEST RUN SUMMARY")
    print("=" * 85)
    print(f"Total Case Studies Evaluated : {len(CASE_STUDIES)}")
    print(f"Passed Successfully          : {passed}")
    print(f"Failed                       : {failed}")
    if failed == 0:
        print("ALL 10 CASE STUDIES PASSED WITH 100% SUCCESS!")
    print("=" * 85)

if __name__ == "__main__":
    run_suite()
