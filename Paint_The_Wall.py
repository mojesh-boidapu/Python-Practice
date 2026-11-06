import math
litre_cover=0
def paint_wall(height,width,cover):
    area=height*width
    litres=area/cover
    no_of_litres=math.ceil(area/cover)
    #print(litres)
    print(f"You will need {no_of_litres} liters of paint")
    remain=(no_of_litres-litres)*(10**3)
    remain_litres=round(remain,2)
    print(f"Wall area: {area:.2f} square meters")
    print(f"Coverage used: {litre_cover} square meters per litre")
    print(f"You will need {no_of_litres} litre(s) of paint.")
    if remain_litres>0:
        print(f"Approximate leftover paint: {remain_litres} ml")
h=float(input('Enter the height of the wall in meters:'))
w=float(input('Enter the width of the wall in meters:'))
layers=int(input("If you want single coat paint enter '1' ,if you want double coat paint enter '2' :"))
if layers==1:
    litre_cover=15
    print(f"So,1 litre of paint covers 15 square meters")
    paint_wall(height=h, width=w, cover=litre_cover)
elif layers==2:
    litre_cover=7
    print(f"So,1 litre of paint covers 7 square meters")
    paint_wall(height=h,width=w,cover=litre_cover)
