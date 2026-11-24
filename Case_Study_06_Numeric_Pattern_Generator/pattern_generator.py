# ==============================================================================
# Case Study 06: Advanced Numeric and Geometric Pattern Generator
# Syllabus elements used: Computational thinking, loops, nested loops,
# pattern generation, conditional statements, variables, strings.
# ==============================================================================

def generate_hollow_diamond(n):
    """
    Generates a hollow diamond pattern with exact dimensional validation.
    n must be an odd positive integer >= 3.
    """
    print("\n" + "=" * 50)
    print(f"PATTERN 1: HOLLOW DIAMOND (Height: {n})")
    print("=" * 50)

    # Input validation
    if n <= 0:
        print("[!] Error: Dimension must be a positive integer.")
        return False
    if n % 2 == 0:
        print(f"[!] Error: {n} is even. A symmetric hollow diamond requires an ODD dimension (e.g. 5, 7, 9, 11).")
        return False

    half = n // 2

    # Top Half (including middle row)
    for i in range(half + 1):
        outer_spaces = half - i
        if i == 0:
            print(" " * outer_spaces + "*")
        else:
            inner_spaces = 2 * i - 1
            print(" " * outer_spaces + "*" + " " * inner_spaces + "*")

    # Bottom Half
    for i in range(half - 1, -1, -1):
        outer_spaces = half - i
        if i == 0:
            print(" " * outer_spaces + "*")
        else:
            inner_spaces = 2 * i - 1
            print(" " * outer_spaces + "*" + " " * inner_spaces + "*")

    return True

def generate_symmetric_number_pyramid(rows):
    """
    Generates a symmetric palindromic number pyramid.
    Each row i starts from 1 up to i, and counts back down to 1.
    """
    print("\n" + "=" * 50)
    print(f"PATTERN 2: SYMMETRIC PALINDROMIC NUMBER PYRAMID ({rows} Rows)")
    print("=" * 50)

    if rows < 1 or rows > 9:
        print("[!] Error: Rows must be between 1 and 9 to maintain single-digit alignment.")
        return False

    for i in range(1, rows + 1):
        # Leading spaces for center alignment
        spaces = "  " * (rows - i)
        row_str = spaces

        # Ascending numbers
        for j in range(1, i + 1):
            row_str += str(j) + " "

        # Descending numbers
        for j in range(i - 1, 0, -1):
            row_str += str(j) + " "

        print(row_str)

    return True

def generate_binary_floyds_triangle(rows):
    """
    Generates an alternating binary Floyd's Triangle.
    Alternates between 1 and 0 based on row and column parity.
    """
    print("\n" + "=" * 50)
    print(f"PATTERN 3: ALTERNATING BINARY FLOYD'S TRIANGLE ({rows} Rows)")
    print("=" * 50)

    if rows < 1:
        print("[!] Error: Number of rows must be >= 1.")
        return False

    for i in range(1, rows + 1):
        row_str = ""
        for j in range(1, i + 1):
            # If sum of indices is even, print 1, else 0
            if (i + j) % 2 == 0:
                row_str += "1 "
            else:
                row_str += "0 "
        print(row_str)

    return True

if __name__ == "__main__":
    # Test executions with validation demonstration
    print("DEMONSTRATING PATTERN GENERATOR WITH DIMENSION VALIDATION:")

    # 1. Invalid Even Dimension for Diamond
    generate_hollow_diamond(6)

    # 2. Valid Odd Dimension for Diamond
    generate_hollow_diamond(9)

    # 3. Symmetric Palindromic Number Pyramid
    generate_symmetric_number_pyramid(6)

    # 4. Alternating Binary Floyd's Triangle
    generate_binary_floyds_triangle(7)
