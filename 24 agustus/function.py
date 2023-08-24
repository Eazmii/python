def Greeting(nama):
    print("hallo", nama)

def penjumlahan(a, b):
    hasil = a + b
    return hasil

    Greeting("Keyza")
    
    hasil_penjumlahan = penjumlahan(7, 9)
    print("Hasilnya adalah", hasil_penjumlahan)
    print(f"Hasilnya adalah {hasil_penjumlahan}")

    def jumlahkan(*args):
        total=0
        for angka in args:
            total += angka
            return total

            hasil = penjumlahan(12, 30, 40, 50, 5, 3, 7, 0, 700, 100)
            print("hasil penjumlahan: {hasil}")