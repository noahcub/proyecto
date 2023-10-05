import sqlite3

con = sqlite3.connect(":memory:")     # path especial que proporciona la creación de una BD temporal en memoria RAM
cur = con.cursor()

cur.execute("create table lang (name, first_appeared)")

# Este es el estilo qmark:
cur.execute("insert into lang values (?, ?)", ("C", 1972))

# El estulo qmark se usa con executemany():
lang_list = [
    ("Fortran", 1957),
    ("Python", 1991),
    ("Go", 2009),
]

cur.executemany("insert into lang values (?, ?)", lang_list)

# Y este es el estilo nombrado:
cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
print(cur.fetchall())
 

con.close()