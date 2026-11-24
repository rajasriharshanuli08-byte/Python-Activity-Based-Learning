# ==============================================================================
# Case Study 08: Student Performance Trend and Marks Matrix Analysis
# Syllabus elements used: Computational thinking, 2D nested lists (matrices),
# loops, nested loops, conditional statements, variables, strings, formatting.
# ==============================================================================

def analyze_marks_matrix(student_names, subject_names, marks_matrix):
    """
    Performs comprehensive 2D matrix analytics on student assessment scores.
    marks_matrix is a nested list where marks_matrix[i][j] is the mark of student i in subject j.
    """
    num_students = len(student_names)
    num_subjects = len(subject_names)

    print("=" * 105)
    print("                     ACADEMIC MARKS MATRIX & CURRICULUM PERFORMANCE REPORT")
    print("=" * 105)

    # 1. Row-Wise Analysis (Student Performance)
    # Each entry: [total, percentage, grade, name, marks_row]
    student_summary = []

    for i in range(num_students):
        student_total = 0
        marks_row = marks_matrix[i]

        for score in marks_row:
            student_total += score

        percentage = student_total / num_subjects

        # Grade Determination
        if percentage >= 90.0:
            grade = "A+ (Outstanding)"
        elif percentage >= 80.0:
            grade = "A  (Excellent)"
        elif percentage >= 70.0:
            grade = "B  (Good)"
        elif percentage >= 60.0:
            grade = "C  (Average)"
        else:
            grade = "D  (Remedial)"

        student_summary.append([student_total, percentage, grade, student_names[i], marks_row])

    # 2. Column-Wise Analysis (Subject Performance & Difficulty Audit)
    # We will accumulate subject statistics
    subject_stats = [] # [avg, highest, lowest, pass_count]

    for j in range(num_subjects):
        col_sum = 0
        highest = marks_matrix[0][j]
        lowest = marks_matrix[0][j]
        pass_count = 0

        for i in range(num_students):
            val = marks_matrix[i][j]
            col_sum += val
            if val > highest:
                highest = val
            if val < lowest:
                lowest = val
            if val >= 50: # 50 is subject pass mark
                pass_count += 1

        avg = col_sum / num_students
        pass_pct = (pass_count / num_students) * 100
        subject_stats.append((subject_names[j], avg, highest, lowest, pass_pct))

    # Print Formatted Student Matrix Ledger
    header_str = f"{'Rank':<5} {'Student Name':<18} "
    for sub in subject_names:
        header_str += f"{sub[:6]:<8} "
    header_str += f"{'Total':<8} {'Agg %':<8} {'Grade'}"
    print(header_str)
    print("-" * 105)

    # Sort students descending by total marks (Bubble Sort)
    for a in range(num_students - 1):
        for b in range(num_students - 1 - a):
            if student_summary[b][0] < student_summary[b + 1][0]:
                student_summary[b], student_summary[b + 1] = student_summary[b + 1], student_summary[b]

    rank = 1
    for st in student_summary:
        tot, pct, grd, name, m_row = st
        row_str = f"{rank:<5} {name:<18} "
        for m in m_row:
            row_str += f"{m:<8} "
        row_str += f"{tot:<8} {pct:<8.1f} {grd}"
        print(row_str)
        rank += 1

    print("-" * 105)

    # 3. Print Subject-Wise Curricular Analytics
    print("\n[+] SUBJECT-WISE CURRICULUM METRICS & DIFFICULTY ASSESSMENT:")
    print(f"{'Subject':<22} {'Class Avg':<12} {'Highest':<10} {'Lowest':<10} {'Pass Rate':<12} {'Difficulty Flag'}")
    print("-" * 105)

    for s in subject_stats:
        s_name, s_avg, s_hi, s_lo, s_pass = s
        if s_avg < 65.0:
            diff_flag = "⚠️ HIGH DIFFICULTY (Needs Curriculum Review)"
        elif s_avg >= 82.0:
            diff_flag = "✅ HIGH MASTERY (Excellent)"
        else:
            diff_flag = "MODERATE DIFFICULTY (Normal)"

        print(f"{s_name:<22} {s_avg:<12.2f} {s_hi:<10} {s_lo:<10} {s_pass:<11.1f}% {diff_flag}")

    # Top Performer Recognition
    print("-" * 105)
    print(f"Top Academic Scholar : {student_summary[0][3]} with {student_summary[0][0]} Marks ({student_summary[0][1]:.2f}%)")
    print(f"Class Valedictorian  : {student_summary[1][3]} with {student_summary[1][0]} Marks ({student_summary[1][1]:.2f}%)")
    print("=" * 105)

if __name__ == "__main__":
    students = [
        "Aarav Mehta",
        "Deepika Padukone",
        "Farhan Akhtar",
        "Kareena Kapoor",
        "Ranbir Kapoor",
        "Alia Bhatt"
    ]

    subjects = [
        "Maths",
        "Physics",
        "CompSci",
        "English",
        "DataStruct"
    ]

    # 6 Students x 5 Subjects Matrix
    marks_data = [
        [95, 88, 92, 85, 90],  # Aarav
        [78, 62, 84, 88, 70],  # Deepika
        [58, 48, 65, 72, 54],  # Farhan (Hard physics/maths)
        [88, 76, 90, 89, 82],  # Kareena
        [92, 85, 96, 84, 94],  # Ranbir
        [84, 70, 88, 92, 78]   # Alia
    ]

    analyze_marks_matrix(students, subjects, marks_data)
