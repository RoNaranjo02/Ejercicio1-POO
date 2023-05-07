import re
class Email:
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contrasena = ""

    def __init__(self, idCuenta="", dominio="", tipoDominio="", contrasena=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena

    #def retornaEmail(self):
        #return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"
    
    def getDominio(self):
        return self.__dominio
    
   # def getContraseña(self):
        #self.__contrasena = input("Ingrese su contraseña: ")

    def crearCuenta(self, direccionCorreo):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        valid = re.fullmatch(regex, direccionCorreo)
        if valid:
            print("Valid email")
            partes = direccionCorreo.split("@")
            self.__idCuenta = partes[0]
            DominioyTipoDominio = partes[1].split(".")
            self.__dominio = DominioyTipoDominio [0]
            self.__tipoDominio = DominioyTipoDominio [1]
        else:
            print("Invalid email")
        return valid
    
    def __str__(self) -> str:
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"
    
    #def cambiarContraseña(self):
        #print ("*****Cambio de contraseña*****")
       # Opass = input("Ingrese contraseña actual: ")
       # if Opass == self.__contrasena:
              #  npass = input("Ingrese nueva contraseña: ")
               # self.__contrasena = npass
              #  print("Contraseña cambiada con éxito")
       # elif Opass != self.__contrasena:
          #  print("Contraseña incorrecta.")
            #self.cambiarContraseña()
        

   