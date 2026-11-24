# ==============================================================================
# Case Study 01: University Scholarship Allocation System
# Syllabus elements used: Computational thinking, variables, data types,
# operators, conditionals, loops, lists, nested lists, tuples, tuple unpacking.
# ==============================================================================

def evaluate_scholarships(student_records, max_full_scholarships, max_partial_scholarships):
    print("=" * 80)
    print("           UNIVERSITY SCHOLARSHIP ALLOCATION SYSTEM")
    print("=" * 80)
    print("Criteria:")
    print("  1. Minimum Attendance >= 75%")
    print("  2. Subject-wise minimum score >= 60 in all subjects")
    print("  3. Aggregate Percentage >= 80%")
    print("  4. Annual Family Income <= Rs. 5,00,000")
    print("Tie-Breaking Hierarchy: Aggregate % -> Attendance % -> Lower Income -> Student ID")
    print("-" * 80)

    # List to store eligible candidates
    # Each entry: [aggregate_pct, attendance, -income, student_id, name, [marks]]
    eligible_students = []
    rejected_students = []

    for record in student_records:
        # Tuple unpacking
        s_id, s_name, marks_list, attendance, income = record

        # Computational thinking: Validate subject-wise criteria
        passed_all_subjects = True
        total_marks = 0
        num_subjects = len(marks_list)

        for mark in marks_list:
            total_marks += mark
            if mark < 60:
                passed_all_subjects = False

        aggregate_pct = total_marks / num_subjects

        # Check eligibility conditions
        disqualification_reasons = []
        if attendance < 75.0:
            disqualification_reasons.append("Low attendance (" + str(attendance) + "%)")
        if not passed_all_subjects:
            disqualification_reasons.append("Subject score < 60")
        if aggregate_pct < 80.0:
            disqualification_reasons.append("Aggregate < 80% (" + str(round(aggregate_pct, 2)) + "%)")
        if income > 500000:
            disqualification_reasons.append("Income exceeds limit (Rs. " + str(income) + ")")

        if len(disqualification_reasons) == 0:
            # Storing eligible candidate with tie-breaker keys
            # Negative income is used so higher value in sorting means lower actual income
            eligible_students.append([
                aggregate_pct,
                attendance,
                -income,
                s_id,
                s_name,
                marks_list,
                income
            ])
        else:
            rejected_students.append((s_id, s_name, aggregate_pct, disqualification_reasons))

    # Manual Bubble Sort based on multi-key tie breaking
    # Key 1: aggregate_pct DESC
    # Key 2: attendance DESC
    # Key 3: income ASC (represented by -income DESC)
    # Key 4: student_id ASC
    n = len(eligible_students)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            item1 = eligible_students[j]
            item2 = eligible_students[j + 1]

            swap = False
            if item1[0] < item2[0]: # Lower aggregate
                swap = True
            elif item1[0] == item2[0]:
                if item1[1] < item2[1]: # Lower attendance
                    swap = True
                elif item1[1] == item2[1]:
                    if item1[2] < item2[2]: # Higher income
                        swap = True
                    elif item1[2] == item2[2]:
                        if item1[3] > item2[3]: # Higher student ID
                            swap = True

            if swap:
                eligible_students[j], eligible_students[j + 1] = eligible_students[j + 1], eligible_students[j]

    # Award Scholarships
    print("\n[+] RANKED ELIGIBLE CANDIDATES & SCHOLARSHIP AWARDS:")
    print(f"{'Rank':<5} {'ID':<10} {'Name':<16} {'Agg %':<8} {'Att %':<8} {'Income (Rs)':<12} {'Scholarship Category'}")
    print("-" * 80)

    rank = 1
    for student in eligible_students:
        agg, att, neg_inc, sid, sname, marks, actual_inc = student
        if rank <= max_full_scholarships:
            award = "FULL SCHOLARSHIP (100% Tuition Waiver)"
        elif rank <= (max_full_scholarships + max_partial_scholarships):
            award = "PARTIAL SCHOLARSHIP (50% Tuition Waiver)"
        else:
            award = "MERIT CERTIFICATE (Quota Filled)"

        print(f"{rank:<5} {sid:<10} {sname:<16} {agg:<8.2f} {att:<8.1f} {actual_inc:<12} {award}")
        rank += 1

    # Rejected list summary
    print("\n[-] DISQUALIFIED CANDIDATES SUMMARY:")
    print(f"{'ID':<10} {'Name':<16} {'Agg %':<8} {'Reason(s) for Rejection'}")
    print("-" * 80)
    for rej in rejected_students:
        r_id, r_name, r_agg, reasons = rej
        reasons_str = "; ".join(reasons)
        print(f"{r_id:<10} {r_name:<16} {r_agg:<8.2f} {reasons_str}")
    print("=" * 80)

# ------------------------------------------------------------------------------
# Demonstration with Test Dataset
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Sample university records
    # Format: (student_id, name, [sub1, sub2, sub3, sub4], attendance_percentage, annual_income)
    sample_records = [
        ("STU101", "Aarav Sharma", [88, 92, 85, 90], 92.5, 320000),
        ("STU102", "Diya Patel",   [78, 85, 90, 84], 88.0, 280000),
        ("STU103", "Rohan Verma",  [95, 92, 94, 91], 72.0, 180000), # Attendance fail
        ("STU104", "Ananya Sen",   [88, 92, 85, 90], 92.5, 240000), # Exact tie with Aarav, lower income
        ("STU105", "Kabir Mehta",  [90, 58, 88, 92], 85.0, 410000), # One sub < 60 fail
        ("STU106", "Sneha Reddy",  [82, 84, 86, 80], 81.0, 620000), # Income fail
        ("STU107", "Ishan Joshi",  [94, 96, 92, 90], 95.0, 350000),
        ("STU108", "Meera Nair",   [86, 88, 84, 82], 90.0, 450000)
    ]

    evaluate_scholarships(sample_records, max_full_scholarships=2, max_partial_scholarships=2)
