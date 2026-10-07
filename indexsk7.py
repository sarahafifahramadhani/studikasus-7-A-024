import json

def lihat_data():
    print("=" * 57)
    print("\n               STOK DATA TOKO               ")
    print("=" * 57)
    with open("toko_kosmetik.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    if len(data) == "0":
        print("Data kosong, silahkan tambahkan data barang.")
    else:
        for barang in data:
            print("Brand       : ", barang["brand"])
            print("Kategori    : ", barang["kategori"])
            print("Stok        : ", barang["stok"])
            print("=" * 57)
#create
def tambah_brg():
    with open("toko_kosmetik.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    print("=" * 57)
    print("\n               DATA BARU               ")
    print("=" * 57)
    brand_br = input("Brand barang baru: ")
    kategori_br = input("Kategori barang baru: ")
    stok_br = input("Stok barang baru: ")
    data_baru = {
        "brand" : brand_br,
        "kategori" : kategori_br,
        "stok" : stok_br
}
    data.append(data_baru)
    print("Barang berhasil ditambahkan!")

    with open (r"toko_kosmetik.json", "w", encoding = "utf-8") as f:
        json.dump(data, f, indent=4)
#program utama
def main():
    while True:
        print("=" * 57)
        print("\n               STOK DATA TOKO               ")
        print("=" * 57)
        print("Pilih opsi dibawah ini.")
        print("1. Tampilkan Data Barang")
        print("2. Tambahkan Data barang")
        print("3. Keluar")
        opsi = input("\n Masukkan pilihan: ")

        if opsi == "1":
            lihat_data()
        elif opsi == "2":
            tambah_brg()
        elif opsi == "3":
            print("See you later!")
            break
        else:
            print("\n Opsi tidak ada, coba lagi.")

main()