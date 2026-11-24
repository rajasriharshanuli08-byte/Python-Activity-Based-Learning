# ==============================================================================
# Case Study 02: Progressive Electricity Billing and Trend Comparison
# Syllabus elements used: Variables, data types, operators, conditional statements,
# loops, lists, nested lists, tuples, tuple unpacking, string formatting.
# ==============================================================================

def calculate_single_bill(units, has_solar_rebate=False):
    """Calculates progressive electricity charges using defined tariff slabs."""
    fixed_charge = 50.0
    energy_charge = 0.0

    # Slab Calculation
    # Slab 1: 0 - 100 units @ Rs. 1.50
    # Slab 2: 101 - 200 units @ Rs. 3.00
    # Slab 3: 201 - 500 units @ Rs. 5.50
    # Slab 4: Above 500 units @ Rs. 7.50

    remaining_units = units

    if remaining_units > 500:
        slab4_units = remaining_units - 500
        energy_charge += slab4_units * 7.50
        remaining_units = 500

    if remaining_units > 200:
        slab3_units = remaining_units - 200
        energy_charge += slab3_units * 5.50
        remaining_units = 200

    if remaining_units > 100:
        slab2_units = remaining_units - 100
        energy_charge += slab2_units * 3.00
        remaining_units = 100

    if remaining_units > 0:
        energy_charge += remaining_units * 1.50

    # Surcharge condition: 10% on energy charge if units exceed 400
    surcharge = 0.0
    if units > 400:
        surcharge = energy_charge * 0.10

    # Rebate condition: 5% discount on energy charge if solar rebate applies
    rebate = 0.0
    if has_solar_rebate:
        rebate = energy_charge * 0.05

    total_bill = fixed_charge + energy_charge + surcharge - rebate

    return (units, fixed_charge, energy_charge, surcharge, rebate, total_bill)

def analyze_household_consumption(consumer_id, consumer_name, monthly_units_data, has_solar):
    """Analyzes 6-month consumption and detects unusual consumption surges (> 25%)."""
    print("=" * 85)
    print(f"      PROGRESSIVE ELECTRICITY BILL & TREND ANALYSIS: {consumer_id} - {consumer_name}")
    print("=" * 85)
    print("Tariff Slabs: 0-100: Rs 1.50 | 101-200: Rs 3.00 | 201-500: Rs 5.50 | >500: Rs 7.50")
    print("Fixed Charge: Rs 50 | High Usage Surcharge (>400 units): 10% | Solar Rebate: 5%")
    print("-" * 85)
    print(f"{'Month':<10} {'Units':<8} {'Energy (Rs)':<12} {'Surcharge':<10} {'Rebate':<8} {'Total (Rs)':<12} {'Trend Alert'}")
    print("-" * 85)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_records = []

    total_consumption = 0
    total_amount_billed = 0.0
    previous_units = None

    for i in range(len(monthly_units_data)):
        month_name = months[i % 12]
        units = monthly_units_data[i]

        bill_tuple = calculate_single_bill(units, has_solar)
        u, fc, ec, sc, rb, total = bill_tuple

        total_consumption += u
        total_amount_billed += total

        # Unusual increase detection: > 25% rise over previous month
        alert = "Normal"
        if previous_units is not None:
            pct_change = ((units - previous_units) / previous_units) * 100
            if pct_change >= 25.0:
                alert = f"SPIKE (+{pct_change:.1f}%)"
            elif pct_change <= -25.0:
                alert = f"DROP ({pct_change:.1f}%)"

        previous_units = units
        monthly_records.append((month_name, u, ec, sc, rb, total, alert))

        print(f"{month_name:<10} {u:<8} {ec:<12.2f} {sc:<10.2f} {rb:<8.2f} {total:<12.2f} {alert}")

    print("-" * 85)
    avg_units = total_consumption / len(monthly_units_data)
    avg_bill = total_amount_billed / len(monthly_units_data)
    print(f"Total Consumption: {total_consumption} Units | Total Billed: Rs. {total_amount_billed:.2f}")
    print(f"Average Monthly Consumption: {avg_units:.1f} Units | Average Monthly Bill: Rs. {avg_bill:.2f}")

    # Identify month with maximum and minimum consumption
    max_idx = 0
    min_idx = 0
    for idx in range(1, len(monthly_units_data)):
        if monthly_units_data[idx] > monthly_units_data[max_idx]:
            max_idx = idx
        if monthly_units_data[idx] < monthly_units_data[min_idx]:
            min_idx = idx

    print(f"Peak Consumption: {months[max_idx]} ({monthly_units_data[max_idx]} units)")
    print(f"Lowest Consumption: {months[min_idx]} ({monthly_units_data[min_idx]} units)")
    print("=" * 85)

if __name__ == "__main__":
    # 6 Months test readings (Jan - Jun)
    # Notice the spike in May (AC usage in summer)
    consumption_readings = [120, 140, 180, 240, 480, 520]
    analyze_household_consumption("CON-7842", "Vikram Singhania", consumption_readings, has_solar=True)
