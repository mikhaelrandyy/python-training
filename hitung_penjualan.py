def hitung_penjualan(transaksi):
    total_pendapatan = 0
    produk_terjual = {}

    # Hitung total pendapatan dan jumlah per produk
    for t in transaksi:
        total_pendapatan = total_pendapatan + t["jumlah"] * t["harga"]
        produk = t["produk"]
        produk_terjual[produk] = produk_terjual.get(produk, 0) + t["jumlah"]

    # Cari produk terlaris
    produk_terlaris = max(produk_terjual, key=produk_terjual.get)

    # Tampilkan hasil
    print("=== Laporan Penjualan ===")
    print(f"Total Pendapatan: Rp {total_pendapatan:,}")
    print("\nJumlah Terjual per Produk:")
    for p, j in produk_terjual.items():
        print(f"- {p}: {j} unit")
    print(f"\nProduk Terlaris: {produk_terlaris}")

# Contoh data
transaksi = [
    {"id": 1, "produk": "A", "jumlah": 2, "harga": 5000},
    {"id": 2, "produk": "B", "jumlah": 1, "harga": 12000},
    {"id": 3, "produk": "A", "jumlah": 1, "harga": 5000}
]

hitung_penjualan(transaksi)
