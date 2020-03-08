import sqlite3
from employee import Employee

#print (dir(sqlite3))
conn =sqlite3.connect(':memory:')

c =conn.cursor()

c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})
#c.execute("""CREATE TABLE employees(first text,last text,pay integer)""")
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)


#c.execute("insert into employees values('shivam','puri',100000)")


#c.execute("insert into employees values(?,?,?)",(emp_1.first,emp_1.last,emp_1.pay))       #one way 
#conn.commit()

#c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay': emp_2.pay}) #another way
#conn.commit()

#c.execute("select * from employees where last ='puri'")
#c.fetchmany(5)
#print c.fetchall()

#c.execute("select * from employees where last=:ls")
#print c.fetchall()

#conn.commit()



insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print emps

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print emps

conn.close()
