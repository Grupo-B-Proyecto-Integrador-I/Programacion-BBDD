from user import Admin

class Menu:

    def show_menu(self, current_user, users, auth):
        if current_user.user_role == 'admin':
            print(current_user.user_role)
            self.show_menu_admin(current_user, users, auth)

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
            if option == '4':
                auth.logout()
                break
            else:
                print("Opción no valida")