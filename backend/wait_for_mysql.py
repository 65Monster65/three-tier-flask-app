import time
import pymysql
import sys

def wait_for_mysql():
    print("\n🔵 Waiting for MySQL to be ready...")
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        attempt += 1
        try:
            conn = pymysql.connect(
                host="mysql",
                user="flaskuser",
                password="flaskpassword",
                database="flaskdb",
                connect_timeout=5
            )
            conn.close()
            print(f"✅ MySQL is ready (attempt {attempt}/{max_attempts})")
            return True
            
        except pymysql.Error as e:
            print(f"⏳ Attempt {attempt}/{max_attempts}: {str(e)}")
            time.sleep(2)
    
    print("🔴 Failed to connect to MySQL after maximum attempts")
    return False

if __name__ == '__main__':
    wait_for_mysql()