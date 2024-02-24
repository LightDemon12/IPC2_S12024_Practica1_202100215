class Producto:
    def __init__(self, codigo, nombre, descripcion, precio_unitario):
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio_unitario = precio_unitario

class Cliente:
    def __init__(self, nombre, correo_electronico, nit):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.nit = nit

class Compra:
    def __init__(self, cliente, id_compra):
        self.cliente = cliente
        self.id_compra = id_compra
        self.lista_productos = []

    def agregar_producto(self, producto, cantidad):
        self.lista_productos.append((producto, cantidad))

    def calcular_costo_total(self):
        costo_total = sum(producto.precio_unitario for producto in self.lista_productos)
        return costo_total

    def agregar_producto(self, producto, cantidad):
        self.lista_productos.append((producto, cantidad))
    
    def generar_factura(self):
        costo_total = sum(producto.precio_unitario * cantidad for producto, cantidad in self.lista_productos)
        impuesto = costo_total * 0.12
        return costo_total, impuesto    

# Lista para almacenar los productos registrados
productos_registrados = [
  
    Producto("01", "Leche", "Leche entera", 5.0),
    Producto("02", "Pan", "Pan blanco", 2.5),
    Producto("03", "Huevos", "Huevos frescos", 3.0),
    Producto("04", "Arroz", "Arroz blanco", 4.0)
]

# Lista para almacenar los clientes registrados
clientes_registrados = [
    Cliente("Angel", "angel@gmail.com", "01")
]

# Lista para almacenar las compras realizadas
compras_realizadas = []

def registrar_producto():
    while True:
        print("Registrar Nuevo Producto")
        codigo = input("Ingrese el código del producto: ")

        # Verificar si el código del producto ya existe
        codigo_existente = False
        for producto in productos_registrados:
            if producto.codigo == codigo:
                print("Error: El código '{}' ya está en uso.".format(codigo))
                codigo_existente = True
                break

        if not codigo_existente:
            break

    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")

    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario >= 0:
                break
            else:
                print("Error: El precio no puede ser negativo.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido para el precio.")

    nuevo_producto = Producto(codigo, nombre, descripcion, precio_unitario)
    productos_registrados.append(nuevo_producto)

    print("Producto registrado exitosamente.")




def registrar_cliente():
    print("Registrar Nuevo Cliente")
    nombre = input("Ingrese el nombre del cliente: ")

    while True:
        correo_electronico = input("Ingrese el correo electrónico del cliente: ")
        correo_existente = any(cliente.correo_electronico == correo_electronico for cliente in clientes_registrados)
        if not correo_existente:
            break
        else:
            print("Error: Este correo electrónico ya está registrado.")
            continue  # Continuar solicitando el correo electrónico

    while True:
        nit = input("Ingrese el NIT del cliente: ")
        nit_existente = any(cliente.nit == nit for cliente in clientes_registrados)
        if not nit_existente:
            break
        else:
            print("Error: Este NIT ya está registrado.")
            continue  # Continuar solicitando el NIT

    nuevo_cliente = Cliente(nombre, correo_electronico, nit)
    clientes_registrados.append(nuevo_cliente)

    print("Cliente registrado exitosamente.")



def realizar_compra():
    print("Realizar Compra")
    nit_cliente = input("Ingrese el NIT del cliente: ")

    # Buscar el cliente por su NIT
    cliente_encontrado = None
    for cliente in clientes_registrados:
        if cliente.nit == nit_cliente:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is None:
        print("Error: No se encontró ningún cliente con ese NIT.")
        return

    id_compra = len(compras_realizadas) + 1
    nueva_compra = Compra(cliente_encontrado, id_compra)

    while True:
        print("------------- Menú Compra -------------")
        print("1. Agregar Producto")
        print("2. Terminar Compra y Facturar")
        print("------------------------------------------")
        opcion_compra = input("Seleccione una opción: ")

        if opcion_compra == "1":
            print("Lista de Productos Disponibles:")
            for producto in productos_registrados:
                print("Código: {}, Nombre: {}, Descripción: {}, Precio: {}".format(producto.codigo, producto.nombre, producto.descripcion, producto.precio_unitario))
            codigo_producto = input("Ingrese el código del producto: ")
            producto_encontrado = None
            for producto in productos_registrados:
                if producto.codigo == codigo_producto:
                    producto_encontrado = producto
                    break
            if producto_encontrado is not None:
                while True:
                    try:
                        cantidad = int(input("Ingrese la cantidad de unidades de '{}' que desea comprar: ".format(producto_encontrado.nombre)))
                        if cantidad > 0:
                            break
                        else:
                            print("Error: La cantidad debe ser mayor que cero.")
                    except ValueError:
                        print("Error: Por favor, ingrese un número entero válido para la cantidad.")
                nueva_compra.agregar_producto(producto_encontrado, cantidad)
                print("Producto agregado a la compra.")
            else:
                print("Error: No se encontró ningún producto con ese código.")
        elif opcion_compra == "2":
            compras_realizadas.append(nueva_compra)
            print("Compra con ID {} realizada y facturada exitosamente.".format(id_compra))
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")



def reporte_compra():
    print("Generar Reporte de Compra")
    id_compra = input("Ingrese el ID de la compra: ")

    # Convertir el ID de la compra ingresado a cadena
    id_compra = str(id_compra)

    compra_encontrada = None
    for compra in compras_realizadas:
        # Convertir el ID de la compra almacenado a cadena para comparar
        if str(compra.id_compra) == id_compra:
            compra_encontrada = compra
            break

    if compra_encontrada is None:
        print("Error: No se encontró ninguna compra con ese ID.")
    else:
        print("------------- REPORTE DE COMPRA {} -------------".format(id_compra))
        print("CLIENTE:")
        print("Nombre: {}".format(compra_encontrada.cliente.nombre))
        print("Correo electrónico: {}".format(compra_encontrada.cliente.correo_electronico))
        print("NIT: {}".format(compra_encontrada.cliente.nit))
        print("ARTÍCULOS COMPRADOS:")
        for i, (producto, cantidad) in enumerate(compra_encontrada.lista_productos, start=1):
            print("# Producto {}: {} - {} - Cantidad: {} - Precio unitario: Q{}".format(i, producto.codigo, producto.nombre, cantidad, producto.precio_unitario))
        costo_total, impuesto = compra_encontrada.generar_factura()
        total_con_impuestos = costo_total + impuesto
        print("Total: Q {:.2f}".format(costo_total))
        print("Impuestos por el 12%: Q {:.2f}".format(impuesto))
        print("Total con Impuestos: Q {:.2f}".format(total_con_impuestos))
        print("------------------------------------------")






def datos_estudiante():
    print("Datos del Estudiante")
    print("Nombre: Angel Guillermo de Jesús Pérez Jiménez")
    print("Número de Carnet: 202100215")

def menu_principal():
    while True:
        print("------------- Menú Principal -------------")
        print("1. Registrar Producto")
        print("2. Registrar Cliente")
        print("3. Realizar Compra")
        print("4. Reporte de Compra")
        print("5. Datos del Estudiante")
        print("6. Salir")
        print("------------------------------------------")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            registrar_cliente()
        elif opcion == "3":
            realizar_compra()
        elif opcion == "4":
            reporte_compra()
        elif opcion == "5":
            datos_estudiante()
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

# Lógica para ejecutar el programa
if __name__ == "__main__":
    menu_principal()
