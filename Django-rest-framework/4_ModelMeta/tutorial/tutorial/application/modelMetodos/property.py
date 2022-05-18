class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email
        
    def __generar_password(self, password):
        return password.upper()
    
    def get_password(self):
        return self.__password
    
    @property
    def password(self):
        print("Esto es un property")
        return self.__password
    
    #cambio de password
    @password.setter
    def password(self, valor):
        print("Esto es un setter")
        self.__password = self.__generar_password(valor)
    
nombre = Usuario("brian", "briandb", "brian@mail.com")
# print(nombre)
print("<-----", nombre.password)

# nombre.password = "Nuevo Password" 
print("----->", nombre.password)


    
    
    