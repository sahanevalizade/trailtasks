class BankHesabi:
    bank_adi = "AzerBank"
    hesab_saygaci = 1000


     def __init__(self, sahib, balans=0):
        self.sahib = sahib 
        self.balans = balans
        BankHesabi.hesabi_saygaci += 1
        self.hesab_nomresi = BankHesabi.hesabi_saygaci


    def pul_yatir(self, mebleg):
        if mebleg > 0:
            self.balans +=mebleg
            return f"{mebleg} AZN yatirildi. Yeni balans: {self.balans} AZN"
        return "Mebleg duzgun deyil!"


    def  pul__cixar(self, mebleg):
        if mebleg <= self.balans:
            self.balans -= mebleg
            return f"{mebleg} AZN cixarildi. Yeni balans: {self.balans} AZN"   

      return "Balans kifayet etmir!"


    def __str__(self):
        return f"{self.sahib} hesabi ({self.bank_adi}): {self.balans} AZN (№{self.hesab_nomresi})" 

    def __repr__(self):
        return f"BankHesabi(sahib='{self.sahib}', balans={self.balans})"
        

    @classmethod
    def bank_adini_deyis(cls, yeni_ad):
        cls.bank_adi = yeni_ad
        return f"Bankin adi deyisdirildi: {cls.bank_adi}"
    
    @staticmethod
    def bank_qaydalari():
        return "Minimun balans 10 azn olmalidir. Kredit yalniz 18 yasdan yuxari sexslere verili."

# Istifade 
hesab1 = BankHesabi("Ruhiyyə", 200)
hesab2 = BankHesabi("Elvin")
print(hesab1)
print(hesab1.pul_yatir(100))
print(hesab1.pul__cixar(50))
print(hesab2)
print(BankHesabi.bank_qaydalari())
print(BankHesabi.bank_adini_deyis("MilliBank"))
print(hesab2)