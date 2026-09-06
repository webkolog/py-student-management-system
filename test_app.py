import os
import mysql.connector as mysql

def test_database_connection_and_table_creation():
    # Environment variable'dan host bilgisini al
    db_host = os.getenv("DB_HOST", "localhost")
    db_user = os.getenv("DB_USER", "root")
    db_pass = os.getenv("DB_PASSWORD", "")

    # 1. Veritabanı bağlantısı ve oluşturma
    conn = mysql.connect(host=db_host, user=db_user, password=db_pass)
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_student_db")
    cursor.execute("USE test_student_db")

    # 2. Tablo oluşturma
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            class VARCHAR(20),
            roll_no VARCHAR(20) UNIQUE,
            marks INT
        )
    """)
    conn.commit()

    # 3. Veri ekleme testi
    sql = "INSERT INTO students (name, class, roll_no, marks) VALUES (%s, %s, %s, %s)"
    val = ("Ali Candan", "12th", "103", 95)
    cursor.execute(sql, val)
    conn.commit()

    # 4. Veri okuma doğrulama
    cursor.execute("SELECT * FROM students WHERE roll_no = %s", ("103",))
    record = cursor.fetchone()
    
    assert record is not None
    assert record[1] == "Ali Candan"
    assert record[3] == "103"
    assert record[4] == 95

    # Temizlik
    cursor.execute("DROP DATABASE test_student_db")
    cursor.close()
    conn.close()
