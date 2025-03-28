def calculate_discount(price, discount):
    return price * (1 - discount / 100) if discount >= 20 else price

price = float(input("Enter price: $"))
discount = float(input("Enter discount %: "))
final = calculate_discount(price, discount)

print(f"Final price: ${final:.2f}")