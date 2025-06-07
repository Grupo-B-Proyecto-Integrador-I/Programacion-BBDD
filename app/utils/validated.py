def validated_password(password):
    return (
        len(password) <= 6 and
        any(c.isdigit() for c in password) and
        any(c.isalpha() for c in password)
    )

def validated_role(role):
    return role in ['user', 'admin']