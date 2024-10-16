import modulku

def main():
    r = int(input("Masukkan jari-jari lingkaran: "))
    luas = modulku.luas_lingkaran(r)
    keliling = modulku.keliling_lingkaran(r)

    print(f"Luas lingkaran adalah: {luas:.2f}")
    print(f"Keliling lingkaran adalah: {keliling:.2f}")

main()
