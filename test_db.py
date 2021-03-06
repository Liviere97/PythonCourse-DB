import sqlite3

#creando base de datos
def create_or_get_database():
    conn = sqlite3.connect('hamburguer.db')
    print("Database connected")
    return conn

#metodo para crear tablas
def create_table(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS hamburguer (
            name VARCHAR NOT NULL,
            price DOUBLE NOT NULL,
            size VARCHAR NOT NULL,
            ingredients TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conn.execute(sql)
    print("All the tables has been created succesfully")

# funcion para saber si la opcion es valida
def validate_user_selection(selection):
    return isinstance(selection, int) and selection >0 and selection < 6

def get_hamburguers(conn):
    print()
    print("-------------------------------")
    print('LISTA DE HAMBURGUESAS DISPONIBLES')
    print("-------------------------------")
    print('Nombre \t\t\t Precio \t\t\t Tamaño')
    sql = '''
        SELECT 
            name, price, size
        FROM
            hamburguer
    '''
    cursor = conn.execute(sql)
    for row in cursor:
        print(f'{row[0]} \t\t\t {row[1]} \t\t\t {row[2]}')
    print('----------------------------------')
    print()

def get_hamburguer(conn,rowid=None):
    if not rowid:
        rowid = input('Ingresa el ID de la hamburguesa que quieres visualizar: ')
    sql = '''
        SELECT 
            rowid, name, price, size, ingredients, timestamp
        FROM
            hamburguer
        WHERE
            rowid = ?
    '''
    values = (rowid,)
    cursor = conn.execute(sql,values)

    data = cursor.fetchone()

    if data is not None:
        print('-----------------------')
        print('DETALLE DE HAMBURGUESA')
        print()
        print(f'ID: {data[0]}')
        print(f'Nombre: {data[1]}')
        print(f'Precio: {data[2]}')
        print(f'Tamaño: {data[3]}')
        print(f'Ingredientes: {data[4]}')
        print(f'Utima actualizacion: {data[5]}')
        print('-----------------------')
        print()
    else:
        print('La hamburguesa no existe :(')

def create_hamburguers(conn):
    name = input('¿Cual es el nombre de tu hamburguesa?: ')
    price = float(input('¿Cual es el precio de la misma?: '))
    size = input('¿Cual es el tamaño de la presentacion?: ')
    ingredients = input('Escribe los ingredientes que tiene: ')

    sql = '''
        INSERT INTO
        hamburguer (name, size, price, ingredients)
        VALUES (?, ?, ?, ?)
    '''
    values = (name, size, price, ingredients)

    conn.execute(sql, values)
    conn.commit()

    print('Hamburguer created! 🍔')

def get_hamb_name(conn):
    ham_name = input('Ingresa el nombre de la hamburguesa que deseas buscar: ')
    sql = '''
        SELECT 
            rowid, name, price, size, ingredients, timestamp
        FROM
            hamburguer
        WHERE
            name = ?
    '''
    values = (ham_name,)
    cursor = conn.execute(sql,values)

    data=cursor.fetchall()
    if len(data) == 0:
        print('Hamburguesa no existe')
    else:
        for hamburguer in data:
            print('----------------------')
            print('DETALLE DE HAMBURGUESA')
            print()
            print(f'ID: {hamburguer[0]}')
            print(f'Nombre: {hamburguer[1]}')
            print(f'Precio: {hamburguer[2]}')
            print(f'Tamaño: {hamburguer[3]}')
            print(f'Ingredientes: {hamburguer[4]}')
            print(f'Utima actualizacion: {hamburguer[5]}')
            print('-----------------------')
            print()

def update_data(conn):
    rowid = input('Ingresa el ID del hamburguesa que quieres editar: ')
    get_hamburguer(conn,rowid)

    column = input('Ingresa el nombre de la columna que deseas modificar: ')
    new_value = input('Ingresa el nuevo valor de dicha columna: ')

    sql = '''
        
    '''



def handle_user_selection(selection, conn):
    if selection == 1:
        get_hamburguers(conn)
    elif selection == 2:
        get_hamburguer(conn)
    elif selection == 3:
        create_hamburguers(conn)
    elif selection == 4:
        get_hamb_name(conn)
    else:
        update_data(conn)

def main():
    getOut = 'N'
    while getOut == 'N':
        conn = create_or_get_database()
        create_table(conn)
        print('\nBIENVENIDOS A LAS HAMBURGUESAS COVID-KING\n')
        print('Te presentamos el menu de opciones')
        print('1. Ver las hamburguesas disponibles')
        print('2. Ver detalles de una hamburguesa')
        print('3. Agregar nueva hamburguesa')
        print('4. Ver detalles de una hamburguesa por nombre')
        print('5. Actualizar una hamburguesa\n')
        selection = int(input('¿Qué opción eliges? '))
        if validate_user_selection(selection):
            handle_user_selection(selection, conn)
            getOut = input('¿Deseas salir de la app? (S/N) ')
            while getOut != 'S' and getOut != 'N':
                print('La opcion que ingresaste no es valida')
                getOut = input('¿Deseas salir de la app? (S/N) ')
        else:
            print("Tu valor que ingresaste es invalido, sorrynotsorry")

main() 