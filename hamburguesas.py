import sqlite3

def create_or_get_database():
    conn = sqlite3.connect('hamburger.db')
    print ("DATA BASE CREATED")
    return conn

def create_tables(conn):
    sql = '''
    CREATE TABLE IF NOT EXISTS hamburger(
        name VARCHAR NOT NULL,
        price DOUBLE NOT NULL,
        size VARCHAR NOT NULL,
        ingredients TEXT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP

    )    
'''
    conn.execute(sql)
    print ('all the table has been create succesful')

def validate_user_selection(selection):
    return isinstance(selection , int) and selection > 0 and selection < 4

def get_hamburguers(conn):
    print()
    print("_________________________________________")
    print ("LISTA DE HAMBURGESAS DISPONIBLES")
    print("_________________________________________")
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
    print("_____________________________")
    print()    

def get_hamburger(conn):
    rowid = input('INGRESA ID DE LA HAMBURGUESA'  )
    sql = '''
        SELECT
           rowid , name , price , size , ingredients , timestamp
        FROM
           hamburger
        WHERE
           rowid = ?      
    '''
    values = (rowid,)
    cursor = conn.execute(sql, values)
    for row in cursor:
        print('_____________________________________')
        print('DETALLE DE HAMBURGUESA')
        print()
        print(f'ID:{row[0]}')
        print(f'Nombre:{row[1]}')
        print(f'Precio:{row[2]}')
        print(f'Size:{row[3]}')
        print(f'Ingredients:{row[4]}')
        print(f'ULTIMA ACTUALIZACION:{row[5]}')
        print ('_________________________________________')
        print()

def create_hamburguer(conn):
    name = input('nombre de tu hamburguesa  '  )
    price = float (input ('cual es el precio '  ))
    size = input ('ingresa el tamaño  ' )
    ingredients = input('escribe tus ingredientes  '  )

   # sql = '''
    # INSERT INTO
     #     hamburguer(name,price,size,ingredients)
      #  VALUES(%s,%s,%f,%s)
    #'''.format(name,size,price,ingredients)

    sql = '''
     INSERT INTO
         hamburger(name,price,size,ingredients)
       VALUES(?,?,?,?)
    '''
    values = (name,size,price,ingredients)
    conn.execute(sql,values)
    conn.commit()

    print('Hamburger created! 🍔')

def handle_user_selection(selection , conn):
    if selection == 1:
        get_hamburguers(conn)
    if selection == 2:
        get_hamburguers(conn)
    else: 
        create_hamburguer(conn) 

def main():
    getOut = 'N'
    while getOut == 'N':

      conn = create_or_get_database()
      create_tables(conn)
      print('BIENVENIDO A HAMBURGUESAS EL PARIENTE\n')
      print('MENU DE OPCIONES\n')
      print('1 Ver hamburguesas disponibles')
      print('2 agregar hamburguesa\n')
      print('3. Agregar nueva hamburguesa\n')
      selection = int (input('Que opcion eliges?'  ))
      if validate_user_selection(selection):
          handle_user_selection(selection, conn)
      else :
          print('ingresaste valor invalido')  
main()          