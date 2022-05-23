print("\nCalculadora de cantidades de ingredientes para la masa de la pizza\n(Pizza pequeña: 125 gramos)\n(Pizza mediana: 250 gramos)\n")

mfinal = int(input("Introduce los gramos de masa final para la pizza que quieras tener: "))

mmharina = mfinal * 0.162602
mmagua = mmharina
mmlevadura = mfinal * 0.004065
mmmiel = mmlevadura
mharina = mfinal * 0.406504
magua = mfinal * 0.243902
msal = mfinal * 0.016260


print("\nPara la masa necesitarás:")
print(str(round(mmharina, 1)) + " gramos de harina")
print(str(round(mmagua, 1)) + " gramos de agua")
print(str(round(mmmiel, 1)) + " gramos de miel")
print(str(round(mmlevadura, 1)) + " gramos de levadura")
print("\nPara la masa madre necesitarás:")
print(str(round(mharina, 1)) + " gramos de harina")
print(str(round(magua, 1)) + " gramos de agua")
print(str(round(msal, 1)) + " gramos de sal")