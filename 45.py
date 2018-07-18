def tax(money):
    if money <= 3500:
        return print(money)
    elif money >=3500 and money <= 5000:
        return print(money-(money-3500)*0.03)
    elif money > 5000 and money <= 9000:
        return print(money-(money-5000)*0.1-(5000-3500)*0.03)
    elif money > 9000 and money <= 12500:
        return print(money-(money-9000)*0.2-(9000-5000)*0.1-(5000-3500)*0.03)
    elif money > 12500 and money <= 38500:
        return print(money-(money-12500)*0.25-(12500-9000)*0.2-(9000-5000)*0.1-(5000-3500)*0.03)
    elif money > 38500 and money <= 58500:
        return print(money-(money-38500)*0.3-(38500-12500)*0.25-(12500-9000)*0.2-(9000-5000)*0.1-(5000-3500)*0.03)
    elif money > 58500 and money <=83500:
        return print(money-(money-58500)*0.35-(58500-38500)*0.3-(38500-12500)*0.25-(12500-9000)*0.2-(9000-5000)*0.1-(5000-3500)*0.03)
    elif money > 83500:
        return print(money-(money-83500)*0.45-(83500-58500)*0.35-(58500-38500)*0.3-(38500-12500)*0.25-(12500-9000)*0.2-(9000-5000)*0.1-(5000-3500)*0.03)
money = float(input('输入金额：'))
a = tax(money)
