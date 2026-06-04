product_one = input("Which product did you buy?")
price_one = float(input("How much was it?"))
product_two = input("Which product did you buy?")
price_two = float(input("How much was it?"))
product_three = input("Which product did you buy?")
price_three = float(input("How much was it?"))

total = price_one + price_two + price_three

if total > 200:
    print(f"{product_one} ------------ ${price_one}")
    print(f"{product_two} ------------ ${price_two}")
    print(f"{product_three} ------------ ${price_three}")
    discount = total - (total * 0.1)
    print(
        f"Your discounted price is ${discount}. Your initial total amount was ${total}"
    )
else:
    print(f"{product_one} ------------ ${price_one}")
    print(f"{product_two} ------------ ${price_two}")
    print(f"{product_three} ------------ ${price_three}")
    print(f"Your total amount is ${total}")

# add shopping cart total - conditional discount and itemized summary
