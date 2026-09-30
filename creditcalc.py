import argparse
import math


class CreditCalc:
    def __init__(self, interest=0.0, principal=0, periods=0, payment=0.0):
        self.interest = interest
        self.principal = principal
        self.periods = periods
        self.payment = payment
        self.nominal_interest = interest / (100 * 12)
        try:
            self.fraction = (self.nominal_interest * (1 + self.nominal_interest) ** self.periods /
                       ((1 + self.nominal_interest) ** self.periods - 1))
        except ZeroDivisionError:
            self.fraction = 0


    def annuity(self):
        if self.payment == 0.0:
            self.payment = math.ceil(self.principal * self.fraction)
        elif self.periods == 0:
            argument = self.payment / (self.payment - self.nominal_interest * self.principal)
            base = 1 + self.nominal_interest
            self.periods = math.ceil(math.log(argument) / math.log(base))
        elif self.principal == 0:
            self.principal = round((self.payment / self.fraction))


    def diff(self):
        pass


parser = argparse.ArgumentParser(description='Loan Calculator')
interest = parser.add_argument('--interest', type=float)
principal = parser.add_argument('--principal', type=float, default=0)
periods = parser.add_argument('--periods', type=int, default=0)
payment = parser.add_argument('--payment', type=float, default=0)
type_loan = parser.add_argument('--type', type=str)

try:
    if type_loan != 'annuity' or type_loan != 'diff':
        raise ValueError('Incorrect parameters')
    elif interest == 0.0:
        raise ValueError('Incorrect parameters')
except ValueError as e:
    print(e)



guriy = CreditCalc(interest=10, principal=1000000, payment=15000)
guriy.annuity()

print(guriy.periods)
print(guriy.payment)
print(guriy.principal)
print(guriy.interest)
