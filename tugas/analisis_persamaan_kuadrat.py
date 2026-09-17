import math

print("Analisis Persamaan Kuadrat")
a = float(input("Koefisien a: "))
b = float(input("Koefisien b: "))
c = float(input("Koefisien c: "))

if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    diskriminan = b ** 2 - 4 * a * c
    print(f"D: {diskriminan:.2f}")

    if diskriminan > 0:
        x1 = (-b + diskriminan ** 0.5) / (2 * a)
        x2 = (-b - diskriminan ** 0.5) / (2 * a)
        print("Memiliki dua akar real berbeda:")
        print(f"x1 = {x1:.2f}")
        print(f"x2 = {x2:.2f}")
    elif diskriminan == 0:
        x = -b / (2 * a)
        print("Memiliki satu akar real kembar:")
        print(f"x = {x:.2f}")
    else:
        print("Tidak memiliki akar real.")
