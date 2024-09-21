import mysql.connector
from datetime import datetime


def get_products(cursor):
    cursor.execute('''SELECT products.product_id,
    products.name,
    products.uom_id,
    products.price_per_unit,
    uom.uom_name
    FROM products
    INNER JOIN uom
    ON uom.uom_id = products.uom_id;
    ''')

    # print(cursor.fetchall())
    list = []
    for record in cursor:
        product_id, name, uom_id, price_per_unit, uom_name = record
        list.append({'product_id' : product_id,
                     'name' : name,
                     "uom_id" : uom_id,
                     "price_per_unit" : price_per_unit,
                     'uom_name' : uom_name
        })

    return list


def print_products(list):
    for i in list:
        print(i)


def insert_new_product(cursor):
    product = {
        'name': 'phone',
        'uom_id': '1',
        'price_per_unit': '25000'
    }
    query = ("INSERT INTO products (name, uom_id, price_per_unit) "
             "VALUES (%s, %s, %s)")
    data = (product['name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)


def delete_product(cursor, id):
    cursor.execute("delete from products where product_id=" + str(id))


def create_connection():
    config = {
        'user': 'root',
        'password': 'brijesh',
        'host': '127.0.0.1',
        'database': 'grocery_store'
    }

    # Establish the connection
    try:
        cnx = mysql.connector.connect(**config)
        print("Connection successful!")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def main():
    cnx = create_connection()
    if cnx is None:
        print("Failed to connect to the database.")
        return

    try:
        cursor = cnx.cursor()

        # Insert a new product
        # insert_new_product(cursor)

        delete_product(cursor, 2)

        # Commit the transaction
        cnx.commit()

        # Fetch and print the products
        product_list = get_products(cursor)
        print_products(product_list)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        if cnx.is_connected():
            cnx.close()
            print("Connection closed.")


if __name__ == '__main__':
    start_time = datetime.now()
    print(f"Program started at: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

    main()

    end_time = datetime.now()
    print(f"Program ended at: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time}")