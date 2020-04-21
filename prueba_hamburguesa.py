import sqlite3

def create_or_get_database():
    conn = sqlite3.connect('hamburger.db')
    print("Database connected")
    return conn

def create_tables(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS hamburger (
            name VARCHAR NOT NULL,
            price DOUBLE NOT NULL,
            size VARCHAR NOT NULL,
            ingredients TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    conn.execute(sql)
    print('All the tables has been created succesfully')

def validate_user_selection(selection):
    return isinstance(selection, int) and selection > 0 and selection < 4

def get_hamburgers(conn):
    print()
    print("------------------------------------")
    print("LISTA DE HAMBURGUESAS DISPONIBLES")
    print("------------------------------------")
    print('Nombre\t\t\tPrecio\t\t\tTamaño')
    sql = '''
        SELECT
            name, price, size
        FROM
            hamburger
    '''
    cursor = conn.execute(sql)
    for row in cursor:
        print(f'{row[0]}\t\t\t{row[1]}\t\t\t{row[2]}')
    print("------------------------------------")
    print()

def get_hamburger(conn):
    rowid = input('Ingresa el ID del hamburguesa que quieres visualizar: ')
    sql = '''
        SELECT
            rowid, name, price, size, ingredients, timestamp
        FROM
            hamburger
        WHERE
            rowid = ?
    '''
    values = (rowid,)
    cursor = conn.execute(sql, values)
    for row in cursor:
        print('--------------------------------')
        print('DETALLE DE HAMBURGUESA')
        print()
        print(f'ID: {row[0]}')
        print(f'Nombre: {row[1]}')
        print(f'Precio: {row[2]}')
        print(f'Size: {row[3]}')
        print(f'Ingredientes: {row[4]}')
        print(f'Última actualización: {row[5]}')
        print('------------------------------')
    print()
def create_hamburger(conn):
    name = input('¿Cuál es el nombre de tu hamburguesa?: ')
    price = float(input('¿Cuál es el precio de la misma?: '))
    size = input('¿Cuál es el tamaño de presentación?: ')
    ingredients = input('Escribe los ingredientes que tiene: ')

    # sql = '''
    #     INSERT INTO
    #         hamburger (name, size, price, ingredients)
    #     VALUES (%s, %s, %f, %s)
    # '''.format(name, size, price, ingredients)

    sql = '''
        INSERT INTO
             hamburger (name, size, price, ingredients)
        VALUES (?, ?, ?, ?)
    '''
    values = (name, size, price, ingredients)

    conn.execute(sql, values)
    conn.commit()

    print('Hamburger created! 🍔')


def handle_user_selection(selection, conn):
    if selection == 1:
        get_hamburgers(conn)
    if selection == 2:
        get_hamburger(conn)
    else:
        create_hamburger(conn)

def main():
    conn = create_or_get_database()
    create_tables(conn)
    print('BIENVENIDO A LAS HAMBURGUESAS COVID-KING\n')
    print('Te presentamos el menú de opciones:\n')
    print('1. Ver las hamburguesas disponibles')
    print('2. Ver detalle de una hamburgesa')
    print('3. Agregar nueva hamburguesa\n')
    selection = int(input('¿Qué opción eliges?: '))
    if validate_user_selection(selection):
        handle_user_selection(selection, conn)
    else:
        print('Tu valor que ingresaste es inválido, sorrynotsorry')

main()