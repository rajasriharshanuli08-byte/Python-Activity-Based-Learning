# ==============================================================================
# Case Study 09: Tuple-Based Employee Shift Conflict Detection System
# Syllabus elements used: Computational thinking, tuples, tuple unpacking,
# lists of tuples, nested loops, conditional statements, variables, strings.
# ==============================================================================

def detect_shift_conflicts(shift_records, min_rest_hours=8.0, max_daily_hours=12.0):
    """
    Audits workplace shift rosters represented as tuples:
    (shift_id, emp_id, emp_name, day, start_hr, end_hr, department)
    Detects overlapping shifts, insufficient rest intervals, and maximum daily hour violations.
    """
    print("=" * 105)
    print("                     ENTERPRISE SHIFT ROSTER & CONFLICT AUDIT REPORT")
    print("=" * 105)
    print(f"Compliance Policy: No Concurrent Shifts | Min Rest Period: {min_rest_hours} Hrs | Max Shift Hours: {max_daily_hours} Hrs/Day")
    print("-" * 105)
    print(f"{'Shift ID':<10} {'Emp ID':<8} {'Employee Name':<18} {'Day':<10} {'Start':<8} {'End':<8} {'Duration':<10} {'Department'}")
    print("-" * 105)

    for shift in shift_records:
        s_id, e_id, e_name, day, start, end, dept = shift
        dur = end - start
        print(f"{s_id:<10} {e_id:<8} {e_name:<18} {day:<10} {start:<8.2f} {end:<8.2f} {dur:<10.1f} {dept}")

    print("-" * 105)

    # Conflict Detection Engine
    conflicts_found = []
    n = len(shift_records)

    # 1. Pairwise Conflict Check (Direct Overlap and Rest Interval Check)
    for i in range(n):
        s1 = shift_records[i]
        id1, emp1, name1, day1, start1, end1, dept1 = s1

        # Check self duration
        if (end1 - start1) > max_daily_hours:
            conflicts_found.append((
                "MAX_HOURS_VIOLATION",
                f"Shift {id1} duration ({end1 - start1:.1f} hrs) exceeds maximum permitted limit ({max_daily_hours} hrs)",
                emp1, name1, day1, id1, "N/A"
            ))

        for j in range(i + 1, n):
            s2 = shift_records[j]
            id2, emp2, name2, day2, start2, end2, dept2 = s2

            # Conflicts only apply if the same employee is assigned
            if emp1 == emp2 and day1 == day2:
                # Direct Overlap condition:
                # Interval 1: [start1, end1], Interval 2: [start2, end2]
                # Overlap occurs if max(start1, start2) < min(end1, end2)
                overlap_start = start1 if start1 > start2 else start2
                overlap_end = end1 if end1 < end2 else end2

                if overlap_start < overlap_end:
                    overlap_duration = overlap_end - overlap_start
                    conflicts_found.append((
                        "DIRECT_OVERLAP",
                        f"Shifts {id1} ({dept1}) and {id2} ({dept2}) overlap by {overlap_duration:.1f} hours on {day1}",
                        emp1, name1, day1, id1, id2
                    ))
                else:
                    # Check Rest Period between shifts on same day
                    # If shift1 ends before shift2 starts
                    if end1 <= start2:
                        rest = start2 - end1
                        if rest < min_rest_hours:
                            conflicts_found.append((
                                "INSUFFICIENT_REST",
                                f"Rest period between {id1} and {id2} is only {rest:.1f} hrs (Required >= {min_rest_hours} hrs)",
                                emp1, name1, day1, id1, id2
                            ))
                    elif end2 <= start1:
                        rest = start1 - end2
                        if rest < min_rest_hours:
                            conflicts_found.append((
                                "INSUFFICIENT_REST",
                                f"Rest period between {id2} and {id1} is only {rest:.1f} hrs (Required >= {min_rest_hours} hrs)",
                                emp1, name1, day1, id1, id2
                            ))

    # Print Conflict Summary
    print("\n[!] DETECTED ROSTER SCHEDULING CONFLICTS & VIOLATIONS:")
    if len(conflicts_found) == 0:
        print("✅ No scheduling conflicts detected! Roster is 100% compliant with labor standards.")
    else:
        print(f"{'Violation Type':<22} {'Emp ID':<8} {'Employee Name':<18} {'Day':<10} {'Conflict Details'}")
        print("-" * 105)
        for conflict in conflicts_found:
            v_type, desc, c_emp, c_name, c_day, s_a, s_b = conflict
            print(f"{v_type:<22} {c_emp:<8} {c_name:<18} {c_day:<10} {desc}")

    print("=" * 105)

if __name__ == "__main__":
    # Test Roster Dataset: (shift_id, emp_id, emp_name, day, start_hr_24h, end_hr_24h, dept)
    test_shifts = [
        ("SH101", "EMP01", "Dr. Arvind Rao",    "Monday",    8.0,  16.0, "Cardiology"),
        ("SH102", "EMP01", "Dr. Arvind Rao",    "Monday",   14.0,  20.0, "Emergency OPD"), # Overlap with SH101
        ("SH103", "EMP02", "Nurse Sarah Jones", "Monday",    7.0,  15.0, "Pediatrics"),
        ("SH104", "EMP02", "Nurse Sarah Jones", "Monday",   18.0,  23.0, "ICU Night Duty"), # Insufficient rest (3 hrs)
        ("SH105", "EMP03", "Dr. Rohan Kapoor",  "Tuesday",   8.0,  22.0, "Trauma Surgery"),  # 14 hrs (exceeds max 12)
        ("SH106", "EMP04", "Tech Priya Sharma", "Tuesday",   9.0,  17.0, "Pathology"),
        ("SH107", "EMP04", "Tech Priya Sharma", "Wednesday", 9.0,  17.0, "Radiology")       # Normal
    ]

    detect_shift_conflicts(test_shifts, min_rest_hours=8.0, max_daily_hours=12.0)
