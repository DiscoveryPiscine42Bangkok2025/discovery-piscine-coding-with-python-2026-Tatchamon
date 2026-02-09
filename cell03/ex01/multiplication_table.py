#!/usr/bin/env python3

try:
    print("Enter a number")
    number = int(input())
    for i in range(10):
        result = i * number
        # แสดงผลตามรูปแบบ: i x number = result
        print(f"{i} x {number} = {result}")

except ValueError:
    # กรณีไม่ใช่ตัวเลข
    pass

#chmod +x ./cell03/ex01/multiplication_table.py
#./cell03/ex01/multiplication_table.py