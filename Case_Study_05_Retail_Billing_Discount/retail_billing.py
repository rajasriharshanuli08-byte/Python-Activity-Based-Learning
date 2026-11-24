# ==============================================================================
# Case Study 05: Retail Billing System with Multiple Discount Rules
# Syllabus elements used: Computational thinking, variables, data types,
# operators, conditional statements, loops, lists, tuples, tuple unpacking, strings.
# ==============================================================================

def generate_retail_invoice(store_name, customer_name, cart_items):
    """Processes product lists, applies tiered discounts & category taxes, prints tax invoice."""
    # Tax rates by category: [category_name, gst_rate]
    tax_rules = [
        ("Grocery",     0.00),
        ("Apparel",     0.05),
        ("Cosmetics",   0.12),
        ("Electronics", 0.18)
    ]

    print("=" * 105)
    print(f"                                   {store_name.upper()}")
    print("                              TAX INVOICE & RETAIL RECEIPT")
    print("=" * 105)
    print(f"Customer Name : {customer_name:<30} Date: 2026-11-24")
    print("Discount Policy: Bulk Buy (Qty >= 3): 10% Off Item | Cart > 2k: 5% Off | Cart > 5k: 10% Off (Max 1k)")
    print("-" * 105)
    print(f"{'Code':<8} {'Item Description':<22} {'Category':<14} {'Qty':<5} {'Price':<8} {'Item Disc':<11} {'Taxable':<10} {'GST%':<6} {'GST (Rs)':<9} {'Total (Rs)':<10}")
    print("-" * 105)

    subtotal_gross = 0.0
    total_item_discounts = 0.0
    total_taxable_value = 0.0
    total_gst_amount = 0.0

    processed_lines = []

    for item in cart_items:
        # Tuple unpacking
        item_code, item_name, category, unit_price, quantity = item

        item_gross = unit_price * quantity
        subtotal_gross += item_gross

        # 1. Bulk quantity discount: 10% off if qty >= 3
        if quantity >= 3:
            item_discount = item_gross * 0.10
        else:
            item_discount = 0.0

        total_item_discounts += item_discount
        taxable_item_value = item_gross - item_discount
        total_taxable_value += taxable_item_value

        # 2. Determine Category GST Rate
        gst_rate = 0.05 # default
        for rule in tax_rules:
            cat_name, rate = rule
            if cat_name.lower() == category.lower():
                gst_rate = rate
                break

        gst_amount = taxable_item_value * gst_rate
        total_gst_amount += gst_amount
        line_total = taxable_item_value + gst_amount

        processed_lines.append((
            item_code, item_name, category, quantity, unit_price,
            item_discount, taxable_item_value, int(gst_rate * 100), gst_amount, line_total
        ))

        print(f"{item_code:<8} {item_name:<22} {category:<14} {quantity:<5} {unit_price:<8.2f} {item_discount:<11.2f} {taxable_item_value:<10.2f} {int(gst_rate*100):<2}%   {gst_amount:<9.2f} {line_total:<10.2f}")

    # 3. Overall Cart Threshold Discount
    cart_discount = 0.0
    discount_tier = "None"

    if total_taxable_value >= 5000:
        cart_discount = total_taxable_value * 0.10
        if cart_discount > 1000.0: # Cap limit
            cart_discount = 1000.0
        discount_tier = "10% Super Saver (Capped at Rs 1000)"
    elif total_taxable_value >= 2000:
        cart_discount = total_taxable_value * 0.05
        if cart_discount > 300.0: # Cap limit
            cart_discount = 300.0
        discount_tier = "5% Smart Shopper (Capped at Rs 300)"

    final_payable = (total_taxable_value - cart_discount) + total_gst_amount
    total_savings = total_item_discounts + cart_discount

    print("-" * 105)
    print(f"{'Gross Items Subtotal':<45} : Rs. {subtotal_gross:>10.2f}")
    print(f"{'Item-Level Quantity Savings':<45} : Rs. -{total_item_discounts:>9.2f}")
    print(f"{'Taxable Merchandise Value':<45} : Rs. {total_taxable_value:>10.2f}")
    print(f"{'Cart Threshold Discount [' + discount_tier + ']':<45} : Rs. -{cart_discount:>9.2f}")
    print(f"{'Total Applicable GST Tax':<45} : Rs. {total_gst_amount:>10.2f}")
    print("=" * 105)
    print(f"{'NET PAYABLE AMOUNT (ROUNDED)':<45} : Rs. {round(final_payable):>10.2f}")
    print(f"{'TOTAL CUSTOMER SAVINGS TODAY':<45} : Rs. {total_savings:>10.2f}  🎉")
    print("=" * 105)

if __name__ == "__main__":
    # Test shopping cart
    # Format: (item_code, name, category, unit_price, quantity)
    sample_cart = [
        ("PRD01", "Basmati Rice 5kg",     "Grocery",     450.00, 2),
        ("PRD02", "Organic Almonds 500g", "Grocery",     380.00, 3), # Qty >= 3 discount
        ("PRD03", "Cotton Polo T-Shirt",   "Apparel",     899.00, 2),
        ("PRD04", "Wireless Bluetooth Buds","Electronics",1499.00, 1),
        ("PRD05", "Natural Herbal Shampoo", "Cosmetics",  275.00, 4)  # Qty >= 3 discount
    ]

    generate_retail_invoice("Reliance Smart Hypermarket", "Sunita Deshmukh", sample_cart)
