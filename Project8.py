Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def copy_file(source_name, destination_name):
...     try:
...         with open(source_name, 'r') as source_file:
...             contents = source_file.read()
... 
...         with open(destination_name, 'w') as destination_file:
...             destination_file.write(contents)
... 
...         print("File copied successfully.")
... 
...     except FileNotFoundError:
...         print("Error: The source file was not found.")
...     except IOError:
...         print("Error: An I/O error occurred.")
... 
...         
>>> if __name__ == "__main__":
...     source = input("Enter the name of the source text file: ")
...     destination = input("Enter the name of the destination text file: ")
... 
...     copy_file(source, destination)
... 
...     
Enter the name of the source text file: r
Enter the name of the destination text file: s
Error: The source file was not found.
