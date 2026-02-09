#!/usr/bin/env python3
def find_the_redheads(family_dict):
    # ใช้ filter เพื่อเลือกเฉพาะ key (ชื่อ) ที่มี value (สีผม) เป็น "red"
    # filter(ฟังก์ชันเงื่อนไข, ข้อมูลที่จะกรอง)
    redheads = filter(lambda name: family_dict[name] == "red", family_dict)
    
    # แปลงผลลัพธ์จาก filter object ให้เป็น list ก่อน return
    return list(redheads)

if __name__ == "__main__":
    # ข้อมูลทดสอบตามโจทย์
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    # เรียกใช้ฟังก์ชันและแสดงผล
    print(find_the_redheads(dupont_family))
