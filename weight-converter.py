weight = float(input("How much do you weigh?: "))
selector = input("Choose k for kilograms or l for pounds?: ")


if selector.upper() == "K":
    kilo_formula = weight * 2.20462
    print(f"You weigh {kilo_formula}lbs.")
else:
    pounds_formula = weight / 2.20462
    print(f"You weigh {pounds_formula}kg.")
