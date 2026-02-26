Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> hourly_wage = float(input("Enter hourly wage: "))
Enter hourly wage: 25.00
>>> regular_hours = float(input("Enter total regular hours: "))
Enter total regular hours: 40
>>> overtime_hours = float(input("Enter total overtime hours: "))
Enter total overtime hours: 40.00
>>> regular_pay = hourly_wage * regular_hours
>>> overtime_pay = overtime_hours * (1.5 * hourly_wage)
>>> total_pay = regular_pay + overtime_pay
>>> print("Total weekly pay:", total_pay)
Total weekly pay: 2500.0
