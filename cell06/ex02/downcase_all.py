#!/usr/bin/env python3
import sys

def downcase_it(text):
    return text.lower()

def main():
    # ตรวจสอบพารามิเตอร์ของโปรแกรม (sys.argv[0] คือชื่อไฟล์)
    if len(sys.argv) < 2:
        print("none")
        return

    # นำเมธอดไปใช้กับทุกพารามิเตอร์ที่รับมา (เริ่มที่ตัวที่ 1 เป็นต้นไป)
    for arg in sys.argv[1:]:
        print(downcase_it(arg))

if __name__ == "__main__":
    main()
