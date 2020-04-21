import  random

def venta_inmuebles():
    print("Venta de inmuebles")
    zona = ["Norte","Sur","Oriente","Centro"]
    precio = [1000000,2000000,1500000,3000000]
    transito = ["Bajo","Medio","Medio","Alto"]
    gastos_mensuales = [100000,150000,200000,300000]
    produccion = [2,4,3,6]
    capital = 10000000
    pproduccion = 0

    print("Compra de inmuebles para ampliar la empresa")
    print("A continuacion se presentan los inmuebles disponibles:\n")

    for i in [1,2,3,4]:
        print("Inmueble ",i)
        print("La ubicacion del inmueble es en la zona : ",zona[i-1])
        print("Precio del inmueble:", precio[i-1])
        print("El transito de personas por la zona es: ",transito[i-1])
        print("Los gastos mensuales del inmuebles seran de: ",gastos_mensuales[i-1])
        print("El aumento de produccion con la compra del nuevo inmueble es del: ",produccion[i-1],"porciento\n")


    op = int(input("Desea comprar un nuevo inmueble?  1) Si  2)  No"))

    if op == 1:
        op = int(input("Que inmueble desea comprar?"))
        if op>0 and op<=4 :
            print("El capital que se descontara de los activos es: ", precio[op - 1])
            print("Los gastos mensuales seran de: ", gastos_mensuales[op - 1])
            print("El aumento de produccion con la compra del nuevo inmueble es del :",produccion[op - 1],"porciento")
            capital = capital - precio[op - 1] - gastos_mensuales[op - 1]
            pproduccion = pproduccion + produccion[op - 1]
            print("\nEl capital final de la compra del inmueble menos los gastos del primer mes es de: \n", capital)
            print("El porcentaje de produccion aumento a : ", pproduccion,"porciento")
        else:
            print("opcion incorrecta")


    dec = int(input("Desea comprar otro inmueble? 1) SI 2) NO"))
    if dec == 1:
        venta_inmuebles()


def inversion_propuesta():
    print("Inversion propuesta")
    print(random.randint(10,20))
    capital = 10000000
    acciones = 100

    print("\n\tEn esta seccion recibiras propuestas de diversos socios interesados en comprar acciones de tu empresa\n")
    deci = int(input("Desea generar una propuesta de inversion?: 1) SI 2) NO"))

    if deci == 1:
        print("\nLa propuesta es la siguiente: \n")
        random_dinero = (random.randint(1, 50))
        random_porcentaje = (random.randint(1,20))
        print(f"Este socio desea invertir el {random_dinero} porciento del capital que tienes")
        print(f"Por el {random_porcentaje} porciento de tu empresa\n");
        decis = int(input("Te interesa esta propuesta? 1) SI 2) NO "))

        if decis == 1:
            dinero_ganado = (random_dinero*capital)/100
            print(f"El capital que gano al realizar la inversion es: {dinero_ganado} ")
            print(f"El porcentaje de acciones de tu socio son de {random_porcentaje}")
            acciones_dueno = acciones - random_porcentaje
            print(f"El porcentaje de tus acciones es de : {acciones_dueno}")


    decisi = int(input("Desea generar otra propuesta de inversion? 1) SI 2) NO "))
    if decisi == 1:
        inversion_propuesta()


def inversion_publicidad():
    produccion = 100.0
    capital = 10000000.00
    print("Inversion en publicidad")
    print("En esta seccion se puede invertir en publicidad")
    print("Usted decide la canttidad de dinero que desea invertir")
    print("Con el dinero que propone se hara una cotizacion con la cual puede aceptar o no")
    inver_pu = float(input("Ingrese la cantidad de dinero que desea invertir en publicidad"))

    aumento_produccion = (inver_pu*1)/50000
    print(f"El aumento de produccion sera de: {aumento_produccion} porciento")

    desici = int(input("Le interesa invertir esa cantidad presione 1, si desea modificarla presione 2"))
    if desici ==1:
        capital = capital - inver_pu
        produccion = produccion + aumento_produccion
        print(f"El capital final es de: {capital}")
        print(f"El porcentaje de produccion final es de : {produccion} porciento")

    if desici == 2:
        inversion_publicidad()

global lista
lista = list()

class Empleado:
    nombre = ("")
    cargo = ("")
    sueldo = 0
    



def contratacion_empleados():
    print("Contratacion de empleados")
    print("En esta seccion se podran contratar empleados para aumentar la produccion de la empresa")

    print("A continuacion se muestran las areas funcionales en las cuales se puede contratar empleados")
    print("1. Direccion   general")
    print("2. Auxiliar   administrativo")
    print("3. Administracion  y  recursos  humanos")
    print("4. Finanzas  y  contabilidad")
    print("5. Publiadad  y  mercadotecnia")
    print("6. Informatica")
    print("7. Produccion")
    opci = int(input("Ingrese el numero del area en la que desea contratar personal"))
    if opci == 1:
        a = Empleado()
        a.nombre = input("Ingrese nombre de empleado")
        a.cargo = input("Ingrese el cargo que desempeñara")
        a.sueldo = input("Ingrese sueldo del empleado")

        lista.append(a)

    elif opci ==2:
        b = Empleado()
        b.nombre = input("Ingrese nombre de empleado")
        b.cargo = input("Ingrese el cargo que desempeñara")
        b.sueldo = input("Ingrese sueldo del empleado")

        lista.append(b)

    elif opci == 3:
        c = Empleado()
        c.nombre = input("Ingrese nombre de empleado")
        c.cargo = input("Ingrese el cargo que desempeñara")
        c.sueldo = input("Ingrese sueldo del empleado")

        lista.append(c)

    elif opci == 4:
        d = Empleado()
        d.nombre = input("Ingrese nombre de empleado")
        d.cargo = input("Ingrese el cargo que desempeñara")
        d.sueldo = input("Ingrese sueldo del empleado")

        lista.append(d)

    elif opci == 5:
        e = Empleado()
        e.nombre = input("Ingrese nombre de empleado")
        e.cargo = input("Ingrese el cargo que desempeñara")
        e.sueldo = input("Ingrese sueldo del empleado")

        lista.append(e)

    elif opci == 6:
        f = Empleado()
        f.nombre = input("Ingrese nombre de empleado")
        f.cargo = input("Ingrese el cargo que desempeñara")
        f.sueldo = input("Ingrese sueldo del empleado")

        lista.append(f)

    elif opci == 7:
        g = Empleado()
        g.nombre = input("Ingrese nombre de empleado")
        g.cargo = input("Ingrese el cargo que desempeñara")
        g.sueldo = input("Ingrese sueldo del empleado")

        lista.append(g)

    else :
        print("Numero invalido")

def menu():
    opcion=0
    salir=5

    while opcion != salir:
        #mostrar menu
        print("1. Venta de inmuebles")
        print("2. Inversiones propuestas")
        print("3. Inversion en publicidad")
        print("4. Contratatacion de empleados")
        print("5. Salir")

        opcion = int(input("Digite opcion"))

        if opcion == 1:
            venta_inmuebles()
        elif opcion == 2:
            inversion_propuesta()
        elif opcion == 3:
            inversion_publicidad()
        elif opcion == 4:
            contratacion_empleados()
        elif opcion == 5:
            exit()

menu()

