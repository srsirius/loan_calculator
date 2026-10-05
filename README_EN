# Loan Calculator (CreditCalc)

A simple command-line loan calculator in Python. Supports annuity and differentiated payments, calculates overpayment, loan term, or principal depending on the provided parameters.

## Features

- **Annuity payment**: calculate monthly payment, loan term, or principal — depending on which one parameter is missing.
- **Differentiated payment**: calculate monthly payments for each month and total overpayment. In this mode, both `principal` and `periods` are required; `payment` is not an input but a calculated output.
- **Input validation**: checks for valid loan type, positive interest rate, non-negative values, and correct number of unknown parameters.
- **CLI interface**: all parameters are passed as command-line arguments.

## Requirements

- Python 3.8+
- Standard library only (no external dependencies)

## Installation and Running

Since there are no external dependencies, just clone the repo and run the script:

```bash
git clone <URL-of-repository>
cd loan-calculator
python creditcalc.py
Usage
The script accepts the following arguments:

--type — loan type: annuity or diff (required).
--interest — annual interest rate in percent (required, must be > 0).
--principal — loan principal amount.
--periods — loan term in months.
--payment — monthly payment amount (used only for annuity).
Rules for Missing Parameters
For --type annuity
Exactly one of these three parameters must be missing: principal, periods, payment. The other two must be provided.

Examples:

Missing payment: provide principal and periods.
Missing principal: provide payment and periods.
Missing periods: provide principal and payment.
For --type diff
Both --principal and --periods must be provided. If either is missing, the program returns an error.
The --payment argument must not be provided. If it is given, the program returns an error.
There is no “missing payment” concept: the program calculates and prints the payment for each month, plus the total overpayment.
Examples
Annuity: calculate monthly payment
bash
python creditcalc.py --type annuity --interest 10 --principal 500000 --periods 60
Annuity: calculate principal
bash
python creditcalc.py --type annuity --interest 10 --payment 10000 --periods 60
Annuity: calculate loan term
bash
python creditcalc.py --type annuity --interest 10 --principal 500000 --payment 10000
Diff: calculate monthly payments (both principal and periods required)
bash
python creditcalc.py --type diff --interest 10 --principal 500000 --periods 12
Diff: error — missing principal
bash
python creditcalc.py --type diff --interest 10 --periods 12
# Output: Incorrect parameters
Diff: error — missing periods
bash
python creditcalc.py --type diff --interest 10 --principal 500000
# Output: Incorrect parameters
Diff: error — payment provided
bash
python creditcalc.py --type diff --interest 10 --principal 500000 --periods 12 --payment 50000
# Output: Incorrect parameters
Expected Output (Differentiated Payment Example)
Running:

bash
python creditcalc.py --type diff --interest 10 --principal 500000 --periods 12
produces output similar to:

text
Month 1: payment is 45834
Month 2: payment is 45486
Month 3: payment is 45139
...
Month 12: payment is 41667

Overpayment = 27500
(exact values depend on rounding up per the formula).

Error Examples
Other cases that produce Incorrect parameters:

Negative values for principal, periods, or payment.
Interest rate ≤ 0.
Invalid loan type (not annuity or diff).
For annuity: more than one of principal, periods, payment missing.
For diff: --payment provided, or either --principal or --periods missing.
Calculation Logic
Nominal monthly interest rate: i = interest / (100 * 12)
Annuity factor:
fraction = i * (1 + i)^n / ((1 + i)^n - 1)
Annuity payment: A = P * fraction (rounded up to integer).
Loan term with known payment:
n = ceil(log(A / (A - i * P)) / log(1 + i))
Principal with known payment and term:
P = payment / fraction (cast to int).
Differentiated payment for month m:
D_m = P / n + i * (P - P * (m - 1) / n) (rounded up).
Project Structure
creditcalc.py — main script with CreditCalc class, validation functions, and entry point.
README.md — this documentation.
Limitations and Notes
All monetary values are rounded up to whole rubles.
Interest rate must be positive.
Negative values for any parameter are treated as invalid.
In diff mode, --principal and --periods are mandatory; --payment must not be provided.
Contributing
If you’d like to suggest improvements or fix a bug, please open an issue or submit a pull request.
