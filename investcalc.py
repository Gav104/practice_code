def invest(amount, rate, years):
    for years in range(1, years + 1):
        rate1 = rate / 100
        amount = (amount * rate1) + amount
        print(f"Year {years}  : ${amount:,.2f}")


amount = float(input("Enter a principal amount: "))
rate1 = float(input("Enter an annual percent rate: %"))
years = int(input("Enter a number of years: "))

print(invest(amount, rate1, years))
