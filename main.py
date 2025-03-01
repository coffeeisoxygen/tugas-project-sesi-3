# Ahmad Hasan Maki
# 20240040032
# 085777076575

from booleantype import BooleanType
from numerictype import NumericType
from tekstype import TextType


def main():
    print("=== PENJELASAN TIPE DATA PYTHON ===")
    print("Pilih tipe data untuk dipelajari:")
    print("1. Boolean")
    print("2. String")
    print("3. Integer")
    print("4. Float")
    print("5. Complex")
    print("0. Keluar")

    while True:
        choice = input("\nMasukkan pilihan Anda (0-5): ")

        if choice == "1":
            data_type = BooleanType()
        elif choice == "2":
            data_type = TextType()
        elif choice == "3":
            data_type = NumericType("int")
        elif choice == "4":
            data_type = NumericType("float")
        elif choice == "5":
            data_type = NumericType("complex")
        elif choice == "0":
            print("Terima kasih telah menggunakan Penjelasan Tipe Data Python!")
            break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")
            continue

        print(f"\n{data_type.get_info()}")
        data_type.show_example()


if __name__ == "__main__":
    main()
