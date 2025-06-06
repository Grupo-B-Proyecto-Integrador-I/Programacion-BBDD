from auth import Auth
from menu import Menu

def main():
     auth = Auth()
     menu = Menu()
     while True:
        print('¡Bienvenido! Seleciona una opción para avanzar:')
        print('1. Registar un usuario')
        print('2. Iniciar sesión')
        print('3. Salir del programa')

        option = input('Ingrese el numero de la operación que desea hacer:')

        if option == '1':
            auth.register()
        elif option == '2':
            if auth.login():
                menu.show_menu(auth.user_current, auth.users, auth)
        elif option == '3':
            print('¡Ya estas fuera del programa!')
            break
        else:
            print('Opción no valida')

if __name__ == "__main__":
    main()
