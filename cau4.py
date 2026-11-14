ma_sv = "B26DCTV007"
ds = [
"    nguyEN   vaN    an ",
"tran THI    binh",
"   le   hoang NAM",
"pham   minh   duc ",
"    nguyen    THI an",
"  nguyen    THE    anh  "
]
#phan a)
def chuan_hoa_ten(ten):
    ten = " ".join(ten.split()) 
    #b1 chia chuoi thanh cac phan tu cach nhau bang " " vao trong list
    #b2 ket hop tat ca cac pt trong list vao chuoi cach nhau 1 dau " "
    ten = ten.title()
    return ten
#b)
def taikhoan(x):
    x = x.lower().split() 
    #bien tat ca chu thanh in thuong va chia thanh cac ptu trong list
    ten = x[-1] #lay ptu cuoi cung trong list
    dem = "".join(i[0] for i in x[:-1]) 
    #chay tu i trong list va lay i[0] (ky tu dau tien) va gop lai thanh chuoi ko cach nhau
    return ten + dem

ds_moi = []
for i in ds:
    ten = chuan_hoa_ten(i)
    ds_moi.append(ten)
print("a) Sau chuan hoa:")
print(ds_moi)

print("b) Tai khoan:")
max_len = max(len(i) for i in ds_moi) 
#tim do dai lon nhat cua cac ten trong ds_moi -> can le dau "->"
for i in ds_moi:
    tk = taikhoan(i)
    if i != ds_moi[-1]:
        print(f"{i:<{max_len}} -> {tk}")
    else:
        print(f"{i:<{max_len}} -> {tk}_{ma_sv.lower()}")
