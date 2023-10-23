class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f}"


class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre}\nDirección: {self.direccion}\nTeléfono: {self.telefono}"


class Venta:
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos

    def calcular_total(self):
        total = sum(producto.precio for producto in self.productos)
        return total

    def generar_factura(self):
        factura = f"Factura para {self.cliente.nombre}:\n"
        for producto in self.productos:
            factura += f"{producto}\n"
        factura += f"Total: ${self.calcular_total():.2f}"
        return factura

# Estructura de datos para almacenar los objetos
productos = []
clientes = []
ventas = []

# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("P1", "Producto 1", 10.99)
    producto2 = Producto("P2", "Producto 2", 7.99)
    producto3 = Producto("P3", "Producto 3", 14.99)

    productos.extend([producto1, producto2, producto3])

    # Crear cliente
    cliente1 = Cliente("Angie", "123 Calle Principal", "9994567890")
    
    clientes.append(cliente1)

    # Crear venta
    productos_venta = [producto1, producto2, producto3]
    venta1 = Venta(cliente1, productos_venta)

    ventas.append(venta1)

    # Mostrar factura
    print(venta1.generar_factura())
