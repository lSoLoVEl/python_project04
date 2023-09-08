#Function 3 No parameter/have Returns ***
def funcA( ) :
    print('AAA')
    print('BBB')
    return 'Wow Wow Wow'

def funcB( ) :
    return 999, True, 10+20  

funcA( ) #เขียนได้แต่เขาไม่ทำกัน
print( funcA( ) )
x = funcA( )

a, b, c = funcB( ) #ให้สร้างตัวแปรมาเก็บค่าที่ส่งกลับก่อน
print(f'{a} {b} {c}')