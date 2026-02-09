#!/usr/bin/env python3

print("Enter a number less than 25")
try:
    number = int(input())

    if number > 25:
        print("Error")
    else:
        for i in range(number, 26):
            print(f"Inside the loop, my variable is {i}")

except ValueError:
    pass

#chmod +x ./cell03/ex00/to25.py
#./cell03/ex00/to25.py