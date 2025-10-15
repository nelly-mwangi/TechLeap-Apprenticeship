def calculate_total_revenue(sales):
    return sum(item["price"] * item["quantity"] for item in sales)

sales_data = [
    {"item": "Pen", "price": 20, "quantity": 3},
    {"item": "Book", "price": 200, "quantity": 2},
    {"item": "Bag", "price": 800, "quantity": 1}
]

total = calculate_total_revenue(sales_data)
print(f"Total Revenue: ${total}")
