import argparse
import math


class CreditCalc:
    def __init__(self, interest=0.0, principal=0, periods=0, payment=0.0):
        self.interest = interest
        self.principal = principal
        self.periods = periods
        self.payment = payment

        try:
            self.nominal_interest = interest / (100 * 12)
        except ZeroDivisionError:
            self.nominal_interest = 0.0

        try:
            self.fraction = (self.nominal_interest * (1 + self.nominal_interest) ** self.periods /
                             ((1 + self.nominal_interest) ** self.periods - 1))
        except ZeroDivisionError:
            self.fraction = 0

    def annuity(self):
        if self.payment == 0.0:
            self.payment = math.ceil(self.principal * self.fraction)
        elif self.periods == 0:
            if self.interest > 0.0:
                argument = self.payment / (self.payment - self.nominal_interest * self.principal)
                base = 1 + self.nominal_interest
                self.periods = math.ceil(math.log(argument) / math.log(base))
            else:
                self.periods = math.ceil(self.principal / self.payment)
        elif self.principal == 0:
            self.principal = int(self.payment // self.fraction)

    def diff(self, period_months):
        self.payment = math.ceil((self.principal / self.periods + self.nominal_interest *
                                  (self.principal - (self.principal * (period_months - 1) / self.periods))))


def zero_count(*mth):
    z_count = sum(1 for x in mth if x == 0)
    if z_count > 1:
        return False
    else:
        return True


def check_arguments(type_loan, interest, principal, periods, payment):
    parameters = 'Incorrect parameters'
    try:
        if type_loan not in ['annuity', 'diff']:
            raise ValueError(parameters)
        elif not interest or interest <= 0:
            raise ValueError(parameters)
        #  проверка на отрицательные значения
        elif any(x < 0 for x in (principal, periods, payment)):
            raise ValueError(parameters)
        elif type_loan == 'annuity':
            if not zero_count(principal, periods, payment):
                raise ValueError(parameters)
        elif type_loan == 'diff':
            if payment:
                raise ValueError(parameters)
            elif not zero_count(principal, periods):
                raise ValueError(parameters)
    except ValueError:
        return parameters


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Loan Calculator')

    parser.add_argument('--interest', type=float, default=None)
    parser.add_argument('--type', type=str, default=None)
    parser.add_argument('--principal', type=float, default=0.0)
    parser.add_argument('--periods', type=int, default=0)
    parser.add_argument('--payment', type=float, default=0.0)

    args = parser.parse_args()

    check = check_arguments(type_loan=args.type, interest=args.interest,
                            principal=args.principal, periods=args.periods, payment=args.payment)
    if check:
        print(check)
    else:
        guriy = CreditCalc(interest=args.interest, principal=args.principal, periods=args.periods, payment=args.payment)
        if args.type == 'diff':
            count = 0
            for i in range(1, args.periods + 1):
                guriy.diff(i)
                print(f'Month {i}: payment is {guriy.payment}')
                count += guriy.payment
            print()
            print(f"Overpayment = {round(count - guriy.principal)}")
        else:
            guriy.annuity()
            if not args.payment:
                print(f"Your annuity payment = {guriy.payment}!")
            elif not args.principal:
                print(f"Your annuity principal = {guriy.principal}!")
            else:
                years = guriy.periods // 12
                months = math.ceil(guriy.periods % 12)
                print(f"It will take {str(years) + ' years' if years > 0 else ''} "
                      f"{'and ' + str(months) + ' months ' if months > 0 else ''}to repay this loan!")

            print(f"Overpayment = {round(guriy.payment * guriy.periods - guriy.principal)}!")
