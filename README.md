# Financial-Interest-Calculator-Python
Is a program that allows the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

Investment and Bond Calculator
This Python script provides a simple tool to calculate the estimated amount you will earn on an investment or the monthly repayments for a bond. It offers both simple and compound interest calculations for investments and computes bond repayments based on the present value of the house, the interest rate, and the repayment period.

Features
Investment Calculation
Calculate future value using Simple Interest.
Calculate future value using Compound Interest.
Bond Repayment Calculation
Calculate monthly repayments based on the present value of the house, interest rate, and repayment period.
How to Use
Prerequisites
Python 3.x
math module (part of the standard Python library)
Running the Script
Clone the repository or download the script.
Open a terminal and navigate to the directory containing the script.
Run the script using the command:
bash
Copy code
python investment_bond_calculator.py
Menu Options
Investment: To calculate the amount of interest you'll earn.
Bond: To calculate the amount you'll have to pay on a home loan.
Example Usage
Investment Calculation

Enter the amount to deposit.
Enter the interest rate.
Enter the number of years.
Choose between simple or compound interest.
Bond Calculation

Enter the present value of the house.
Enter the interest rate.
Enter the number of months to repay the bond.
Sample Interaction
plaintext
Copy code
Choose either 'investment' or 'bond' from the menu below to proceed:

Investment    - to calculate the amount of interest you'll earn on interest
Bond          - to calculate the amount you'll have to pay on a home loan

Enter: investment
Enter amount to deposit: 1000
Enter interest rate: 5
Enter number of years: 10
Do you want simple or compound interest?: simple
=====================================================
Estimated amount :R1500.0
Type: simple interest
Number of Years: 10
Rate :5.0%
=====================================================

Do you want to continue? yes/no: no
=========================Good Bye!!!============================
