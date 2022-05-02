# md5

import hashlib
str = input("Enter the input: ")
result = hashlib.md5(str.encode())

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of hash is : ", end="")
print(result.hexdigest())

# SHA-1

str = input("Enter the input: ")
result = hashlib.sha1(str.encode())

# printing the equivalent byte value.
print("The byte equivalent of hash is : ", end="")
print(result.digest())

# printing the equivalent hexadecimal value.
print("The hexadecimal equivalent of SHA1 is : ")
print(result.hexdigest())
