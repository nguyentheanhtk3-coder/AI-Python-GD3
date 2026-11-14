sach = [
{"code": "B01", "name": "Lap trinh Python",
"author": "Nguyen Van A",
"so_luong": 12, "don_gia": 85000},
{"code": "B02", "name": "Cau truc du lieu",
"author": "Tran Van B",
"so_luong": 0, "don_gia": 110000},
{"code": "B03", "name": "De Men phieu luu ky",
"author": "To Hoai",
"so_luong": 5, "don_gia": 60000},
{"code": "B04", "name": "Hoc may co ban",
"author": "Nguyen Van A",
"so_luong": 8, "don_gia": 150000},
{"code": "B05", "name": "Vo chong A Phu",
"author": "To Hoai",
"so_luong": 0, "don_gia": 55000},
{"code": "B02", "name": "Dac nhan tam",
"author": "Dale Carnegie",
"so_luong": 20, "don_gia": 90000},
{"code": "B07", "name": "Python nang cao",
"author": "Nguyen Van A",
"so_luong": 4, "don_gia": 130000},
]

def thong_ke(sach):
    ma_so = sach["code"]
    ten_sach = sach["name"]
    so_luong = sach["so_luong"]
    don_gia = sach["don_gia"]
    return ma_so, ten_sach, so_luong, don_gia

def gia_tri_ton_kho(sach):
    tong = 0
    for s in sach:
        tong += s["so_luong"] * s["don_gia"]
    return tong

def sach_het_hang(sach):
    ds_het_hang = []
    for s in sach:
        if s["so_luong"] == 0:
            ds_het_hang.append(s["name"])
    return ds_het_hang

def sach_sap_het_hang(sach):
    ds_sap_het_hang = []
    for s in sach:
        if 0 < s["so_luong"] < 10:
            ds_sap_het_hang.append(s["name"])
    return ds_sap_het_hang

tong_gia_tri = gia_tri_ton_kho(sach)

print("Danh sach sach:")
for s in sach:
    ma_so, ten_sach, so_luong, don_gia = thong_ke(s)
    print(f"{ma_so} {ten_sach}: {don_gia}")
print("")

print("a) Tong gia tri ton kho:", tong_gia_tri)
print("")

print("- Het hang (so_luong = 0):")
print(" ", sach_het_hang(sach))
print("")

print("- Sap het hang (0 < so_luong < 10):")
print(" ", sach_sap_het_hang(sach))
print("")

def tac_gia(sach):
    ds_tac_gia = {}
    for s in sach:
        if s["author"] in ds_tac_gia:
            ds_tac_gia[s["author"]] += 1
        else:
            ds_tac_gia[s["author"]] = 1
    return ds_tac_gia

def so_sach_cua_tac_gia(sach, tac_gia):
    tac_pham = []
    for s in sach:
        if s["author"] == tac_gia:
            tac_pham.append(s["name"])
    return tac_pham

def code(sach):
    ds_code = {}
    for s in sach:
        if s["code"] in ds_code:
            ds_code[s["code"]] += 1
        else:
            ds_code[s["code"]] = 1
    return ds_code

print("b) Tac gia >= 2 cuon:")
ds_tac_gia = tac_gia(sach)
for tg in ds_tac_gia:
    if ds_tac_gia[tg] >= 2:
        tac_pham = so_sach_cua_tac_gia(sach, tg)
        print(f"- {tg}: \n  {tac_pham}")
print("")

print("Trung ma sach: ", end="")
ds_code = code(sach)
code_trung = []
if any(x > 1 for x in ds_code.values()): 
    #bat ky dk thoan man xay ra trong vong lap gia tri cua ds_code
    print("YES -> ", end="")
    for x in ds_code:
        if ds_code[x] > 1:
            code_trung.append(x)
    print(code_trung)
else:
    print("NO")