import json

def agregar():
 with open("biblioteca.json","a") as libro:
 agre = libro.write(Autor,Categoria,Libro,Usuario,Prestamo)

 Autor = [
        {
            "AutorID" = enumerate("biblioteca.json"("AutorID"))
            "Nombre" = input("Ingresar Autor: ")
            "Nacionalidad" = input("Ingresar País: ")

        }]

 Categoria = [
        {
            "CategoriaID"= enumerate("biblioteca.json"("CategoriaID"))
            "Nombre" = input("Ingresar Categoria: ")
        }]
 
 Libro = [
        {
            "LibroID" = enumerate("biblioteca.json"("LibroID"))
            "Titulo" = input("Ingresar Título del libro: ")
            "AutorID" = enumerate("bibliotecas.json")("AutorID")
            "CategoriaID": enumerate("bibliotecas.json")("CategoriaID")
            "AnoPublicacion" = int(input("Año de publicación del libro: "))
            "ISBN" = input("Código de barra (ISBN) : ")
        }
 ]

 Usuario = [
        {
            "UsuarioID" = enumerate("biblioteca.json"("UsuarioID"))
            "Nombre" = input("Ingresar Nombre de usuario: ")
            "Email" = input("Email: ")
            "FechaRegistro" = input("Ingresar Fecha de registro")
        }]

 Prestamo = [
            {
            "PrestamoID" = enumerate("biblioteca.json"("PrestamoID"))
            "LibroID"= enumerate("biblioteca.json"("LibroID"))
            "UsuarioID" = enumerate("biblioteca.json"("UsuarioID"))
            "FechaPrestamo" = input("Ingresar Fecha de préstamo: ")
            "FechaDevolucion" = input("Ingresar Fecha de devolución: ")
        }
 ]
 

def mantenedor(agregar):
    
    global man(mantenedor(agregar))
    print("*******************************************")
    print("*           Mantenedor de libro           *")
    print("*******************************************")

    print("[1] Agregar libro")
    print("[2] Editar libro")
    print("[3] Eliminar libro")
    print("[4] Buscar libro")
    print("[5] Volver")

    opcion1 = int(input("Ingresa una opción >> "))

    if opcion1 == "1":
      add_libros = []

      with open("biblioteca.json","a") as agregar:
        agre = agregar.write(add_libros)
        
    while True:
         
         agregar = input("Agrega libros (Ingresar [salir] para finalizar")
         
         
         if agregar == "salir".lower:
            print(f"Libros agregados: {add_libros}")
            break
         agregar.append(add_libros)
         agre(add_libros)
            

     



    if opcion1 == "2":
       with open("biblioteca.json","w") as editar:

        palabra = input("Editar >> ")
        edit = editar.write(palabra)