import pymysql

# INSERTA LAS ESPECIFICACIONES DE TU BASE DE DATOS EN LA PARTE DE ABAJO
def get_connection():
    return pymysql.connect(
        host='YOUR HOST',
        user='YOUR ROOT',
        password='YOUR PASSWORD',
        db='YOUR DATABASE',
    )