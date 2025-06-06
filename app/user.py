
class User:
    __id = 1

    def __init__(self, user_name, user_password):
        self.user_id = User.__id
        self.user_role = 'user'
        self.user_name = user_name
        self.user_password = user_password
        User.__id += 1


class Admin(User):
    def __init__(self, user_name, user_password):
        super().__init__(user_name, user_password)
        self.user_role = 'admin'

    def view_users(self, users):
        print('--* Lista de usuario *--')
        for user in users:
            print(f"• Usuario: {user.user_name} - Rol: {user.user_role}")
