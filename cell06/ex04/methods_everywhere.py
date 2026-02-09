#!/usr/bin/env python3
import sys

# ตัดให้เหลือ 8 ใช้ slices
def shrink(s):
    print(s[:8])

# เติมตัว 'Z' จนครบ 8 ตัว
def enlarge(s):
    while len(s) < 8:
        s += 'Z'
    print(s)

def main():
    # ตรวจสอบถ้าไม่มีเลยให้แสดง none
    args = sys.argv[1:]
    if len(args) < 1:
        print("none")
        return

    # วนลูปตามเงื่อนไข
    for arg in args:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()
