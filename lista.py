# Creación de una lista para las compras
compras = []

# Agregar elementos a la lista
compras.append("Pan")
compras.append("Leche")
compras.append("Huevos")
compras.append("Tomates")
compras.append("Café")
compras.append("Arroz")
compras.append("Helado")

print("Lista inicial de compras:")
print(compras)

# Eliminar un producto ya comprado
producto_comprado = compras.pop(4)
print("Se compró:", producto_comprado)

# Mostrar cómo queda la lista actualizada
print("Lista pendiente de compras:")
print(compras)