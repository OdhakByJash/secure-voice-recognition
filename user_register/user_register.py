import sounddevice as sd
from mysql.connector import connect
from dotenv import load_dotenv
import os
def input_audio():
    sampling_frequency = 48000
    time_period = 7
    recording = sd.rec(
        int(sampling_frequency*time_period),
        samplerate=sampling_frequency,
        channels=1
    )
    sd.wait()
    return [sampling_frequency,time_period,recording]
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
        cursor.execute("CREATE TABLE IF NOT EXISTS user (first_name VARCHAR(50), last_name VARCHAR(50), username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), audio LONGBLOB);")
        audio = input_audio()[2]
        audio_array = audio.tobytes()
        cursor.execute(f"INSERT INTO user VALUES ('{first_name}','{last_name}','{username}','{email}','{password}','{audio_array}')")
    except Exception as e:
        return str(e)
print(register_user("jash","upadhyay","bitsbuild","jashupadhyay.java@gmail.com","password"))