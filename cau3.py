A = [5, 3, 8, 3, 9, 1, 5, 7, 8, 2, 9, 4]
B = [6, 3, 2, 9, 5, 7, 5, 12, 8, 15, 7, 4]

D = set(A) & set(B)
D = list(D)

cungvitri = []
for i in range(len(A)):
    if A[i] == B[i]:
        cungvitri.append((i, A[i]))
C = []
soptu = {}
lon_nhat = 0
lon_nhi = 0
for i in A:
    if i in soptu:
        soptu[i] += 1
    else:
        soptu[i] = 1
        C.append(i)
    if lon_nhat < i:
        lon_nhat = i

for i in A:
    if i != lon_nhat and i > lon_nhi:
        lon_nhi = i

print("Danh sach C:", C)
print("Chung A va B:", D)
print("Cung vi tri:", cungvitri)
print(f"Lon nhat: {lon_nhat} ({soptu[lon_nhat]} lan) | Lon thu hai: {lon_nhi}")