from utils.validated import validated_password

class User:
    __id = 1

    def __init__(self, user_name, user_password):
        self.user_id = User.__id
        self.user_role = 'user'
        self.user_name = user_name
        self.user_password = user_password
        User.__id += 1


    def view_personal_data(self):
        print("\n=== TUS DATOS ===")
        print(f"Nombre: {self.user_name}")
        print(f"Rol: {self.user_role}")


class Admin(User):
    def __init__(self, user_name, user_password):
        super().__init__(user_name, user_password)
        self.user_role = 'admin'

    def view_users(self, users):
        print('--* Lista de usuario *--')
        for user in users:
            print(f"• Usuario: {user.user_name} - Rol: {user.user_role}")

    def modify_user(self, users): 
        print('--* Modificar Usuario *--')
        user_to_modify_name = input('Ingrese el nombre del usuario a modificar:').upper()

        found_user = None
        for user in users:
            if user.user_name == user_to_modify_name:
                found_user = user
                break

        if not found_user:
            print(f"Usuario '{user_to_modify_name}' no encontrado.")
            return

        print(f"Usuario encontrado: {found_user.user_name} (Rol actual: {found_user.user_role})")
        print("¿Qué desea modificar?")
        print("1. Contraseña")
        print("2. Rol")
        
        while True:
            option = input("Ingrese el número de la opción (1 o 2):")
            if option == '1':
                while True:

                    new_password = input('Nueva contraseña:')
                    if validated_password(new_password):
                        found_user.user_password = new_password
                        print(f"Contraseña de '{found_user.user_name}' modificada correctamente (en memoria).")                        
                        break
                    print('¡La contraseña debe tener un máximo de 6 caracteres y contener letra y números!')

                break

            elif option == '2':
                while True:
                    new_role = input("Nuevo rol (user o admin):").title()                    
                    
                    if new_role == 'admin' or new_role == 'user':
                        found_user.user_role = new_role
                        print(f"Rol de '{found_user.user_name}' modificado a '{new_role}' (en memoria).")                        
                        break

                    print("¡El rol es inválido, debe ser 'user' o 'admin'!")
                break

            else:
                print("Opción no válida. Ingrese 1 o 2.")
                
    def delete_user(self, users):
        print('--* Eliminar Usuario *--')
        user_to_delete = input('Ingrese el nombre del usuario a eliminar:').upper()

        for user in users:
            if user.user_name.upper() == user_to_delete:
                if user.user_name.upper() == self.user_name.upper():
                    print("No puedes eliminar tu propio usuario.")
                    return
                users.remove(user)
                print(f"Usuario '{user_to_delete}' eliminado correctamente.")
                return

        print(f"Usuario '{user_to_delete}' no encontrado.")
                
                
                