from user import User, Admin
from utils.validated import validated_password, validated_role


class Auth:
    def __init__(self):
        self.users = []
        self.user_current = None

        #Usuarios por defecto para pruebas
        self.users.append(Admin('MELI', 'use123'))
        self.users.append(User('nuevo', 'use123'))
        self.users.append(User('nuevoDos', 'use123'))

    def login(self):
        print('--* Inicio de sesión *--')
        name = input('Nombre de usuario: ').strip()
        password = input('Contraseña:')

        for user in self.users:
            if user.user_name.lower() == name.lower() and user.user_password == password:
                self.user_current = user
                print('¡Se inició sesión correctamente!')
                return True
        
        print('Credenciales invalidas, intente nuevamente.')
        return False
    

    def register(self):
        print('--* Registrar un usuario *--')
        name = input('Nombre de usuario: ').strip()

        while True:
            password = input('Contraseña:')
            if validated_password(password):
                break
            print('¡La contraseña debe tener un máximo de 6 caracteres y contener letra y números!')

        while True:
            role = input('Rol (user o admin):').lower()
            if validated_role(role):
                break
            print("¡El rol es invalido, debe ser 'user' o 'admin'!")

        if role == 'admin':
            new_user = Admin(name, password)
        else:
            new_user = User(name, password)

        self.users.append(new_user)
    
    def logout(self):
        if self.user_current:
            print('Se cerró sesión correctamente')
            self.user_current = None
        else:
            print('No hay sesión iniciada')
