toplam=int(input("Doğalgaz faturanız kaç para:"))
       
    
d1=int(input("Birinci daire faturanın yüzde kaçını ödüyor:"))	        
d2=int(input("İkinci daire faturanın yüzde kaçını ödüyor:"))	        


ekle = input("Hesaplanması için yeni daire eklemek ister misin? E/H:")

if ekle == "E":
    d3 = int(input("Yeni daire faturanın yüzde kaçını ödüyor:"))
    ödeme1 = toplam*d1/100
    ödeme2 = toplam*d2/100
    ödeme3 = toplam*d3/100  
    print("Birinci dairenin doğalgaz faturası", ödeme1)
    print("İkinci dairenin doğalgaz faturası", ödeme2)
    print("Üçüncü dairenin doğalgaz faturası", ödeme3)
    
    ekle1 = input("Hesaplaması için yeni daire eklemek ister misin? E/H:") 
    if ekle1 == "E":
        d4 = int(input("Yeni daire faturanın yüzde kaçını ödüyor:"))
        ödeme1 - toplam*d1/100
        ödeme2 - toplam*d2/100
        ödeme3 - toplam*d3/100
        ödeme4 - toplam*d4/100
        print("Birinci dairenin doğalgaz faturası", ödeme1)
        print("İkinci dairenin doğalgaz faturası", ödeme2)
        print("Üçüncü dairenin doğalgaz faturası", ödeme3)
        print("Dördüncü dairenin doğalgaz faturası", ödeme4)
    elif ekle1 =="H":
        ödeme1 - toplam*d1/100
        ödeme2 - toplam*d1/100
        ödeme3 - toplam*d1/100
        print("Birinci dairenin doğalgaz faturası", ödeme1)
        print("İkinci dairenin doğalgaz faturası", ödeme2)
        print("Üçüncü dairenin doğalgaz faturası", ödeme3)
        
    
        
elif ekle == "H":
    ödeme1=toplam*d1/100
    ödeme2=toplam*d2/100
    
    print("Birinci dairenin doğalgaz faturası",ödeme1)
    print("İkinci dairenin doğalgaz faturası",ödeme2)
    
