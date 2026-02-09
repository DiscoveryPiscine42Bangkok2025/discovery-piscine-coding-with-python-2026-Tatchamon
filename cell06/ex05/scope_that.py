def add_one(number):
    # คืนค่าผลลัพธ์กลับไปให้ผู้เรียก
    return number + 1

if __name__ == "__main__":
    my_var = int(input("Enter a number: "))
    print(f"ก่อน: {my_var}")
    
    # รับค่าที่ return กลับมา แล้วนำไปเก็บไว้ใน my_var ตัวเดิม
    my_var = add_one(my_var)
    
    print(f"หลัง: {my_var}")  # รอบนี้ค่าจะเปลี่ยนเป็น 43

