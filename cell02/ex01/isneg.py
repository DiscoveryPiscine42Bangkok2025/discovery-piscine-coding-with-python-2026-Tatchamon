#!/usr/bin/env python3

# รับค่าจากผู้ใช้และแปลงเป็นตัวเลข (float เพื่อรองรับทศนิยม)
try:
    number = float(input())

    # ตรวจสอบเงื่อนไขตามที่โจทย์กำหนด
    if number < 0:
        print("This number is negative.")
    elif number > 0:
        print("This number is positive.")
    else:
        print("This number is both positive and negative.")
except ValueError:
    # กรณีผู้ใช้ใส่ค่าที่ไม่ใช่ตัวเลข
    pass
#chmod +x ./cell02/ex01/isneg.py
#./cell02/ex01/isneg.py