ma_sv = "B26DCTV007"
ds = [
"    nguyEN   vaN    an ",
"tran THI    binh",
"   le   hoang NAM",
"pham   minh   duc ",
"    nguyen    THI an",
"  nguyen    THE    anh  "
]

def chuan_hoa_ten(ten):
    ten = " ".join(ten.split())
    ten = ten.title()
    return ten

def taikhoan(x):
    x = x.lower().split()
    ten = x[-1]
    dem = "".join(i[0] for i in x[:-1])
    return ten + dem

ds_moi = []
for i in ds:
    ten = chuan_hoa_ten(i)
    ds_moi.append(ten)
print("a) Sau chuan hoa:")
print(ds_moi)

print("b) Tai khoan:")
max_len = max(len(i) for i in ds_moi)
for i in ds_moi:
    tk = taikhoan(i)
    if i != ds_moi[-1]:
        print(f"{i:<{max_len}} -> {tk}")
    else:
        print(f"{i:<{max_len}} -> {tk}_{ma_sv.lower()}")
