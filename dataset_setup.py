import dataset

db = dataset.connect('sqlite:///football_players_list.db')

try:
    db['list'].drop()
except:
    pass

db.begin()
try:
    table = db['list']
    items = [
        { "description": 'Messi' },
        { "description": 'Ronaldo' },
        { "description": 'Mbappe' },
        { "description": 'Neymer' }

        ]
    table.insert_many(items)
    db.commit()
except:
    db.rollback()