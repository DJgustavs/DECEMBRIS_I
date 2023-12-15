lietotāja_ievade = int(input("Ievadiet skaitli: "))

summa = 0 

for skaitlis in range(13, lietotāja_ievade +1):
    summa += skaitlis

print(f"Summa no 13 līdz {lietotāja_ievade},rezultats ir: {summa}")