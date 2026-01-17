# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
def calculate_average_order_value(orders):
    # Handles edge case of empty orders list
    if not orders:
        return 0

    valid_orders = [o for o in orders if o.get("status") != "cancelled"]
    
    
    if not valid_orders:
        return 0

    total_amount = sum(order.get("amount", 0) for order in valid_orders)
    
    # Divide by the filtered count, not the original count
    return total_amount / len(valid_orders)