# """
# - registrar alumnos
# - generar fichas de matricula
# - mostrar la lista de todos los matriculados 
# - filtrar matriculados por programa de estudio
# """
# lista_alumnos=[]
#inicio de problema
#necesito poder agregar mas alumnos sin necesidad 
# nombre=input("ingrese el nombre del alumno: ")
# apellido=input("ingrese el apellido del alumno")
# lista_alumnos.append(nombre)
# # lista_alumnos.append(apellido)
# alumnos={}
# # deseo mostrar un menu con las opciones de agregar 
# print(lista_alumnos)
## tarea
# lista_alumnos=[]
# def mensaje_menu():
#     menu_opciones=input("""
#     ------------Bienvenido al sistema------------
#     -------------Registra tu alumno--------------
    
# 1. escribe  (s) si deseas registrar un alumno
# 2. escribe  (n) si deseas salir del programa 
# escribe la accion que deseas realizar: """)
# print(menu_opciones)

# while true:
#     if menu_opciones. lower()== "n":
#         print("saliendo del sistema")
#         break
#     if menu_opciones. lower()== "s":
     
# nombre=input("ingrese el nombre del alumno: ")
# apellido=input("ingrese el apellido del alumno: ")
# alumno=(
#     "nombre":nombre,
#     "apellido":apellido 
# )
# lista_alumnos.append(alumno)
# print(lista_alumnos) 
### clase_resolucion de la tarea con el profe_lunes_14

lista_alumnos=[]
def mensaje_menu():
    menu_opciones = """
    ------------Bienvenido al sistema------------
    -------------Registra tu alumno--------------
    
1. escribe  (s) si deseas registrar un alumno
2. escribe  (n) si deseas salir del programa 
escribe la accion que deseas realizar: """
    return menu_opciones

def ingresar_datos_alumno():
    id =len(lista_alumnos)+1
    cui =int(input("ingrese el numero de dni: "))
    nombre =input("ingrese el nombre del alumno: ")
    apellido =input("ingrese el apellido del alumno: ")
    numero_celular =int(input("ingrese el numero de celular: "))
    programa_estudio =input("ingrese el programa de estudio")
    ciclo_academico =input("ingrese su ciclo academico. ")
    email =input("ingrese su correo electronico")

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
         alumno={
                "id":id,
                "cui":cui,
                "nombre":nombre,
                "apellido":apellido,
                "numero_celular":numero_celular,
                "programa_estudio":programa_estudio,
                "ciclo_academico":ciclo_academico,
                "email":email
               }
        
         lista_alumnos.append(alumno)
while True:
   menu_opciones=input(mensaje_menu())

   if menu_opciones.lower() == "n":
       print("saliendo del sistema")
       break
   elif menu_opciones.lower() == "s":
       ingresar_datos_alumno()
   else:
        print("opciones erronea")

print(lista_alumnos)
