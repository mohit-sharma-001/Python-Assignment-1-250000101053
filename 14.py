# Question 14: Write a program to calculate simple interest using principal, rate and time.

principal = 10000.0  # Principal amount in INR
rate = 5.5           # Annual interest rate in %
time = 3.0           # Time period in years

simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest

print("Principal Amount:", principal)
print("Annual Interest Rate (%):", rate)
print("Time Period (years):", time)
print("Simple Interest:", simple_interest)
print("Total Amount:", total_amount)
