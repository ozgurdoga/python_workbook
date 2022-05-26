def solve(meal_cost, tip_percent, tax_percent):
    tip_value = (meal_cost / 100) * tip_percent
    tax_value = (meal_cost / 100) * tax_percent
    total_bill = tax_value + meal_cost + tip_value
    print(round(total_bill))
    return


meal_cost = float(input().strip())

tip_percent = int(input().strip())

tax_percent = int(input().strip())

solve(meal_cost, tip_percent, tax_percent)
