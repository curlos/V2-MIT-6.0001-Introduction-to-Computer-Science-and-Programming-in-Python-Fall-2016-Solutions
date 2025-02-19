def ask_for_float_input(prompt):
    while True:
        try:
            float_val = float(input(prompt).strip())
            return float_val
        except ValueError:
            pass


annual_salary = ask_for_float_input("Enter your annual salary: ")
portion_saved = ask_for_float_input(
    "Enter the percent of your salary to save, as a decimal: "
)
total_cost = ask_for_float_input("Enter the cost of your dream home: ")
semi_annual_raise = ask_for_float_input("Enter the semi-annual raise, as a decimal: ")

portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
annual_return = 0.04

num_of_months = 0

while current_savings < total_down_payment:
    if num_of_months != 0 and num_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

    monthly_salary_savings = (annual_salary * portion_saved) / 12
    monthly_investment_return_savings = (current_savings * annual_return) / 12

    current_savings += monthly_salary_savings
    current_savings += monthly_investment_return_savings
    num_of_months += 1

print(f"Number of months: {num_of_months}")
