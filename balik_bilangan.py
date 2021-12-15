def balik_bilangan(num):
    return int(str(num)[::-1])

ulang = 5
for i in range(ulang):
    x = int(input("Masukkan nilai : "))
    print(("Hasil balik====>"),balik_bilangan(num=x),"\n")

