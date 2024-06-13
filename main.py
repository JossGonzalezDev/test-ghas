def get_database_password():
    password = "password123"
    return password

def connect_to_database():
    db_password = get_database_password()
    # Conectar a la base de datos usando la contraseña
    print("Conectado a la base de datos con la contraseña:", db_password)

if __name__ == "__main__":
    connect_to_database()
