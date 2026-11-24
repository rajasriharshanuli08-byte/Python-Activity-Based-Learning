# Case Study 06: Advanced Numeric and Geometric Pattern Generator

## 1. Problem Statement
Pattern generation exercises form the bedrock of algorithmic discipline, teaching multi-index coordination, coordinate geometry transformations, and nested iterative constraints. The problem requires generating symmetric hollow geometric figures (hollow diamond), palindromic numeric pyramids, and binary logic triangles while validating user-supplied dimensions against structural parity constraints.

## 2. Objectives
- Implement a hollow star diamond with space-character algebra and strict odd-dimension verification.
- Build a symmetric palindromic numeric pyramid with ascending and descending inner loops.
- Construct an alternating binary Floyd's triangle using parity arithmetic $(i + j) \pmod 2$.
- Prevent misaligned terminal output through comprehensive input boundary validation.

## 3. Assumptions
- Dimensions are supplied as integer parameters.
- A symmetric hollow diamond is geometrically well-formed only when the total line count is an odd integer $\ge 3$.
- Numeric pyramids are bounded within single-digit ranges ($1 \le \text{rows} \le 9$) to preserve spacing symmetry.

## 4. Algorithm
### Hollow Diamond (Dimension $N$)
1. If $N$ is even or $N \le 0$, reject with informative error message.
2. Let $\text{half} = N // 2$.
3. For upper half ($i = 0$ to $\text{half}$):
   - Outer spaces $= \text{half} - i$.
   - If $i = 0$, print outer spaces followed by single `*`.
   - Else, inner spaces $= 2i - 1$; print outer spaces + `*` + inner spaces + `*`.
4. For lower half ($i = \text{half} - 1$ down to $0$):
   - Repeat symmetric spacing logic.

### Symmetric Number Pyramid
1. For row $i = 1$ to $\text{rows}$:
   - Print leading spaces proportional to $(\text{rows} - i)$.
   - Ascend from $j = 1$ to $i$, printing each number.
   - Descend from $j = i - 1$ down to $1$, printing each number.

### Binary Floyd's Triangle
1. For row $i = 1$ to $\text{rows}$:
   - For column $j = 1$ to $i$:
     - If $(i + j)$ is even, print `1 `, else `0 `.

## 5. Flowchart
```mermaid
flowchart TD
    Start([Start Diamond]) --> CheckOdd{Is N Odd and >= 3?}
    CheckOdd -- No --> Err[Display Parity Error & Terminate]
    CheckOdd -- Yes --> SetHalf[half = N // 2]
    SetHalf --> TopLoop{For i = 0 to half}
    TopLoop -- Next i --> TopCond{i == 0?}
    TopCond -- Yes --> TopApex[Print half spaces + '*']
    TopCond -- No --> TopHollow[Print (half - i) spaces + '*' + (2i-1) spaces + '*']
    TopApex --> TopLoop
    TopHollow --> TopLoop
    TopLoop -- Done --> BotLoop{For i = half-1 down to 0}
    BotLoop -- Next i --> BotCond{i == 0?}
    BotCond -- Yes --> BotApex[Print half spaces + '*']
    BotCond -- No --> BotHollow[Print (half - i) spaces + '*' + (2i-1) spaces + '*']
    BotApex --> BotLoop
    BotHollow --> BotLoop
    BotLoop -- Done --> End([End])
```

## 6. Pseudocode
```text
BEGIN
    FUNCTION GenerateHollowDiamond(N):
        IF N % 2 == 0 OR N < 3 THEN RETURN ERROR
        half = N // 2
        FOR i FROM 0 TO half DO
            IF i == 0 THEN PRINT SPACES(half) + "*"
            ELSE PRINT SPACES(half - i) + "*" + SPACES(2*i - 1) + "*"
        END FOR
        FOR i FROM half - 1 DOWNTO 0 DO
            IF i == 0 THEN PRINT SPACES(half) + "*"
            ELSE PRINT SPACES(half - i) + "*" + SPACES(2*i - 1) + "*"
        END FOR
    END FUNCTION
END
```

## 7. Python Source Code
Refer to the complete script in [`pattern_generator.py`](file:///c:/Users/Harsha/Downloads/New%20folder/Python-Activity-Based-Learning/Case_Study_06_Numeric_Pattern_Generator/pattern_generator.py).

## 8. Test Cases
| Test ID | Pattern | Input Dim | Expected Result | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **TC-01** | Hollow Diamond | 6 | Error: Even dimension rejected | Verifies parity constraint validation |
| **TC-02** | Hollow Diamond | 9 | Perfect 9-line hollow symmetric diamond | Validates odd dimension spacing math |
| **TC-03** | Number Pyramid | 6 | 6 rows, palindromic sequence (e.g. 1 2 3 2 1) | Validates dual inner loop counting |
| **TC-04** | Binary Triangle | 7 | 7 rows alternating 1s and 0s | Validates parity indexing logic |

## 9. Sample Output Run
```text
DEMONSTRATING PATTERN GENERATOR WITH DIMENSION VALIDATION:

==================================================
PATTERN 1: HOLLOW DIAMOND (Height: 6)
==================================================
[!] Error: 6 is even. A symmetric hollow diamond requires an ODD dimension (e.g. 5, 7, 9, 11).

==================================================
PATTERN 1: HOLLOW DIAMOND (Height: 9)
==================================================
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *

==================================================
PATTERN 2: SYMMETRIC PALINDROMIC NUMBER PYRAMID (6 Rows)
==================================================
          1 
        1 2 1 
      1 2 3 2 1 
    1 2 3 4 3 2 1 
  1 2 3 4 5 4 3 2 1 
1 2 3 4 5 6 5 4 3 2 1 

==================================================
PATTERN 3: ALTERNATING BINARY FLOYD'S TRIANGLE (7 Rows)
==================================================
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1 
```

## 10. Conclusion
This case study highlights nested loop iteration, boundary calculations, string multiplication, and parity logic, fulfilling the pattern generation syllabus requirements.
