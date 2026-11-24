# ==============================================================================
# Case Study 04: Railway Fare and Multi-Passenger Reservation Calculator
# Syllabus elements used: Computational thinking, variables, data types,
# operators, conditional statements, loops, lists, tuples, tuple unpacking, strings.
# ==============================================================================

def calculate_base_distance_fare(distance_km):
    """Calculates stepped base distance fare using tiered distance slabs."""
    fare = 0.0
    rem = distance_km

    if rem > 500:
        fare += (rem - 500) * 0.40
        rem = 500
    if rem > 100:
        fare += (rem - 100) * 0.55
        rem = 100
    if rem > 0:
        fare += rem * 0.75

    return fare

def calculate_cancellation_refund(total_fare, travel_class, hours_before_departure):
    """Computes refund and penalty based on cancellation timing."""
    if hours_before_departure > 48:
        # Flat clerkage charge
        penalty = 60.0 if travel_class == "SL" else 180.0
        if penalty > total_fare:
            penalty = total_fare
    elif 12 <= hours_before_departure <= 48:
        penalty = total_fare * 0.25
    elif 4 <= hours_before_departure < 12:
        penalty = total_fare * 0.50
    else: # < 4 hours
        penalty = total_fare

    refund = total_fare - penalty
    return (penalty, refund)

def process_reservation(pnr_number, train_name, distance_km, travel_class, passenger_list):
    """Generates an itemized passenger reservation ticket with age-based concessions."""
    # Travel Class Configuration: (class_name, multiplier, reservation_fee, superfast_charge)
    class_configs = [
        ("SL", 1.0, 20.0, 30.0),
        ("3A", 2.5, 40.0, 45.0),
        ("2A", 3.5, 50.0, 45.0),
        ("1A", 5.0, 60.0, 75.0)
    ]

    multiplier = 1.0
    res_fee = 20.0
    superfast = 30.0

    for cfg in class_configs:
        c_code, c_mult, c_res, c_sf = cfg
        if c_code == travel_class:
            multiplier = c_mult
            res_fee = c_res
            superfast = c_sf
            break

    base_km_fare = calculate_base_distance_fare(distance_km)
    class_base_fare = base_km_fare * multiplier

    print("=" * 90)
    print("                     INDIAN RAILWAYS PASSENGER RESERVATION INVOICE")
    print("=" * 90)
    print(f"PNR Number    : {pnr_number:<20} Train: {train_name}")
    print(f"Distance      : {distance_km} KM{'':<17} Class: {travel_class} (Multiplier: {multiplier}x)")
    print("-" * 90)
    print(f"{'No.':<4} {'Passenger Name':<20} {'Age':<5} {'Gender':<8} {'Concession Type':<20} {'Base Fare':<12} {'Total (Rs)':<10}")
    print("-" * 90)

    total_ticket_amount = 0.0
    passenger_index = 1
    berth_count = 0

    for p in passenger_list:
        p_name, p_age, p_gender, p_berth = p

        # Concession Rules
        if p_age < 5:
            concession_type = "Infant (Free)"
            applied_base = 0.0
            passenger_total = 0.0
        elif 5 <= p_age <= 12:
            concession_type = "Child (50% Base)"
            applied_base = class_base_fare * 0.50
            passenger_total = applied_base + res_fee + superfast
            berth_count += 1
        elif p_age >= 60:
            concession_type = "Senior Citizen (40% Off)"
            applied_base = class_base_fare * 0.60
            passenger_total = applied_base + res_fee + superfast
            berth_count += 1
        else:
            concession_type = "Standard Adult"
            applied_base = class_base_fare
            passenger_total = applied_base + res_fee + superfast
            berth_count += 1

        total_ticket_amount += passenger_total

        print(f"{passenger_index:<4} {p_name:<20} {p_age:<5} {p_gender:<8} {concession_type:<20} {applied_base:<12.2f} {passenger_total:<10.2f}")
        passenger_index += 1

    print("-" * 90)
    print(f"Total Passengers: {len(passenger_list)} (Berths Allocated: {berth_count}) | GRAND TOTAL: Rs. {total_ticket_amount:,.2f}")
    print("=" * 90)

    # Simulated Cancellation Scenarios
    print("\n--- CANCELLATION CHARGES & REFUND ESTIMATION ---")
    timing_scenarios = [72, 24, 6, 2] # hours before chart preparation
    for hrs in timing_scenarios:
        penalty, refund = calculate_cancellation_refund(total_ticket_amount, travel_class, hrs)
        print(f"Cancelled {hrs:>2} hrs prior -> Cancellation Penalty: Rs. {penalty:>8.2f} | Refund Payable: Rs. {refund:>8.2f}")
    print("=" * 90)

if __name__ == "__main__":
    sample_passengers = [
        ("Rameshwar Gupta", 63, "Male",   "Lower"),
        ("Savitri Gupta",   60, "Female", "Lower"),
        ("Alok Gupta",      34, "Male",   "Middle"),
        ("Pooja Gupta",     31, "Female", "Side Upper"),
        ("Aarav Gupta",     8,  "Male",   "Upper"),
        ("Anvi Gupta",      3,  "Female", "None") # Infant
    ]

    process_reservation("248-9102847", "12951 Mumbai Rajdhani Express", 840, "3A", sample_passengers)
