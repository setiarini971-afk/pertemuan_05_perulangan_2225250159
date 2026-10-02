# Input: nilai ujian 0 sampai 100
# Proses: memeriksa apakah nilai berada dalam rentang yang valid
# Kondisi berhenti: nilai sudah berada antara 0 dan 100
# Output: nilai yang diterima

nilai = float(input("Nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

print(f"Nilai diterima: {nilai}")