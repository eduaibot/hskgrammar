# database.py
import sqlite3
import json
import hashlib

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def init_db():
    conn = sqlite3.connect('hsk_master.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS history (username TEXT, type TEXT, content TEXT, score TEXT, date DATETIME DEFAULT CURRENT_TIMESTAMP)')
    c.execute('CREATE TABLE IF NOT EXISTS exam_sessions (username TEXT PRIMARY KEY, exam_json TEXT, answers_json TEXT, time_left INTEGER)')
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect('hsk_master.db')
    hashed = hash_password(password)
    try:
        conn.execute("INSERT INTO users VALUES (?, ?)", (username, hashed))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False # Username đã tồn tại
    finally:
        conn.close()

def check_user(username, password):
    conn = sqlite3.connect('hsk_master.db')
    hashed = hash_password(password)
    user = conn.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed)).fetchone()
    conn.close()
    return user is not None

def save_history(user, log_type, content, score):
    conn = sqlite3.connect('hsk_master.db')
    conn.execute("INSERT INTO history (username, type, content, score) VALUES (?, ?, ?, ?)", 
                 (user, log_type, content, score))
    conn.commit()
    conn.close()

def save_exam_progress(user, exam_json, answers, time_left):
    conn = sqlite3.connect('hsk_master.db')
    conn.execute('INSERT OR REPLACE INTO exam_sessions VALUES (?, ?, ?, ?)', 
                 (user, json.dumps(exam_json), json.dumps(answers), int(time_left)))
    conn.commit()
    conn.close()

def get_unfinished_exam(user):
    conn = sqlite3.connect('hsk_master.db')
    data = conn.execute('SELECT exam_json, answers_json, time_left FROM exam_sessions WHERE username = ?', (user,)).fetchone()
    conn.close()
    if data:
        return {"exam": json.loads(data[0]), "answers": json.loads(data[1]), "time_left": data[2]}
    return None

def clear_unfinished_exam(user):
    conn = sqlite3.connect('hsk_master.db')
    conn.execute('DELETE FROM exam_sessions WHERE username = ?', (user,))
    conn.commit()
    conn.close()

def get_history(user):
    conn = sqlite3.connect('hsk_master.db')
    data = conn.execute('SELECT type, content, score, date FROM history WHERE username = ? ORDER BY date DESC', (user,)).fetchall()
    conn.close()
    return data