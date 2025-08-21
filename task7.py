import json
import os 


class Istifadeci:
    def __init__(self, ad, yas, email, telefon):
        self.ad = ad
        self.yas = yas
        self.email = email
        self.telefon = telefon

    def melumat_olaraq(self):
        return {
            "ad": self.ad,
            "yas": self.yas,
            "email": self.email,
            "telefon": self.telefon
        } 

    def __str__(self):
        return f"İstifadəçi: {self.ad}, Yaş: {self.yas}, Email: {self.email}, Telefon: {self.telefon}"
  


class IstifadeciMeneceri:
    def __init__(self, fayl_adi="users.txt"):
        self.fayl_adi = fayl_adi
        self.istifadeciler = self._istifadecileri_yukle()

    def _istifadecileri_yukle(self):
        if not os.path.exists(self.fayl_adi):
            return []
        with open(self.fayl_adi, "r") as fayl:
            return [Istifadeci(**json.loads(line)) for line in fayl]

    def _istifadecileri_yaz(self):
        with open(self.fayl_adi, "w") as fayl:
            for istifadeci in self.istifadeciler:
                fayl.write(json.dumps(istifadeci.melumat_olaraq()) + "\n")

    def istifadeci_elave_et(self, istifadeci):
        self.istifadeciler.append(istifadeci)
        self._istifadecileri_yaz()

    def yeni_istifadeci_elave_et(self):
        print("\nYeni istifadeci melumatlari:")
        ad = input("Ad: ")
        yas = input("Yaş: ")
        email = input("Email: ")
        telefon = input("Telefon: ")  

        istifadeci = Istifadeci(ad, yas, email, telefon)
        self.istifadeci_elave_et(istifadeci)

    def butun_istifadecileri_goster(self):
        print("\nSistemdəki istifadəçilər:")
        if not self.istifadeciler:
             print("Heç bir istifadəçi mövcud deyil.")
             return
        
        for idx, istifadeci in enumerate(self.istifadeciler, start=1):
            print(f"{idx}. {istifadeci}")
            
# ============ istifadeci ==============

def menyu_goster():
    print("\n--- Menyu ---")
    print("1. Yeni istifadəçi əlavə et")
    print("2. Bütün istifadəçiləri göstər")
    print("3. Çıxış")

def proqrami_baslat():
    menecer = IstifadeciMeneceri()
    while True:
        menyu_goster()
        secim = input("Seçiminizi edin: ")
        if secim == "1":
            menecer.yeni_istifadeci_elave_et()
        elif secim == "2":
            menecer.butun_istifadecileri_goster()
        elif secim == "3":
            print("Proqramdan çıxılır...")
            break
        else:
            print("Yanlış seçim, zəhmət olmasa yenidən cəhd edin.")
               

if __name__ == "__main__":
    proqrami_baslat()
