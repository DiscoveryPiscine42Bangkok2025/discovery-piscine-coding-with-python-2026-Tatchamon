#!/usr/bin/env python3
import sys

def main():
    #ตรวจสอบจำนวนพารามิเตอร์ (sys.argv[0] คือชื่อไฟล์ ดังนั้นต้องมีรวมเป็น 3)
    if len(sys.argv) != 3:
        print("none")
        return

    keyword = sys.argv[1]
    search_string = sys.argv[2]

    # 2. นับจำนวนครั้งที่ keyword ปรากฏใน search_string
    count = search_string.count(keyword)

    # 3. ตรวจสอบว่ามีคำนั้นปรากฏหรือไม่ (ถ้าไม่มี หรือ count เป็น 0 ให้พิมพ์ none)
    if count == 0:
        print("none")
    else:
        print(count)

if __name__ == "__main__":
    main()

#chmod +x ./cell05/ex9/scan_it.py
