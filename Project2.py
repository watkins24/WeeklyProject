Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def caesar_decrypt(text, shift):
...     result = ""
...     
...     for char in text:
...         # Only shift printable ASCII characters
...         if 32 <= ord(char) <= 126:
...             # Normalize to 0–94 range
...             normalized = ord(char) - 32
...             shifted = (normalized - shift) % 95
...             result += chr(shifted + 32)
...         else:
...             # Leave non-printable characters unchanged
...             result += char
... 
...     return result
... 
>>> if __name__ == "__main__":
...     encrypted_text = input("Enter encrypted text: ")
...     distance = int(input("Enter distance value: "))
...     
...     plaintext = caesar_decrypt(encrypted_text, distance)
...     print("Decrypted text:", plaintext)
... 
...     
Enter encrypted text: lynzee
Enter distance value: 6
Decrypted text: fsht__
