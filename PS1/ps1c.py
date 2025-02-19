from utils import ask_for_float_input


semi_annual_raise = 0.07
investments_annual_return = 0.04
down_payment_percent = 0.25
total_cost_of_house = 1000000
total_down_payment = total_cost_of_house * down_payment_percent
monthly_total_down_payment = total_down_payment / 36
starting_salary = ask_for_float_input("Enter the starting salary: ")


def calculate_savings_after_36_months(savings_percent, starting_salary):
    """
    Calculate the total savings after 36 months using the savings percent and starting salary. This will take into account that the user will receive a raise every 6 months and that their savings nets them an annual return of 0.04% which will be added to the total savings.
    """

    current_savings = 0
    annual_salary = starting_salary

    # For 36 months, go through each month and add to the total savings using the monthly salary * savings percent and the monthly investment return.
    for month in range(0, 36):
        # If 6 months have passed since the last raise, give the user another a raise of 0.07% of their current annual salary.
        if month != 0 and month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

        monthly_salary = annual_salary / 12

        monthly_salary_savings = monthly_salary * savings_percent
        monthly_investment_return_savings = (
            current_savings * investments_annual_return
        ) / 12

        current_savings += monthly_salary_savings
        current_savings += monthly_investment_return_savings

    return current_savings


def get_best_savings_rate_binary_search():
    """
    Get the closest possible savings rate that will let the user pay off the down payment at the specified timeframe by testing out different savings rate. If the savings are too high, then decrease the savings rate. If the savings are too low, then increase the savings rate. And, if the savings are within $100 (less or more), than it is approximately close enough and that is the best savings rate.
    """
    steps_bisection_search = 0

    low = 0
    high = 1

    savings = calculate_savings_after_36_months(1, starting_salary)

    # If saving 100% of their salary is less than the required total down payment, then they cannot pay it in 3 years.
    if savings < total_down_payment:
        return -1

    while low < high:
        steps_bisection_search += 1

        mid_savings_percent = low + ((high - low) / 2)
        savings = calculate_savings_after_36_months(
            mid_savings_percent, starting_salary
        )

        low_total = total_down_payment - 100
        high_total = total_down_payment + 100

        savings_within_100 = (savings == total_down_payment) or (
            savings >= low_total and savings <= high_total
        )

        if savings_within_100:
            return {
                "best_savings_rate": mid_savings_percent,
                "steps_bisection_search": steps_bisection_search,
            }
        elif savings < total_down_payment:
            low = mid_savings_percent
        elif savings > total_down_payment:
            high = mid_savings_percent

    return -1


result = get_best_savings_rate_binary_search()

if result == -1:
    print("It is not possible to pay the down payment in three years.")
else:
    print(f"Best savings rate: {round(result["best_savings_rate"], 4)}")
    print(f"Steps in bisection search: {result["steps_bisection_search"]}")
