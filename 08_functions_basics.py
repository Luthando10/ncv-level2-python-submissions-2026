def place_order():
    print("Place order: your order is{item}")
    
def calculate_total(item):
    best_price = 25.5
    VAT = 0.15
    totalPrice = (base_price + len(item))* 1.15
    print(f"Place order: your order is{item}")

def get_order():
    print("Preparing order")
    return'Collect your order'
myFood = input("What would you like?: ")
place_order(myFood)

print(get_order())
order_total = calculate_total(myFood)
print(f'Your order costs: R{round(order_total,2)}')