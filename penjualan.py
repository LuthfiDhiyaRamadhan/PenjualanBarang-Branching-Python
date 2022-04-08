print("Perhitungan Penjualan Barang")
print("-"* 30)
kode=input("Kode Barang     :")
qty=int(input("Qty          :"))
print("-"* 30)
if kode=="PG001":
    print("Nama Barang       : Penggaris 30 cm")
    harga=15000
    print(f"Harga             : Rp.{harga}")
elif kode=="BK001":
    print("Nama Barang       : Buku Tulis")
    harga = 5000
    print(f"Harga            : Rp.{harga}")
elif kode=="PS002":
    print("Nama Barang       : Pensil")
    harga = 2500
    print(f"Harga             : Rp.{harga}")
else:
    print("Kode Barang Tidak tersedia")

subtotal= harga*qty
print(f"Subtotal          : Rp.{subtotal}")
if subtotal <=20000:
    diskon=0.30 * subtotal
else:
    subtotal>20000
    diskon=20000
print(f"Diskon          : Rp.{diskon:10.0f}")
totalbayar=subtotal-diskon
print(f"Total Bayar     : Rp.{totalbayar:10.0f}")

