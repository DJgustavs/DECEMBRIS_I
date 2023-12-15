ievadits_skaitlis = int(input('Ievadi skaitli'))

if ievadits_skaitlis % 2 != 0:
    print(f'{ievadits_skaitlis} ir nepara')
else:
    print(f'{ievadits_skaitlis} ir pāra')


if ievadits_skaitlis % 5 == 0 and ievadits_skaitlis % 9 == 0:
    print(f'{ievadits_skaitlis} dalas ar 5 un 9')
else:
    print(f'{ievadits_skaitlis} nedalās vai ar 5 vai 9')