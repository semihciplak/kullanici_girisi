#Bir binaya gelen ortak doğalgaz faturasını, hane başına % kaç düştüğününü hesaplayan bir program. Önce Toplam fatura tutarını giriyorsunuz.
#Daha sonra her dairenin faturanın % kaçını ödediğini giriyorsunuz. Binada 5 daire ve bir dükkan olacak şekilde program çalışmaktadır.
#5ten az veya 5ten çok daire olması programın çalışma mantığına uygun değildir.



print("====DOĞALGAZ FATURASI HESAPLAMA PROGRAMI====")


toplam=int(input("Doğalgaz faturanız kaç para:"))


yüzde=0

        
while(yüzde!=100):        
        d1=int(input("Birinci daire faturanın yüzde kaçını ödüyor:"))
        d2=int(input("İkinci daire faturanın yüzde kaçını ödüyor:"))
        d3=int(input("üçüncü daire faturanın yüzde kaçını ödüyor:"))
        d4=int(input("Dördüncü daira faturanın yüzde kaçını ödüyor:"))
        d5=int(input("Beşinci daire faturanın yüzde kaçını ödüyor:"))
        dd=int(input("Dükkan faturanın yüzde kaçını ödüyor:"))

        print()
        print()
        
        yüzde=(d1)+(d2)+(d3)+(d4)+(d5)+(dd)     
        
        if yüzde!=100:
               print("Uyarı toplam %100 olmalıdır.Sizin yüzdeniz",yüzde)




        


ödeme1=toplam*d1/100
ödeme2=toplam*d2/100
ödeme3=toplam*d3/100
ödeme4=toplam*d4/100
ödeme5=toplam*d5/100
ödeme6=toplam*dd/100

print()
print()

print("Birinci dairenin doğalgaz faturası",ödeme1)
print("İkinci dairenin doğalgaz faturası",ödeme2)
print("İkinci dairenin doğalgaz faturası",ödeme3)
print("İkinci dairenin doğalgaz faturası",ödeme4)
print("İkinci dairenin doğalgaz faturası",ödeme5)
print("İkinci dairenin doğalgaz faturası",ödeme6)
