#!/usr/bin/env python3
import math

# 1. รับค่าตัวเลขจากผู้ใช้
try:
    user_input = input("Give me a number: ")
    number = float(user_input)
    result = math.ceil(number)
    print(result)

except ValueError:
    pass

#chmod +x ./cell04/ex04/round_up.py
#./cell04/ex04/round_up.py