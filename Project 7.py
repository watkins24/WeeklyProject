Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> start_salary = float(input("Enter the starting salary: "))
Enter the starting salary: 25
>>> increase_percent = float(input("Enter the annual percentage increase: "))
Enter the annual percentage increase: 5
>>> years = int(input("Enter the number of years: "))
... 
Enter the number of years: 10
>>> salary = start_salary
>>> increase_rate = increase_percent / 100
>>> print("\nYear\tSalary")

Year	Salary
>>> print("--------------------")
--------------------
>>> for year in range(1, years + 1):
...     print(f"{year}\t${salary:,.2f}")
...     salary += salary * increase_rate
... 
...     
1	$25.00
2	$26.25
3	$27.56
4	$28.94
5	$30.39
6	$31.91
7	$33.50
8	$35.18
9	$36.94
10	$38.78
