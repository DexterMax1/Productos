producto = []

def encontrar(producto, reemplazar, nuevo):
    for index, item in enumerate(producto):
        if item == reemplazar:
            producto[index] = nuevo
            

      
      

seleccion = 0
while seleccion !=4:
      print("1. Registrar Producto")
      print("2. Ver Lista de Productos")
      print("3. Editar")
      print("4. Eliminar Producto")
      print("5. Salir")

      seleccion = int(input("Selecciona una opcion: "))
      if seleccion == 1:
            registrar=input("Ingresar el producto: ")
            producto.append(registrar)
      elif seleccion == 2:
            print(producto)
      elif seleccion == 3:
            edit = input('Ingrese el producto que desea eliminar: ')
            if edit in producto:
                nuevo = input(f'Producto que desea cambiar {producto}: ')
                encontrar(producto, edit, nuevo)
      elif seleccion == 4:
            borrar = input("¿Qué producto quieres eliminar?: ")
            producto.remove(borrar)
            print(producto)
      elif seleccion == 5:
            print("Gracias por usarnos.")
            break
               



                  