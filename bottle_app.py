from bottle import default_app, route, get, post, template, request, redirect
import sqlite3

connection = sqlite3.connect("football_players_list.db")

@route('/')
def hello_world():
    return 'Hello from janardhan!'

@route('/hi')
def hi_world():
    return 'Hi from janardhan!'

@route('/bye')
def bye_world():
    return 'Bye from janardhan!'

@route('/list')
def get_list():
    cursor = connection.cursor()
    rows = cursor.execute("select id, description from list")
    rows = list(rows)
    rows = [ {'id':row[0] ,'desc':row[1]} for row in rows ]
    return template("football_players_list.tpl", name="janardhan", football_players_list=rows)

@get('/add')
def get_add():
    return template("add_item.tpl")

@post('/add')
def post_add():
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"insert into list (description) values ('{description}')")
    connection.commit()
    redirect('/list')

@route("/delete/<id>")
def get_delete(id):
    cursor = connection.cursor()
    cursor.execute(f"delete from list where id={id}")
    connection.commit()
    redirect('/list')

@get("/edit/<id>")
def get_edit(id):
    cursor = connection.cursor()
    items = cursor.execute(f"select description from list where id={id}")
    items = list(items)
    if len(items) != 1:
        redirect('/list')
    description = items[0][0]
    return template("edit_item.tpl", id=id, description=description)

@post("/edit/<id>")
def post_edit(id):
    description = request.forms.get("description")
    cursor = connection.cursor()
    cursor.execute(f"update list set description='{description}' where id={id}")
    connection.commit()
    redirect('/list')


application = default_app()