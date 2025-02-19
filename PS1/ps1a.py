from utils import ask_for_float_input


annual_salary = ask_for_float_input("Enter your annual salary: ")
portion_saved = ask_for_float_input(
    "Enter the percent of your salary to save, as a decimal: "
)
total_cost = ask_for_float_input("Enter the cost of your dream home: ")

portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
annual_return = 0.04
monthly_salary_savings = (annual_salary * portion_saved) / 12

num_of_months = 0

while current_savings < total_down_payment:
    monthly_investment_return_savings = (current_savings * annual_return) / 12

    current_savings += monthly_salary_savings
    current_savings += monthly_investment_return_savings
    num_of_months += 1

print(f"Number of months: {num_of_months}")
