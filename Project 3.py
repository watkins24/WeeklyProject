Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import math
>>> print("Think of a number, and I will try to guess it!")
Think of a number, and I will try to guess it!
>>> lower = int(input("Enter the lower bound: "))
Enter the lower bound: 0
>>> upper = int(input("Enter the upper bound: "))
Enter the upper bound: 100
>>> max_guesses = math.ceil(math.log2(upper - lower + 1))
>>> print(f"I can guess your number in at most {max_guesses} guesses.")
I can guess your number in at most 7 guesses.
>>> guesses = 0
>>> while lower <= upper:
...     guess = (lower + upper) // 2
...     guesses += 1
... 
...     print(f"My guess is {guess}")
...     hint = input(
...         "Enter 'h' if your number is higher, "
...         "'l' if it is lower, or 'c' if correct: "
...     ).lower()
... 
...     if hint == 'c':
...         print(f"I guessed your number in {guesses} guesses!")
...         break
...     elif hint == 'h':
...         lower = guess + 1
...     elif hint == 'l':
...         upper = guess - 1
...     else:
...         print("Invalid input. Please enter h, l, or c.")
...         guesses -= 1
...         continue
... 
...     
My guess is 50
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: h
My guess is 75
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: l
My guess is 62
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: h
My guess is 68
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: h
My guess is 71
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: h
My guess is 73
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: l
My guess is 72
Enter 'h' if your number is higher, 'l' if it is lower, or 'c' if correct: c
I guessed your number in 7 guesses!
