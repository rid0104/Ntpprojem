class Kullanici:
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre):
        self.kullaniciad = kullaniciad
        self.kullanicisoyad = kullanicisoyad
        self.email = email
        self.sifre = sifre
        self.giris_yapildi = False
        self.arkadaslar = []

    def kisiselbilgi(self):
        return f'{self.kullaniciad} {self.kullanicisoyad} {self.email} {self.sifre}'

    def uyegiris(self):
        while True:
            kulad = input("Adınız: ")
            sifre = int(input("Şifreniz: "))

            if kulad == self.kullaniciad and sifre == self.sifre:
                print("Kullanıcı adınız ve şifreniz doğru. Giriş yapıldı.")
                self.giris_yapildi = True
                break
            elif kulad == self.kullaniciad:
                print("Yanlış şifre girdiniz. Tekrar deneyiniz.")
            elif sifre == self.sifre:
                print("Yanlış kullanıcı adı girdiniz. Tekrar deneyiniz.")
            else:
                print("Yanlış kullanıcı adı ve şifre. Tekrar deneyiniz.")

    def uyecikis(self):
        if not self.giris_yapildi:
            print("Önce giriş yapmalısınız.")
            self.uyegiris()
            return
        input("Çıkış yapmak için enter tuşuna basınız: ")
        self.giris_yapildi = False
        print("Çıkış yapıldı.")

    def arkadas_ekle(self, arkadas):
        if arkadas not in self.arkadaslar:
            self.arkadaslar.append(arkadas)
            print(f"{arkadas.kullaniciad} {arkadas.kullanicisoyad} arkadaş listesine eklendi.")
        else:
            print(f"{arkadas.kullaniciad} {arkadas.kullanicisoyad} zaten arkadaş listesinde.")

    def ortak_arkadas(self, diger_kullanici):
        ortaklar = [arkadas for arkadas in self.arkadaslar if arkadas in diger_kullanici.arkadaslar]
        return ortaklar


class StandartKullanici(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre, bio, dil):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)
        self.bio = bio
        self.takipedilenler = []
        self.dil = dil

    def dilseçimi(self, istenilendil):
        self.dil = istenilendil
        print(f"Diliniz {self.dil} olarak değiştirildi.")

    def takipet(self, kisi):
        self.takipedilenler.append(kisi)
        print(f"Takip edilenler: {self.takipedilenler}")

    def takibibirak(self, kisi):
        if kisi in self.takipedilenler:
            self.takipedilenler.remove(kisi)
            print(f"{kisi} takip listesinden çıkarıldı.")
        else:
            print(f"{kisi} zaten takip edilmiyor.")

    def biodegis(self, yeni_bio):
        self.bio = yeni_bio
        print(f"Yeni biyo: {self.bio}")


class Paylas(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)
        self.postsayisi = 0
        self.storysayisi = 0

    def postat(self, miktar):
        self.postsayisi += miktar
        print(f"{miktar} yeni post paylaşıldı. Toplam post sayınız: {self.postsayisi}")

    def storyat(self, miktar):
        self.storysayisi += miktar
        print(f"{miktar} yeni story paylaşıldı. Toplam story sayınız: {self.storysayisi}")


class Güvenlik(Kullanici):
    def sifrekontrol(self):
        hak = 3
        while hak > 0:
            girilen_sifre = int(input("Şifrenizi giriniz: "))
            if self.sifre == girilen_sifre:
                print("Doğru şifre, giriş başarılı.")
                return
            else:
                hak -= 1
                print(f"Yanlış şifre. Kalan hak: {hak}")
        print("Hesabınız bloke edildi. Lütfen şifrenizi sıfırlayın.")

    def sifredegistir(self, mevcut_sifre, yeni_sifre):
        if self.sifre == mevcut_sifre:
            self.sifre = yeni_sifre
            print(f"Yeni şifreniz başarıyla değiştirildi: {self.sifre}")
        else:
            print("Mevcut şifreniz hatalı.")


class Premium(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre, tanınmış):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)
        self.tanınmış = tanınmış  

    def premium(self):
        if self.tanınmış is True:  
            print(f"Yeni ismi {self.kullaniciad} ","\u2705"," olarak değiştirildi.")
        else:
            print("Belli bir takipçiye ulaşmadığı için işareti alamadı.")



class Grup(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)
        self.grup = []

    def grupkur(self):
        kisi_sayisi = int(input("Grubunuza kaç kişi eklemek istiyorsunuz? "))
        for _ in range(kisi_sayisi):
            isim = input("Kişinin adını giriniz: ")
            self.grup.append(isim)
        print(f"Grubunuz başarıyla oluşturuldu: {', '.join(self.grup)}")


class Yakınarkadas(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)

    @staticmethod
    def Ekle():
        isim_listesi = ["Ahmet", "Ayşe", "Mehmet", "Zeynep", "Ali", 
                        "Elif", "Hasan", "Fatma", "Murat", "Sibel"]
        yakınarkadaslistesi = []
        
        while True:
            a = input("İsmi giriniz (çıkış için 'q'): ")
            if a == "q":
                print("Çıkış yapıldı.......")
                break
            
            if a in isim_listesi:
                yakınarkadaslistesi.append(a)
                print(f"Yakın arkadaş listesi: {yakınarkadaslistesi}")
            else:
                print(f"{a} isim listesinde bulunamadı.")





# Alt sınıf
class Bilgiver(Kullanici):
    def bilgiler(self):
        pass

# Bio sınıfı
class Bio(Bilgiver):
    def bilgiler(self):
        return f"Kullanıcı: {self.kullaniciad} {self.kullanicisoyad}, Email: {self.email}"

# Sifre sınıfı
class Sifre(Bilgiver):
    def bilgiler(self):
        return f"Şifre: {self.sifre}"


# Polimorfizm fonksiyonu
def göster(kullanıcı):
    print(kullanıcı.bilgiler())



class Erişim(Kullanici):
    def __init__(self, kullaniciad, kullanicisoyad, email, sifre,yenisifre,yeniad):
        super().__init__(kullaniciad, kullanicisoyad, email, sifre)
        self.__yenisifre=yenisifre   #private
        self._yeniad=yeniad  #procted

    def __sifreyi_goster(self):
        # Private: Şifreyi yalnızca sınıf içinde gösterebiliriz
        print(f" yeni sifre::{self.__yenisifre}")

    def adigoster(self):
        # Protected metot: sadece sınıf ve alt sınıflar erişebilir
        print(f"Yeni ad: {self._yeniad}")






"""kullanıcılar oluşturuluyor-------------------------------------------------------------------"""

k1 = Kullanici("Ahmet", "Yılmaz", "ahmet.yilmaz@gmail.com", 1234)
k2 = Kullanici("Fatma", "Kaya", "fatma.kaya@gmail.com", 5678)

"""Kullanıcı bilgilerini görüntüleme--------------------------------------------------------------------"""


print(k1.kisiselbilgi())  # Ahmet Yılmaz ahmet.yilmaz@gmail.com 1234
print(k2.kisiselbilgi())  # Fatma Kaya fatma.kaya@gmail.com 5678

"""Giriş yapma ve çıkış yapma----------------------------------------------------------------------------------"""


k1.uyegiris()
k1.uyecikis()

"""----------------------------------------------------------------"""

k3 = Kullanici("Ali", "Çelik", "ali.celik@gmail.com", 7890)
k4 = Kullanici("Ayşe", "Demir", "ayse.demir@gmail.com", 1122)

"""Arkadaş ekleme--------------------------------------------------------------------------------------------------"""
k1.arkadas_ekle(k3)
k2.arkadas_ekle(k3)
k2.arkadas_ekle(k4)

"""Ortak arkadaşları bulma---------------------------------------------------------------------------------"""
ortaklar = k1.ortak_arkadas(k2)
print(f"Ortak arkadaşlar: {[ark.kullaniciad for ark in ortaklar]}")


"""----------------------------------------------------------------------------------------------------"""

sk1 = StandartKullanici("Zeynep", "Yılmaz", "zeynep.yilmaz@gmail.com", 3344, "Yazılım geliştiricisi", "Türkçe")
sk2 = StandartKullanici("Burak", "Arslan", "burak.arslan@gmail.com", 5566, "Fotoğraf tutkunu", "İngilizce")
""" Dil seçimi--------------------------------------------------------------------------------------------"""

sk1.dilseçimi("Fransızca")
sk2.dilseçimi("Almanca")

"""Bio değiştirme----------------------------------------------------------------------------------------"""

sk1.biodegis("Python geliştiricisi ve içerik üreticisi.")
sk2.biodegis("Kamp ve doğa aşığı.")

"""Takip etme----------------------------------------------------------------------------------"""
sk1.takipet("Burak Arslan")
sk2.takipet("Zeynep Yılmaz")

"""Takibi bırakma-------------------------------------------------------------------------------"""
sk1.takibibirak("Burak Arslan")

"""-------------------------------------------------------------"""

p1 = Paylas("Merve", "Koç", "merve.koc@gmail.com", 9999)

"""Post ve story paylaşımı-------------------------------------------------------------------------------"""

p1.postat(3)  # 3 yeni post paylaşıldı.
p1.storyat(2)  # 2 yeni story paylaşıldı.

p2 = Paylas("Eren", "Deniz", "eren.deniz@gmail.com", 8888)
p2.postat(5)  # 5 yeni post paylaşıldı.
p2.storyat(4)  # 4 yeni story paylaşıldı.


"""-----------------------------------------------------------------------"""

g1 = Güvenlik("Hakan", "Taş", "hakan.tas@gmail.com", 1234)

"""Şifre kontrolü--------------------------------------------------------------------"""
g1.sifrekontrol()

"""Şifre kontrolü-----------------------------------------------------------------------"""
g1.sifredegistir(1234, 5678)  # Eski şifre doğruysa yeni şifre atanır.



pk1 = Premium("Can", "Büyük", "can.buyuk@gmail.com", 5555,False)
pk2 = Premium("Ece", "Şen", "ece.sen@gmail.com", 6666,True)

"""Premium kullanıcı işareti verme-----------------------------------------------------------"""
pk1.premium()  # Premium işareti aldı.
pk2.premium()  # İşareti alamadı.

"""-------------------------------------------------------------------------------"""

g1 = Grup("Melis", "Yıldız", "melis.yildiz@gmail.com", 1234)

"""Grup oluşturma-------------------------------------------------------------------------------"""

g1.grupkur()

"""Grup bilgisi-----------------------------------------------------------------------------------"""

print(f"Oluşturulan grup: {g1.grup}")



Yakınarkadas.Ekle()



# Nesneler oluşturma
bio = Bio("Şüheda", "Yılmaz", "suh@example.com", "1234")
sifre = Sifre("Şüheda", "Yılmaz", "suh@example.com", "1234")

# Bilgileri gösterme
göster(bio)    # Çıktı: Kullanıcı: Şüheda Yılmaz, Email: suh@example.com
göster(sifre)  # Çıktı: Şifre: 1234



kullanici1 = Erişim("Şüheda", "sarsılmaz", "sude@example.com", "12345","4567","haydar")
kullanici1._Erişim__sifreyi_goster()

kullanici1.adigoster()





