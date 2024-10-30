meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]
tavi = ["tava"] * 7
istoric_comenzi = []

contor_comenzi = {"papanasi": 0, "ceafa": 0, "guias": 0}

# 1
print("Servirea comenzilor:")
while studenti and comenzi:
    student = studenti.pop(0)
    comanda = comenzi.pop(0)
    if tavi:
        tavi.pop()

    istoric_comenzi.append((student, comanda))
    contor_comenzi[comanda] += 1

    print(f"{student} a comandat {comanda}.")

# 2
print("\nInventar:")
print(f"S-au comandat {contor_comenzi['guias']} guias, {contor_comenzi['ceafa']} ceafa, {contor_comenzi['papanasi']} papanasi.")
print(f"Mai sunt {len(tavi)} tavi.")

for produs in ["ceafa", "papanasi", "guias"]:
    disponibil = meniu.count(produs) > contor_comenzi[produs]
    print(f"Mai este {produs}: {disponibil}.")

# 3
print("\nFinanțe:")

total_incasari = 0
for produs, pret in preturi:
    total_incasari += contor_comenzi[produs] * pret
print(f"Cantina a încasat: {total_incasari} lei.")

produse_ieftine = [produs for produs in preturi if produs[1] <= 7]
print("Produse care costă cel mult 7 lei:", produse_ieftine)
