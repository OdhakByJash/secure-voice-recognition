from mysql.connector import connect
import os
from dotenv import load_dotenv
from audio_input.input import input_audio
def register_user(first_name,last_name,email,password):
    try:
        load_dotenv()
        db = connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE')
        )
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name VARCHAR(50), last_name VARCHAR(50), username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), audio LONGBLOB);")
        audio_array = input_audio()
        cursor.execute("")
    except Exception as e:
        return str(e)
register_user()