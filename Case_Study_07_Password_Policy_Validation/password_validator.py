# ==============================================================================
# Case Study 07: Password Policy Validation and Security Audit Engine
# Syllabus elements used: Computational thinking, strings, string manipulation,
# loops, conditional statements, lists, tuples, tuple unpacking, variables.
# ==============================================================================

def validate_password_security(password_string):
    """
    Evaluates a candidate password against strict enterprise policy rules.
    Returns: (is_compliant, score, failed_rules, strength_label)
    """
    failed_rules = []
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    prohibited_substrings = ["password", "admin", "1234", "qwerty", "welcome", "letmein"]

    # 1. Length Rule
    pw_len = len(password_string)
    if pw_len < 8:
        failed_rules.append(f"Length too short ({pw_len} chars; minimum required is 8)")
    elif pw_len > 32:
        failed_rules.append(f"Length too long ({pw_len} chars; maximum allowed is 32)")

    # 2. Character Categories Rule
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password_string:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True
        elif ch >= '0' and ch <= '9':
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if not has_upper:
        failed_rules.append("Missing at least one UPPERCASE letter (A-Z)")
    if not has_lower:
        failed_rules.append("Missing at least one LOWERCASE letter (a-z)")
    if not has_digit:
        failed_rules.append("Missing at least one NUMERIC digit (0-9)")
    if not has_special:
        failed_rules.append(f"Missing at least one SPECIAL character ({special_chars[:10]}...)")

    # 3. Consecutive Character Repetition Rule (<= 2 consecutive identical characters)
    has_excess_repetition = False
    repeat_char = ""
    for i in range(len(password_string) - 2):
        if password_string[i] == password_string[i+1] == password_string[i+2]:
            has_excess_repetition = True
            repeat_char = password_string[i]
            break

    if has_excess_repetition:
        failed_rules.append(f"Contains 3 or more consecutive identical characters ('{repeat_char*3}')")

    # 4. Prohibited Substring / Common Pattern Check
    lower_pw = password_string.lower()
    found_prohibited = []
    for bad_str in prohibited_substrings:
        if bad_str in lower_pw:
            found_prohibited.append(bad_str)

    if len(found_prohibited) > 0:
        failed_rules.append(f"Contains prohibited common dictionary word(s): {', '.join(found_prohibited)}")

    # Score Evaluation
    is_compliant = (len(failed_rules) == 0)
    score = 100 - (len(failed_rules) * 18)
    if score < 0:
        score = 0

    if is_compliant:
        if pw_len >= 14 and has_special and has_digit and has_upper:
            strength_label = "EXCELLENT / ENTERPRISE COMPLIANT"
        else:
            strength_label = "STRONG / ACCEPTABLE"
    elif score >= 50:
        strength_label = "MODERATE (Needs Remediation)"
    else:
        strength_label = "WEAK / REJECTED"

    return (is_compliant, score, failed_rules, strength_label)

def audit_password_batch(candidate_passwords):
    """Audits multiple candidate passwords and prints diagnostic security report."""
    print("=" * 95)
    print("                      ENTERPRISE PASSWORD POLICY AUDIT ENGINE")
    print("=" * 95)
    print("Policy Rules: Length: 8-32 | Uppercase + Lowercase + Digit + Special | No 3x repeat | No dictionary terms")
    print("-" * 95)

    for candidate in candidate_passwords:
        is_ok, score, failures, label = validate_password_security(candidate)
        status_symbol = "[PASS]" if is_ok else "[FAIL]"

        print(f"Password Sample : '{candidate}'")
        print(f"Audit Status    : {status_symbol} Score: {score}/100 | Classification: {label}")

        if len(failures) == 0:
            print("Policy Checks   : All 7 enterprise cryptographic constraints satisfied.")
        else:
            print("Failed Rules    :")
            for reason in failures:
                print(f"   • {reason}")
        print("-" * 95)

if __name__ == "__main__":
    test_batch = [
        "pass123",                    # Too short, no upper, no special, prohibited 'pass'
        "Administrator2026!",         # Contains 'admin'
        "K9#mQ2$xP8@vL1",             # Fully compliant strong password
        "HellooooWorld123!",          # Excessive repetition 'oooo'
        "MySuperSecretP@ssw0rd2026",  # Very strong compliant
        "12345678"                    # Only digits, prohibited '1234'
    ]

    audit_password_batch(test_batch)
