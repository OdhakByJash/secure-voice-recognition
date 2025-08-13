from mysql.connector import connect
import os
from dotenv import load_dotenv
def register_user():
    load_dotenv()
    db = connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD')
    )
    print(db)
register_user()