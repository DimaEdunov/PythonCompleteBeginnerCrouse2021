# Integer and float practice

gross_payckeck = 10000
health_insurance = 430.99
rent = 1200
food = 400.5

tax = 0.2 #In %

donation_for_the_poor = 0.1 #In %

# Calculate net salary
tax_amount_in_money = gross_payckeck * tax
net_salary = gross_payckeck - tax_amount_in_money - health_insurance - rent - food
print("Net salary : " +str(net_salary))

# Donation to poor, taken from net salary
donation_amount = net_salary * donation_for_the_poor
print("Donation amount in $ : " +str(donation_amount))