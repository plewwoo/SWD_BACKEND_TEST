
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def convertArabicToRoman():
    print("Please inupt Arabic number : ", end="")
    number = input()
    number = int(number)
    arabic = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    roman = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
    result = ""
    i = 12
    if number > 0 and number < 1001:
        while number:
            output = number // arabic[i]
            number %= arabic[i]
    
            while output:
                result += roman[i]
                output -= 1
            i -= 1

        print(result)
    else:
        print("Number must be greater than 1 and less or equal than 1000")
 

convertArabicToRoman()