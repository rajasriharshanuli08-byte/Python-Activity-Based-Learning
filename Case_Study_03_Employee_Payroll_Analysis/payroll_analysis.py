# ==============================================================================
# Case Study 03: Employee Payroll and Deduction Analysis System
# Syllabus elements used: Computational thinking, variables, arithmetic operators,
# conditionals, loops, strings, lists, tuples, tuple unpacking, formatted output.
# ==============================================================================

def calculate_monthly_tax(annual_taxable_income):
    """Calculates progressive income tax based on tiered income brackets."""
    tax = 0.0
    rem = annual_taxable_income

    if rem > 1000000:
        tax += (rem - 1000000) * 0.20
        rem = 1000000
    if rem > 600000:
        tax += (rem - 600000) * 0.10
        rem = 600000
    if rem > 300000:
        tax += (rem - 300000) * 0.05
        rem = 300000

    # Monthly TDS
    return tax / 12.0

def generate_payroll_statement(employee_records):
    """Processes employee records and generates comprehensive salary statements."""
    print("=" * 115)
    print("                             CORPORATE PAYROLL & TAX DEDUCTION STATEMENT")
    print("=" * 115)
    print("Allowances: DA = 40% | HRA = 20% | Overtime = Rs 350/hr | Incentive = 5% (if Basic > 50k) else 8%")
    print("Deductions: PF = 12% Basic | Professional Tax = Rs 200 | Progressive TDS based on Annual Projected")
    print("-" * 115)
    print(f"{'Emp ID':<8} {'Name':<18} {'Dept':<12} {'Basic':<9} {'Gross':<10} {'PF':<8} {'PT':<6} {'TDS':<9} {'Total Ded':<10} {'Net Salary':<11}")
    print("-" * 115)

    total_company_payout = 0.0
    total_tax_collected = 0.0
    total_pf_collected = 0.0

    processed_records = []

    for emp in employee_records:
        # Tuple unpacking
        emp_id, emp_name, dept, basic_pay, ot_hours = emp

        # Allowances
        da = basic_pay * 0.40
        hra = basic_pay * 0.20
        ot_pay = ot_hours * 350.0

        if basic_pay > 50000:
            incentive = basic_pay * 0.05
        else:
            incentive = basic_pay * 0.08

        gross_salary = basic_pay + da + hra + ot_pay + incentive

        # Deductions
        pf = basic_pay * 0.12
        professional_tax = 200.0

        # Annual projection for TDS
        annual_projected = gross_salary * 12.0
        # Standard deduction of Rs 50,000 for tax assessment
        taxable_annual = annual_projected - 50000.0
        if taxable_annual < 0:
            taxable_annual = 0.0

        monthly_tds = calculate_monthly_tax(taxable_annual)
        total_deductions = pf + professional_tax + monthly_tds
        net_salary = gross_salary - total_deductions

        # Accumulators
        total_company_payout += net_salary
        total_tax_collected += monthly_tds
        total_pf_collected += pf

        processed_records.append((
            emp_id, emp_name, dept, basic_pay, gross_salary,
            pf, professional_tax, monthly_tds, total_deductions, net_salary
        ))

        print(f"{emp_id:<8} {emp_name:<18} {dept:<12} {basic_pay:<9.0f} {gross_salary:<10.1f} {pf:<8.1f} {professional_tax:<6.0f} {monthly_tds:<9.1f} {total_deductions:<10.1f} {net_salary:<11.1f}")

    print("-" * 115)
    print(f"Total Disbursed Net Salary: Rs. {total_company_payout:,.2f}")
    print(f"Total Monthly TDS Deposited: Rs. {total_tax_collected:,.2f} | Total PF Contribution: Rs. {total_pf_collected:,.2f}")
    print("=" * 115)

    # Detailed Individual Payslip for Top Earner
    highest_earner = processed_records[0]
    for r in processed_records:
        if r[9] > highest_earner[9]:
            highest_earner = r

    print("\n" + "=" * 50)
    print("           SAMPLE GENERATED PAYSLIP")
    print("=" * 50)
    print(f"Employee ID   : {highest_earner[0]}")
    print(f"Employee Name : {highest_earner[1]}")
    print(f"Department    : {highest_earner[2]}")
    print("-" * 50)
    print(f"Basic Salary        : Rs. {highest_earner[3]:>10.2f}")
    print(f"Gross Earnings      : Rs. {highest_earner[4]:>10.2f}")
    print(f"Provident Fund (PF) : Rs. {highest_earner[5]:>10.2f}")
    print(f"Professional Tax    : Rs. {highest_earner[6]:>10.2f}")
    print(f"Income Tax (TDS)    : Rs. {highest_earner[7]:>10.2f}")
    print(f"Total Deductions    : Rs. {highest_earner[8]:>10.2f}")
    print("-" * 50)
    print(f"NET TAKE-HOME PAY   : Rs. {highest_earner[9]:>10.2f}")
    print("=" * 50)

if __name__ == "__main__":
    employees = [
        ("EMP01", "Rajesh Khanna",   "Engineering", 65000, 15),
        ("EMP02", "Sunita Nair",     "Marketing",   45000, 5),
        ("EMP03", "Amitabh Sen",     "Operations",  35000, 22),
        ("EMP04", "Priyanka Roy",    "HR",          52000, 0),
        ("EMP05", "Tanmay Kulkarni", "Engineering", 80000, 10)
    ]
    generate_payroll_statement(employees)
