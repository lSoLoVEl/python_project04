#หาพิ้นที่สี่เหลี่ยม และสามเหลี่ยม โดยรับกว้าง ยาว/ฐาน ศูง ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ
#function การทำงานอะไรบ้าง
#1.รับค่า กว่างยาว 2.รับค่า ฐาน ศุง 3.คำนวณพื้นที่.สี่เหลี่ยม 4.คำนวณพื้นที่.สามเหลี่ยม
def inputWitdhLong( ) :
    wi = float( input('ป้อนกว้าง : '))
    lo = float( input('ป้อนยาว : '))
    return wi, lo

def inputBaseHigh( ) :
    ba = float( input('ป้อนฐาน : '))
    hi = float( input('ป้อนสูง : '))
    return ba, hi

def calAndShowAreaSquare(wi, lo ) :
    area = wi * lo
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {lo} มีพื้นที่ {area}')

def calAndShowAreaTrianble(ba, hi ) :
    area = ba * hi/2
    print(f'ฐานสามเหลี่ยม {ba} สูง {hi} มีพื้นที่ {area}')

wi, lo = inputWitdhLong( )
calAndShowAreaSquare(wi, lo)
print('------------------------------')
ba, hi = inputBaseHigh( )
calAndShowAreaTrianble(ba, hi)
