telebeler_kurslar = [
    ["Tarix", "Edebiyyat","Azerbaycan dili " ],
    ["ingilis dili", "Riyaziyyat", "Informatika"],
    ["Biologiya", "Fizika", "Kimya"]
]

# Butun kurslari bir set'e toplayaq
umumi_kurslar = set()

for kurs_siyahisi in telebeler_kurslar:
    umumi_kurslar.update(kurs_siyahisi)

print("Unikal kurslar:")
print(umumi_kurslar)