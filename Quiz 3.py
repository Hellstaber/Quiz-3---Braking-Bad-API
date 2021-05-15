import requests
import json
import sqlite3

conn = sqlite3.connect('bb_db.sqlite')
c = conn.cursor()

# ამ კოდის დახმარებით ვქმნით ჩვენ ცხრილს მონაცემთა ბაზებისთვის

c.execute('''CREATE TABLE IF NOT EXISTS bb
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Characters VARCHAR(25),
            Nickname INTEGER,
            Birthday INTEGER
            )''')

resp = requests.get('https://www.breakingbadapi.com/api/characters')

r = resp.json()

print(resp)
print(resp.status_code)
print(resp.headers)
print(resp.text)
print(resp.content)
print(resp.json())

res = json.loads(resp.text)
with open('bb.json', 'w') as f:
    json.dump(res, f, indent=4)

print(json.dumps(res, indent=4))

# აღნიშნული კოდით მონაცემთა ბაზებს გადავეცით თუ რა ინფორმაცია უნდა წამოიღოს api-დან
all_row = []
for each in r:
    Characters = each['name']
    Nickname = each['nickname']
    Birthday = each['birthday']
    row = (Characters, Nickname, Birthday)
    all_row.append(row)

print(all_row)

c.executemany('INSERT INTO bb (Characters, Nickname, Birthday) VALUES (?, ?, ?)', all_row)

conn.commit()
conn.close()
