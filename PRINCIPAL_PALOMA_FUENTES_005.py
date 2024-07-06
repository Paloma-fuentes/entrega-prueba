from FUNCIONES_PALOMA_FUENTES_005 import * 
bd = [
    {
        "ID": 1,
        "nombre": "MARTA",
        "apellido": "ALARCÓN",
        "correo": "martairene65@gmail.com",
        "compras": [{"fecha": "2024-07-01", "monto": 45000, "puntos": 450}]
    }
]

print("¡Bienvenido al control de clientes TODOAHORRO!")

while True:
    menu()
    opcion = input("Ingrese la opción que desea ejecutar: ")

    if opcion == "1":
        registrar_clientes(bd)

    elif opcion == "2":
        listar_clientes(bd)

    elif opcion == "3":
        registrar_compra(bd)

    elif opcion == "4":
        resumen_puntos(bd)

    elif opcion == "5":
        print("HASTA LA PRÓXIMA!")
        break 

    else:
        print("%$&$! HAGALO OTRA VEZ")