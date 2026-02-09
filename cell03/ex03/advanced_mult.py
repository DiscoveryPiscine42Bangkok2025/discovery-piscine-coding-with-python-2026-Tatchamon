#!/usr/bin/env python3
import sys

def main():
    # ตรวจสอบว่ามีการใส่ argument มาหรือไม่ (sys.argv[0] คือชื่อไฟล์)
    # หากมี argument เพิ่มเติม (len > 1) ให้พิมพ์ none และจบการทำงาน
    if len(sys.argv) > 1:
        print("none")
        return

    # เริ่มต้น loop ที่ 1 สำหรับ "แม่สูตรคูณ" (Table de 0 ถึง 10)
    i = 0
    while i <= 10:
        print(f"Table de {i}:", end="")
        
        # เริ่มต้น loop ที่ 2 สำหรับ "ตัวคูณ" (0 ถึง 10)
        j = 0
        while j <= 10:
            # คำนวณผลคูณและแสดงผลโดยใช้ช่องว่างคั่น (end=" ")
            print(f" {i * j}", end="")
            j += 1
            
        # ขึ้นบรรทัดใหม่เมื่อจบรอบของแต่ละแม่
        print()
        i += 1

if __name__ == "__main__":
    main()

#chmod +x ./cell03/ex03/advanced_mult.py
#./cell03/ex03/advanced_mult.py