#!/usr/bin/env python3
def array_of_names(persons):
    # สร้างลิสต์ว่างเพื่อเก็บชื่อเต็ม
    full_names = []
    
    # วนลูปดึง key (ชื่อต้น) และ value (นามสกุล) จาก dictionary
    for first, last in persons.items():
        # ใช้ capitalize() เพื่อทำให้ตัวแรกเป็นตัวพิมพ์ใหญ่
        # แล้วนำมาต่อกันด้วยช่องว่าง
        formatted_name = f"{first.capitalize()} {last.capitalize()}"
        
        # เพิ่มชื่อที่จัดรูปแบบแล้วลงในลิสต์
        full_names.append(formatted_name)
    
    return full_names

if __name__ == "__main__":
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    print(array_of_names(persons))
