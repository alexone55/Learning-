def calculate_monthly_payment(year_percent,credit_money,term):
    monthly_percent=year_percent/12/100
    annuity_coef = (monthly_percent*((1+monthly_percent)**(12*term)))/(((1+monthly_percent)**(12*term))-1)
    print(annuity_coef)
    monthly_payment = annuity_coef*credit_money
    overpay = monthly_payment*(12*term) - credit_money
    return monthly_payment, overpay


def main():
    print('This program is a mortrage calculator (annuity payment)')
    year_percent = float(input('Enter a year percent: '))
    credit_money = float(input('Enter a credit sum of money: '))
    term = float(input('Enter a term (years, int): '))
    monthly_payment, overpay = calculate_monthly_payment(year_percent,credit_money,term)
    print('Monthly payment: '+str(monthly_payment))
    print('Overpay: '+str(overpay))

# https://www.banki.ru/wikibank/raschet_annuitetnogo_plateja/
# слегка не сходится с данным сайтом, но наверное все заключается в точности округления.
if __name__=="__main__":
    main()