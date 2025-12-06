def total_by_category(expenses):
    """Compute and display totals for each category."""
    if not expenses:
        print("No expenses yet.")
        return

    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\nTotal By Category:")
    for cat, total in totals.items():
        print(f"{cat}: {total:.2f}")


def total_amount(expenses):
    """Display total amount of all expenses."""
    total = sum(e["amount"] for e in expenses)
    print("\nTotal Amount Spent:", f"{total:.2f}")
