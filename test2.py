#Function 2 : have parameter/have Return
#parameter คือตัวแปรประเภทหนึ่งที่รอรับข้อมูล ขอบเขตการใช้งานจะใช้ได้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น

def funcA( x, y ) :
    print('konijiva')
    z =  x + y 
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่งreturn

def funcB( x ) :
    print(f"x is {x} 555...")

funcA(10, 20)  #argument คือจำนวนข้อมูลที่ส่งให้parameter
funcA(5, 5)
funcB('Sau IoT')