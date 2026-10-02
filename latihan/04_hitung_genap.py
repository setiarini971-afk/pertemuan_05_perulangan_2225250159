# Input: bilangan positif n
# Proses: memeriksa bilangan 1 sampai n dan menghitung yang genap
# Kondisi berhenti: for selesai sampai n
# Output: banyak bilangan genap

n = int(input("n: "))

jumlah_genap = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

print(f"Banyak bilangan genap = {jumlah_genap}")