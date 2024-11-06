import random

# 1
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

# 2
incercari_ramase = 6
litere_incercate = []

print(" ".join(progres))
print(f"Încercări rămase: {incercari_ramase}")

while incercari_ramase > 0 and "_" in progres:
    # a
    litera = input("Introdu o literă: ").lower()

    # b
    if len(litera) != 1 or not litera.isalpha():
        print("Te rog introdu o singură literă validă!")
        continue
    if litera in litere_incercate:
        print("Ai încercat deja această literă. Încearcă altceva!")
        continue

    litere_incercate.append(litera)

    # c
    if litera in cuvant_de_ghicit:
        for i, l in enumerate(cuvant_de_ghicit):
            if l == litera:
                progres[i] = litera
        print("Bravo! Litera este corectă!")
    else:
        incercari_ramase -= 1
        print(f"Litera '{litera}' nu este în cuvânt. Încercări rămase: {incercari_ramase}")

    # 3
    print("Progres: " + " ".join(progres))
    print(f"Încercări rămase: {incercari_ramase}")
    # 4
if "_" not in progres:
    print(f"Felicitări! Ai ghicit cuvântul: {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut! Cuvântul era: {cuvant_de_ghicit}")