#!/usr/bin/env python3
def average(scores_dict):
    # ตรวจสอบว่า dictionary ว่างหรือไม่ เพื่อป้องกันการหารด้วยศูนย์
    if not scores_dict:
        return 0
    
    # ดึงค่าคะแนนทั้งหมด (values) ออกมา
    scores = scores_dict.values()
    
    # คำนวณค่าเฉลี่ย: ผลรวมคะแนนทั้งหมด หารด้วย จำนวนนักเรียน
    avg = sum(scores) / len(scores)
    
    return avg

# ส่วนการทดสอบตามตัวอย่างในโจทย์
if __name__ == "__main__":
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }

    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
