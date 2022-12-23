print("""**************************
Faktöriyel Bulucu

çıkamak için q ya basınız

**************************""")
while True :
    sayı = input("Sayı:")
    if sayı == "q" :
        print("Uygulamadan Çıkılıyor...")
        break

    sayı =int(sayı)

    faktöriyel = 1

    for i in range(2,sayı+1) :
        faktöriyel *= i

    print("Faktöriyel",faktöriyel)
