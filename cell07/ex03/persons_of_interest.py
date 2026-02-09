#!/usr/bin/env python3
def famous_births(persons_dict):
    # 1. เรียงลำดับข้อมูลใน dictionary ตามค่า 'date_of_birth'
    # dict.values() จะดึง dictionary ย่อยออกมา
    # sorted จะใช้ key เพื่อบอกว่าให้เรียงตามปีเกิด (แปลงเป็น int เพื่อความแม่นยำ)
    sorted_persons = sorted(persons_dict.values(), key=lambda x: int(x['date_of_birth']))

    # 2. วนลูปเพื่อแสดงผลตามรูปแบบที่โจทย์กำหนด
    for person in sorted_persons:
        name = person['name']
        birth = person['date_of_birth']
        print(f"{name} is a great scientist born in {birth}.")

# ส่วนการทดสอบตามตัวอย่างในโจทย์
if __name__ == "__main__":
    women_scientists = {
        "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
        "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
        "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
        "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
    }

    famous_births(women_scientists)
