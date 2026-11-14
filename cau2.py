def nto(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#tinh tong cac chu so cua so n
def tongchuso(n):
    tong = 0
    while n > 0:
        tong += n % 10 #lay so cuoi cung trong so n
        n //= 10 #loai bo so cuoi cung trong so n
    return tong
#vidu 23 -> chia du lay 3 -> phan nguyen con 2 -> chia du lay 2 -> tong ac chu so = 2 + 3

A = [23, 45, 17, 88, 101, 64, 37, 45, 59, 120, 73, 17, 91, 2]
so_nto = []
tongnto = {}
for i in A:
    if nto(i):
        so_nto.append(i)
    so = tongchuso(i) #Tong chu so cua so i
    if nto(so):
        tongnto[i] = so

print("a) So nguyen to trong A:")
print("  ",so_nto)
print("   Tong cac so nguyen to:", sum(so_nto))

print("b) Tong chu so la SNT:")
print("   ", end="")
nho = len(tongnto)
for key, value in tongnto.items():
    print(f"{key} ({value})", end="")
    #In ra dau phay neu con phan tu tiep theo
    if nho > 1:
        print(", ", end="")
        nho -= 1