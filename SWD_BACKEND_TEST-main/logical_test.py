# """
# Convert Number to Thai Text.
# เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลข เป็นตัวหนังสือภาษาไทย
# โดยที่ค่าที่รับต้องมีค่ามากกว่าหรือเท่ากับ 0 และน้อยกว่า 10 ล้าน

# *** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
# ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

# """
import math

def convertNumberToThai():
    print("Please inupt Number : ", end="")
    amount_number = input()
    amount_number = int(amount_number)
    number = ""
    number = amount_number

    result = ""
    result = readnumber(number)

    print(result)

def readnumber(number):
    number_position = ["แสน", "หมื่น", "พัน", "ร้อย", "สิบ", ""]
    thai_number = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]
    number = number
    result = ""
    pos = 0

    if (number == 0):
        return result
    if (number >= 1000000):
        result += readnumber(int(number / 1000000)) + "ล้าน"
        number = int(math.fmod(number, 1000000))
    divider = 100000

    while(number > 0):
        d = int(number/divider)
        if (divider == 10) and (d == 2):
            result += "ยี่"
        elif (divider == 10) and (d == 1):
            result += ""
        elif ((divider == 1) and (d == 1) and (result != "")):
            result += "เอ็ด"
        else:
            result += thai_number[d]
        if(d):
            result += number_position[pos]
        else:
            result += ""

        number = number % divider
        divider = divider / 10
        pos += 1
    
    return result

convertNumberToThai()

