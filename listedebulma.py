#Bir liste var ve bir karakterin listede olup olmadığını sorguladığımız bir if ve else deneme programı

liste=["a","b","c","d"]
hedef_harf= "x"

if hedef_harf in liste:   #bu in özelliğini daha önce görmemiştim. "in" listenin içindekileri arama gibi düşünülebilir. 
    print("Baba burada")
else: print("Burada kimse yok")
