Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> initial_height = float(input("Enter the initial height (in feet): "))
Enter the initial height (in feet): 7
>>> bounces = int(input("Enter the number of times the ball bounces: "))
Enter the number of times the ball bounces: 5
>>> BOUNCINESS = 0.6
... 
>>> total_distance = initial_height
>>> current_height = initial_height
>>> for _ in range(bounces):
...     bounce_height = current_height * BOUNCINESS
...      total_distance += bounce_height * 2
... current_height = bounce_height
SyntaxError: unexpected indent
>>> for _ in range(bounces):
...     bounce_height = current_height * BOUNCINESS
...      total_distance += bounce_height * 2
...      
SyntaxError: unexpected indent
>>> for _ in range(bounces):
...     bounce_height = current_height * BOUNCINESS
...     total_distance += bounce_height * 2
...     current_height = bounce_height
... 
...     
>>> print("Total distance traveled:", total_distance)
Total distance traveled: 26.367040000000003
