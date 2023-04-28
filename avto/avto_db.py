import sqlite3

connection = sqlite3.connect("avto.db")
cursor = connection.cursor()


cursor.execute("""

    create table if not exists avto(
    
    id integer primary key ,
    make varchar ,
    model varchar ,
    color varchar ,
    price float  
    )
""")

add_avto = """
     insert into avto (make,model,color,price) values (? , ? , ?,?)


    """




avtolar = cursor.execute("""
    
        select * from avto 
    
    """).fetchall()


def commit(func):
    def wrapper(*args,**kwargs):
        responce = func(*args,**kwargs)
        connection.commit()
        return responce
    return wrapper