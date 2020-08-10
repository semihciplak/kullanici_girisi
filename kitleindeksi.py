boy=float(input("Boyunuzu Giriniz:"))
kilo=float(input("Kilonuzu giriniz:"))

index = kilo/(boy*boy)

print("indeksiniz", index)

if index < 18.5:
  print("zayıfsınız")

elif index <= 25:
  print("Normal")

elif index <= 30:
  print("fazla kilolu")

else:
  print("Obez")
