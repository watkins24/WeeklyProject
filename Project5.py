Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> initial_population = float(input("Enter the initial number of organisms: "))
Enter the initial number of organisms: 500
>>> growth_rate = float(input("Enter the growth rate (greater than 0): "))
Enter the growth rate (greater than 0): 2
>>> hours_per_period = float(input("Enter the number of hours to achieve this growth rate: "))
Enter the number of hours to achieve this growth rate: 6
>>> total_hours = float(input("Enter the total number of hours of growth: "))
Enter the total number of hours of growth: 12
>>> growth_periods = total_hours / hours_per_period
>>> final_population = initial_population * (growth_rate ** growth_periods)
>>> print("Predicted population:", final_population)
Predicted population: 2000.0
