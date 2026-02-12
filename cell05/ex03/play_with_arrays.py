#!/usr/bin/env python3

# 1. กำหนดอาร์เรย์ต้นฉบับตามโจทย์
original_array = [2, 8, 9, 48, 8, 22, -12, 2]
filtered_array = [x + 2 for x in original_array if x > 5]
unique_array = list(set(filtered_array))

# 4. แสดงผลลัพธ์ตามรูปแบบที่โจทย์กำหนด
print(original_array)
print(unique_array)
