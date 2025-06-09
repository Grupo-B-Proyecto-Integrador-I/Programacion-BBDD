from user import Admin, User

class Menu:

    def show_menu(self, current_user, users, auth):
        if current_user.user_role == 'admin':
            print(current_user.user_role)
            self.show_menu_admin(current_user, users, auth)
        else:     
            self.show_standard_menu(current_user, auth)
            
    def show_menu_admin(self, user: Admin, users, auth):
        while True:
            print(f'¡{user.user_name}! Seleciona una opción para avanzar:')
            print('1. Ver usuario')
            print('2. Modificar usuario')
            print('3. Eliminar usuario')
            print('4. Cerrar sesión')

            option = input('Ingrese el numero de la operación que desea hacer:')
            
            if option == '1':
                user.view_users(users)
            elif option == '2':
                user.modify_user(users)
            elif option == '3':
                user.delete_user(users)
            elif option == '4':
                auth.logout()
                break
            else:
                print("Opción no valida")
                
    def show_menu_user(self, user: User, auth):
        while True:
            print(f"\n¡Bienvenido {user.user_name}!")
            print("=== MENÚ USUARIO ===")
            print("1. Ver mi información personal")
            print("2. Cerrar sesión")

            option = input("Seleccione una opción (1-2): ").strip()

            if option == "1":
                user.view_personal_data()
            elif option == "2":
                auth.logout()
                print("\nSesión cerrada correctamente.")
                break
            else:
                print("\nOpción inválida. Por favor ingrese 1 o 2.")
