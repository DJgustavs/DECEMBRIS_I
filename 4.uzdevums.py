ievadits_skaitlis = int(input('Ievadiet skaitli:'))

faktorials = 1

for skaitlis in range(1, ievadits_skaitlis + 1):
    faktorials *= ievadits_skaitlis

print(f' faktorials no {ievadits_skaitlis} ir {faktorials}')