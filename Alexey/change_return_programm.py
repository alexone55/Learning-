
def main():
    total = float(input("How much money you need to change: ")) * 100
    quarters = 25
    dimes = 10
    nickels = 5
    money_changer(total, quarters, dimes, nickels)


def money_changer(total, quarters, dimes, nickels):
    quantity_quart = (total - (total % quarters)) / quarters
    money2 = total % quarters
    quantity_dimes = (money2 - (money2 % dimes)) / dimes
    money3 = money2 % dimes
    quantity_nickels = (money3 - (money3 % nickels)) / nickels
    pennies = money3 % nickels
    answer = f"Quarters: {int(quantity_quart)} " \
             f"\nDimes: {int(quantity_dimes)} " \
             f"\nNickels: {int(quantity_nickels)}" \
             f"\nPennies: {int(pennies)}"
    print(answer)


if __name__ == '__main__':
    main()



