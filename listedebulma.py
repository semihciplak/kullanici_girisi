#Bir liste var ve bir karakterin listede olup olmadığını sorguladığımız bir if ve else deneme programı

liste=["a","b","c","d"]
hedef_harf=input("Eğer listeye olmayan bir eleman eklemek istiyorsan buraya yazabilirsin. ")

if hedef_harf in liste:   #bu in özelliğini daha önce görmemiştim. "in" listenin içindekileri arama gibi düşünülebilir. 
   print("yazdığın eleman zaman listede mevcut")
    print(liste)
else: 
    liste.append(hedef_harf)
    print("yazdığınız listede yoktu, ama ben onu listeye ekledim. Yeni listen", liste, "bu şekilde")
