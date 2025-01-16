import os

class Market:
    def __init__(self, filename="product.txt"):
        self.filename = filename
        if not os.path.exists(self.filename):
            open(self.filename, 'w', encoding='utf-8').close()

    def __del__(self):
        pass

    def list_products(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            print("Ürün dosyası bulunamadı.")
            return
            
        if not lines:
            print("Ürün bulunmamaktadır.")
            return
        
        for index, line in enumerate(lines):
            urun = line.split(',')
            if len(urun) == 4:
                urun_adi, kategori, fiyat, stok = urun
                print(f"{index + 1}) Ürün Adı: {urun_adi}  Kategori: {kategori}  Fiyat: {fiyat}  Stok: {stok}")
            else:
                print("Hatalı ürün formatı:", line)

    def add_product(self):
        urun_adi = input("Ürün adı: ")
        kategori = input("Kategori: ")
        try:
            fiyat = float(input("Fiyat: "))
            stok = int(input("Stok miktarı: "))
        except ValueError:
            print("Geçersiz giriş. Fiyat ve stok sayı olmalıdır.")
            return

        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f"{urun_adi},{kategori},{fiyat},{stok}\n")
        print("Ürün eklendi.")

    def delete_product(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            print("Ürün dosyası bulunamadı.")
            return
        if not lines:
            print("Silinecek ürün bulunmamaktadır.")
            return
        self.list_products()
        try:
            urun_sirasi = int(input("Silinecek ürünün satır numarasını girin: "))
            if 1 <= urun_sirasi <= len(lines):
                del lines[urun_sirasi - 1]

                with open(self.filename, 'w', encoding='utf-8') as file:
                    for line in lines:
                        file.write(f"{line}\n")
                print("Ürün silindi.")
            else:
                print("Geçersiz satır numarası.")
        except ValueError:
            print("Geçersiz giriş. Satır numarası sayı olmalıdır.")

def menu():
    market = Market()
    while True:
        print("\n*** MENÜ ***")
        print("1) Ürünleri Listele")
        print("2) Ürün Ekle")
        print("3) Ürün Sil")
        print("4) Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == '1':
            market.list_products()
        elif choice == '2':
            market.add_product()
        elif choice == '3':
            market.delete_product()
        elif choice == '4':
            print("Programdan çıkılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()