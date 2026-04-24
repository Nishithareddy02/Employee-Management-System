import sqlite3
def create_connection():
    return sqlite3.connect("employees.db")
def create_table():
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        salary REAL
        )
        """)
    conn.commit()
    conn.close()
def add_employee():
    name=input("Enter Name:")
    age=int(input("Enter Age:"))
    department=input("Enter Department:")
    salary=float(input("Enter Salary:"))
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("INSERT INTO employees(name,age,department,salary)VALUES(?,?,?,?)",(name,age,department,salary))
    conn.commit()
    conn.close()
    print("Employee added successfully!")
def view_employees():
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows=cursor.fetchall()
    print("\n---Employee List---")
    for row in rows:
        print(row)
    conn.close()
def search_employee():
    emp_id=int(input("Enter Employee ID:"))
    conn=create_connection()
    cursor=conn.curosr()
    cursor.execute("SELECT * FROM employees WHERE id=?",(emp_id,))
    row =cursor.fetchone()
    if row:
        print("Employee Found:",row)
    else:
        print("Employee not found!")
    conn.close()
def update_employee():
    emp_id=int(input("Enter Employee ID:"))
    name=input("Enter new name:")
    age=int(input("Enter new age:"))
    department=input("Enter new department:")
    salary=float(input("Enter new salary:"))
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("""
    UPDATE employees
    SET name=?,age=?,department=?,salary=?
    WHERE id=?
     """,(name,age,department,salary,emp_id))
    conn.commit()
    if cursor.rowcount==0:
        print("Employee not found!")
    else:
        print("Employee updated successfully!")
    conn.close()
def delete_employee():
    emp_id=int(input("Enter Employee ID:"))
    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM employees WHERE id=?",(emp_id,))
    conn.commit()
    if cursor.rowcount==0:
        print("Employee not found!")
    else:
        print("Employee deleted successfully!")
    conn.close()
def main():
    create_table()
    while True:
        print("\n===Employee Management System===")
        print("1.Add Employee")
        print("2.view Employees")
        print("3.serach Employee")
        print("4.update Employee")
        print("5.Delete Employee")
        print("6.Exit")
        choice =input("Enter your choice:")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Exiting...")
            break
    else:
     print("Invalid choice!")

if __name__ == "__main__":
  main()


   



                   
                








