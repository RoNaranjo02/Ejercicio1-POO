from claseEmail import Email   
import csv

#def crearMail():
    #name = input ("Ingrese su nombre: ")
   # idcuenta = input ("Ingrese su ID: ")
   # dominio = input ("Ingrese dominio: ")
   # tipodom = input ("Ingrese tipo dominio: ")
   # contrasena = input ("Ingrese su contraseña: ")
   # unEmail = Email(idcuenta, dominio, tipodom, contrasena)
   # print('Estimado', name ,'le enviaremos sus mensajes a la direccion:', unEmail.retornaEmail())
   # return unEmail

def leerArchivo():
    archivo = open ("MailsPOO.csv")
    reader = csv.reader(archivo, delimiter=',')
    email3 = []
    for fila in reader:
        if '@' in fila[0] and '.' in fila[0]:
            email = Email()
            if email.crearCuenta(fila[0])!=None:
             email3.append(email)
        else: 
            print("Direccion {} incorrecta".format(fila[0]))
    for email in email3:
        print(email)
    return email3
        
       
if __name__ == "__main__":
  #  email = crearMail()
  #  email.cambiarContraseña()
    # direccion_email = input("Ingrese mail para crear una cuenta: ")
   # email2 = Email()
   # email2.crearCuenta(direccion_email)
   # print(email2.retornaEmail())
    email3 = leerArchivo()      
    cont = 0
    dom = input("Ingrese dominio a buscar: ")
    for email in email3:
        email.getdominio()
        if dom == email.getdominio():
            cont += 1
    print(cont)    
    