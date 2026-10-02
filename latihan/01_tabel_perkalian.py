# Input: satu bilangan bulat n
# Proses: mengalikan n dengan 1 sampai 10 menggunakan for
# Kondisi berhenti: range berhenti sebelum 11
# Output: tabel perkalian n dari 1 sampai 10

n = int(input("Bilangan: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")