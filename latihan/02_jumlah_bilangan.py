# Input: bilangan bulat positif n
# Proses: menjumlahkan bilangan 1 sampai n menggunakan for
# Kondisi berhenti: range berhenti pada n
# Output: jumlah bilangan 1 sampai n

n = int(input("n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"Jumlah = {total}")