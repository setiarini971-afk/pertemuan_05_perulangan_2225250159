# Input: suku pertama a, beda d, dan banyak suku n
# Proses: memvalidasi n, menghasilkan suku dengan for,
#         dan menjumlahkan seluruh suku
# Kondisi berhenti: n harus lebih dari 0 dan for berjalan n kali
# Output: setiap suku dan jumlah seluruh suku

print("Deret Aritmetika")

a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

total = 0

for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

print(f"Jumlah = {total:.2f}")