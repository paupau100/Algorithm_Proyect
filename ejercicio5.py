productos = ["laptop", "mause", "teclado", "monitor", "audifonos"]

precios = [2500000, 45000, 120000, 890000, 200000]

def mostrar_inventario(productos, precios ):

    print("INVENTARIO")
    for i in range(len(productos)):
        print(productos[i], ":", precios[i])
def calcular_valor_total(precios):
    return sum(precios)
def buscar_producto(productos, nombre):
    for producto in productos:
        if producto.lower() == nombre.lower():
            return "producto encontrado"
    return "producto no encontrado"
def producto_mas_caro(productos, precios):
    precio_maryor = max(precios)
    posicion = precios.index(precio_maryor)
    return productos[posicion], precio_maryor
def friltrar_prodductos_precio(productos, precios, maximo):
    print("PRODUCTOS MENORES O IGUALES",  maximo)
    for i in range(len(precios)):
        if precios[i] <= maximo:
            print(productos[i], ":", precios[i])
def aplicar_decuento(precios, porcentaje):
    precios_con_descuento = []
    for precio in precios:
        nuevo_precio = precio -(precio * porcentaje/100)
        precios_con_descuento.append(nuevo_precio)
    return precios_con_descuento
def probar_inventario():
    mostrar_inventario(productos,precios)
    print("-"*30)
    total= calcular_valor_total(precios)
    print("Valor total del inventario:", total)
    print("-"*30)
    print(buscar_producto(productos, "teclado"))
    print(buscar_producto(productos, "celular"))
    print("-"*30)
    nombre_producto, precio = producto_mas_caro(productos, precios)
    print("Producto mas caro:", nombre_producto, "con un precio de", precio)
    print("-"*30)
    friltrar_prodductos_precio(productos, precios, 200000)
    print("-"*30)
    nuevos_precios = aplicar_decuento(precios, 10)
    print("Precios con descuento del 10%:")
    for i in range(len(productos)):
        print(productos[i], ":", nuevos_precios[i])
def main():
    probar_inventario()
main()