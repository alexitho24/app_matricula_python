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
lista_alumnos=[]
while True:
    opcion=input{"""elige lo que desas hacer
                 escribe  (s) si deseas registrar un alumno
                 escribe  (n) si deseas salir del programa 
                 escribir tu resúesta: """}
    if opcion. lower()=="n"
       break
nombre=input("ingrese el nombre del alumno: ")
apellido=input("ingrese el apellido del alumno: ")
alumno=(
    "nombre":nombre,
    "apellido":apellido 
)
lista_alumnos.append(alumno)
print(lista_alumnos) 
