import sqlite3  # SQLite ডাটাবেজ লাইব্রেরি ইম্পোর্ট করা হচ্ছে
import hashlib  # পাসওয়ার্ড হ্যাশ করার জন্য hashlib ইম্পোর্ট করা হচ্ছে

# ডাটাবেজ ফাইলে কানেকশন তৈরি করা হচ্ছে
conn = sqlite3.connect('users.db')
cursor = conn.cursor()  # ডাটাবেজে কমান্ড চালানোর জন্য cursor তৈরি

# যদি 'users' নামের টেবিল না থাকে তাহলে তা তৈরি করা হচ্ছে
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    password TEXT
)
''')
conn.commit()  # ডাটাবেজে পরিবর্তন সংরক্ষণ করা হচ্ছে

# পাসওয়ার্ডকে নিরাপদ করার জন্য হ্যাশ ফাংশন
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ইউজারদের ইনপুট ধরে রাখার জন্য একটা ডিকশনারি তৈরি করা হচ্ছে
user_data = {}

# ইউজারদের ইনপুট নেওয়া হচ্ছে যতক্ষণ না তারা 'exit' টাইপ করে
while True:
    name = input("আপনার নাম দিন (বা 'exit'): ")
    if name.lower() == 'exit':
        break  # exit টাইপ করলে লুপ থেকে বেরিয়ে যাবে
    email = input("আপনার ইমেইল দিন: ")
    password = input("পাসওয়ার্ড দিন: ")

    hashed = hash_password(password)  # পাসওয়ার্ড হ্যাশ করা হচ্ছে
    user_data[name] = (email, hashed)  # ডিকশনারিতে ডেটা সেভ করা হচ্ছে

# ইউজার ডেটা ডাটাবেজে ইনসার্ট করার ফাংশন
def insert_users(data_dict):
    for name, (email, hashed_pw) in data_dict.items():
        cursor.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_pw))
    conn.commit()  # ইনসার্ট করার পর ডেটা সংরক্ষণ

# লগইন ফাংশন যেখানে ইউজার ইমেইল ও পাসওয়ার্ড দিয়ে লগইন করবে
def login():
    email = input("আপনার ইমেইল দিন: ")
    password = input("আপনার পাসওয়ার্ড দিন: ")
    hashed_input = hash_password(password)  # ইউজারের ইনপুট হ্যাশ করা হচ্ছে

    # ডাটাবেজ থেকে মিল খুঁজে দেখা হচ্ছে
    cursor.execute("SELECT name FROM users WHERE email = ? AND password = ?", (email, hashed_input))
    result = cursor.fetchone()

    # লগইন সফল হলে স্বাগত জানানো হচ্ছে, নাহলে ভুল বার্তা
    if result:
        print(f"স্বাগতম, {result[0]}! লগইন সফল ✅")
    else:
        print("দুঃখিত, ইমেইল বা পাসওয়ার্ড ভুল ❌")

# সব ইউজার ইনসার্ট করার পর লগইন ফাংশন কল করা হচ্ছে
insert_users(user_data)
login()
