ma_sv = "B26DCTV007"
x = 7
cc = 9
bt = 8
kt = 7.5
thi = 6.0
t = 7385 + x

def tg(i):
    giay = i % 60
    i = i // 60
    phut = i % 60
    i = i // 60
    gio = i
    print(f"Thoi gian: {gio} gio {phut} phut {giay} giay")

def diem_hp(x, y, z, t):
    diem = 0.1 * x + 0.1 * y + 0.2 * z + 0.6 * t
    return diem

def xep_loai(x):
    if x >= 8.0:
        print("Xep loai: Gioi")
    elif x >= 6.5:
        print("Xep loai: Kha")
    elif x >= 5.0:
        print("Xep loai: Trung binh")
    else:
        print("Xep loai: Yeu")

def diem_thi_toi_thieu_de_dat_8(x, y, z):
    diem = (8.0 - x * 0.1 - y * 0.1 - z * 0.2) / 0.6
    round(diem, 2)
    return diem

dhp = diem_hp(cc, bt, kt, thi)
dtt = diem_thi_toi_thieu_de_dat_8(cc, bt, kt)
tg(t)
print(f"Con thieu de du 3 gio: {10800 - t}")
print(f"Diem hoc phan: {dhp}")
xep_loai(dhp)
print(f"Diem thi toi thieu de dat 8.0: {dtt}")