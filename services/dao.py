import sqlite3


def add_new_user(firstname, lastname, email, password):
    con = sqlite3.connect('pen')
    cur = con.cursor()
    sql = "INSERT INTO users (firstname,lastname,email,password) VALUES (?,?,?,?)"
    val = (firstname, lastname, email, password)
    cur.execute(sql, val)
    con.commit()
    print(cur.rowcount, "user added.")
    # for row in cur.execute('SELECT * FROM users'):
    #     print(row)
    con.close()


def fetch_user(email, password):
    con = sqlite3.connect('pen')
    cur = con.cursor()
    sql = "SELECT * FROM users WHERE email=?"
    val = (email,)
    cur.execute(sql, val)
    user = cur.fetchone()
    con.close()

    if user is None:
        print('wrong email!')
        return None

    if user[4] == password:
        return user
    print('passwords didnt match!')
    return None
