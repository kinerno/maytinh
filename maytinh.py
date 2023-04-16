import math;
import random;
print("1 : toan hoc")
print("2 : hoa hoc")
print("3 : tinh diem trung binh mon")
print("4 : random so may man")
st = int(input("===> "))
if st == 1:
  print("1 : giai phuong trinh bac 2")
  th = int(input("===> "))
  if th == 1:
    a = int(input("nhap he so a : "))
    b = int(input("nhap he so b : "))
    c = int(input("nhap he so c : "))
    x = b*b-4*a*c
    print('co denta bang :',x)
    if x < 0:
      print('=> vo nghiem')
    elif x == 0:
       print('=> nghiem kep')
    elif x > 0:
       print('=> hai nghiem phan biet')
    if x > 0:
      ww = math.sqrt(x)
      v = -b+ww
      z = 2*a
      l = v/z
      q = -b-ww
      p = q/z
      print("x1 =",l," x2 =",p)
    if x == 0:
       xz = -b/2*a
       print ("x1 = x2 = ", xz)
       
if st == 2:
    print("1 : tinh so mol (g)")
    print("2 : tinh so mol (khi)")
    hh = int(input("===>"))
    if hh == 1:
        kl = float(input("khoi luong chat :"))
        nk = int(input("nguyen tu khoi :"))
        mol = kl/nk
        print("so mol cua chat la :",mol)
    if hh == 2:
        tt = float(input("the tich khi (lit) : "))
        mok = tt/22.4
        print("so mol cua chat la :",mok)

if st == 3:
    print(" ban co bao nhieu diem thuong xuyen")
    di1 = int(input("3 hoac 4 : "))
    if di1 == 3:
        print("diem thuong xuyen")
        dz1 = float(input("diem so 1 :"))
        dz2 = float(input("diem so 2 :"))
        dz3 = float(input("diem so 3 :"))
        print("diem giua ky")
        gk = float(input("diem :"))
        print("diem cuoi ky")
        ck = float(input("diem :"))
        tk = dz1+dz2+dz3+gk*2+ck*2
        tk1 = tk/7
        print("diem tong cua ban la :",tk1)
        
    if di1 == 4:
        print("diem thuong xuyen")
        dz1 = float(input("diem so 1 :"))
        dz2 = float(input("diem so 2 :"))
        dz3 = float(input("diem so 3 :"))
        dz4 = float(input("diem so 4 :"))
        print("diem giua ky")
        gk = float(input("diem :"))
        print("diem cuoi ky")
        ck = float(input("diem :"))
        tk = dz4+dz1+dz2+dz3+gk*2+ck*2
        tk1 = tk/8
        print("diem tong cua ban la :",tk1)
if st == 4:
  a = random.randint(1, 6)
  b = random.randint(1, 6)
  c = random.randint(1, 6)
  smm = a+b+c
  if smm < 11:
      print("XIU")
      print(smm)
  elif smm > 10:
      print('TAI')
      print(smm)

exit(0)

