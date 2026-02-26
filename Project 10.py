Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
purchase_price = float(input("Enter the purchase price: "))
Enter the purchase price: 60000
down_payment = purchase_price * 0.10
balance = purchase_price - down_payment
annual_rate = 0.12
monthly_rate = annual_rate / 12
monthly_payment = purchase_price * 0.05
print("\nTidBit Computer Store Payment Schedule")

TidBit Computer Store Payment Schedule
print("-" * 95)
-----------------------------------------------------------------------------------------------
>>> print(
...     f"{'Month':<6}"
...     f"{'Balance':>12}"
...     f"{'Interest':>12}"
...     f"{'Principal':>12}"
...     f"{'Payment':>12}"
...     f"{'Remaining':>14}"
... )
Month      Balance    Interest   Principal     Payment     Remaining
>>> print("-" * 95)
-----------------------------------------------------------------------------------------------
>>> month = 1
>>> while balance > 0:
...     interest = balance * monthly_rate
...     principal = monthly_payment - interest
... 
...     # Adjust final payment if it would overpay
...     if principal > balance:
...         principal = balance
...         monthly_payment = interest + principal
... 
...     remaining_balance = balance - principal
... 
...     print(
...         f"{month:<6}"
...         f"${balance:>11,.2f}"
...         f"${interest:>11,.2f}"
...         f"${principal:>11,.2f}"
...         f"${monthly_payment:>11,.2f}"
...         f"${remaining_balance:>13,.2f}"
...     )
... 
...     balance = remaining_balance
...     month += 1
... 
...     
1     $  54,000.00$     540.00$   2,460.00$   3,000.00$    51,540.00
2     $  51,540.00$     515.40$   2,484.60$   3,000.00$    49,055.40
3     $  49,055.40$     490.55$   2,509.45$   3,000.00$    46,545.95
4     $  46,545.95$     465.46$   2,534.54$   3,000.00$    44,011.41
5     $  44,011.41$     440.11$   2,559.89$   3,000.00$    41,451.53
6     $  41,451.53$     414.52$   2,585.48$   3,000.00$    38,866.04
7     $  38,866.04$     388.66$   2,611.34$   3,000.00$    36,254.70
8     $  36,254.70$     362.55$   2,637.45$   3,000.00$    33,617.25
9     $  33,617.25$     336.17$   2,663.83$   3,000.00$    30,953.42
10    $  30,953.42$     309.53$   2,690.47$   3,000.00$    28,262.96
11    $  28,262.96$     282.63$   2,717.37$   3,000.00$    25,545.59
12    $  25,545.59$     255.46$   2,744.54$   3,000.00$    22,801.04
13    $  22,801.04$     228.01$   2,771.99$   3,000.00$    20,029.05
14    $  20,029.05$     200.29$   2,799.71$   3,000.00$    17,229.34
15    $  17,229.34$     172.29$   2,827.71$   3,000.00$    14,401.64
16    $  14,401.64$     144.02$   2,855.98$   3,000.00$    11,545.65
17    $  11,545.65$     115.46$   2,884.54$   3,000.00$     8,661.11
18    $   8,661.11$      86.61$   2,913.39$   3,000.00$     5,747.72
19    $   5,747.72$      57.48$   2,942.52$   3,000.00$     2,805.20
20    $   2,805.20$      28.05$   2,805.20$   2,833.25$         0.00
