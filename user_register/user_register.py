import sounddevice as sd
from mysql.connector import connect
from dotenv import load_dotenv
import os
def register_user(first_name,last_name,username,email,password):
    try:
        load_dotenv()
        db = connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE')
        )
        cursor = db.cursor()
        cursor.execute("""
                       CREATE TABLE IF NOT EXISTS user(
                       first_name VARCHAR(50) NOT NULL, 
                       last_name VARCHAR(50) NOT NULL, 
                       username VARCHAR(50), 
                       email VARCHAR(50) NOT NULL, 
                       password VARCHAR(50) NOT NULL, 
                       audio VARBINARY(MAX) NOT NULL, 
                       UNIQUE(email),
                       PRIMARY KEY (username)
                       );
                       """)
        audio = "placeholder"
        cursor.execute(f"""
                       INSERT INTO user VALUES (
                       '{first_name}',
                       '{last_name}',
                       '{username}',
                       '{email}',
                       '{password}',
                       '{audio}'
                       );
                       """)
    except Exception as e:
        return str(e)
print(register_user("jash","upadhyay","bitsbuild","jashupadhyay.java@gmail.com","password"))