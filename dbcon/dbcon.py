import sqlite3


class UserDB:
    def __init__(self):
        self.conn = sqlite3.connect("mydatabase.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
        """)
        self.conn.commit()

    def add_user(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        self.cursor.execute(
            "INSERT INTO users (name, age) VALUES (?, ?)",
            (name, age)
        )
        self.conn.commit()
        print("User added successfully")

    def search_user(self):
        name = input("Enter name to search: ")
        self.cursor.execute(
            "SELECT * FROM users WHERE name = ?",
            (name,)
        )
        rows = self.cursor.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("User not found")

    def display_users(self):
        self.cursor.execute("SELECT * FROM users")
        rows = self.cursor.fetchall()
        print("All users:")
        for row in rows:
            print(row)

    def delete_user(self):
        user_id = int(input("Enter user ID to delete: "))
        self.cursor.execute(
            "DELETE FROM users WHERE id = ?",
            (user_id,)
        )
        self.conn.commit()
        print("User deleted")

    def close(self):
        self.conn.close()

db = UserDB()

while True:
    print("\nMENU")
    print("1. Add User")
    print("2. Search User")
    print("3. Display All Users")
    print("4. Delete User")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        db.add_user()
    elif choice == "2":
        db.search_user()
    elif choice == "3":
        db.display_users()
    elif choice == "4":
        db.delete_user()
    elif choice == "5":
        db.close()
        print("Exiting program")
        break
    else:
        print("Invalid choice")
