fecha = input("Ingrese una fecha en formato DD/MM: ")

dia, mes = fecha.split(' / ')

if dia == '25' and mes == '12':
    print("Es Navidad.")
else:
    print("No es Navidad.")
