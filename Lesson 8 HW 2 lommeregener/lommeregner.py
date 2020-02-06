x = int(input("vælg tal: "))
y = int(input("vælg tal: "))

Lommeregner = input("Lommeregner +,-,*,/: ")

if Lommeregner == "+":
    print(x + y)
elif Lommeregner == "-":
    print(x - y)
elif Lommeregner == "*":
    print(x * y)
elif Lommeregner == "/":
    print(x / y)
else:
    print("Fejl kan ikke udregne. Brug kun +,-,* eller / .")