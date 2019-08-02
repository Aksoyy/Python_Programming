from flask import Flask
from flask import request, redirect
from redis import Redis

app = Flask(__name__)
redis = Redis()

def get_entries():
    global redis
    data = redis.lrange('entries', 0, -1)
    result = []
    for item in data:
        try:
            username, entry = item.decode('utf-8').split('|')
        except ValueError:
            continue
        result.append({'username': username, 'entry': entry})
    return result


def get_form():
    form = '<form action="/add/" method="post" style="background: lightgrey; border: 1px solid black; padding: 10px"><table>'
    form += '<tr><td>username:</td><td><input style="width: 100%" type="text" name="username"></td></tr>'
    form += '<tr><td>entry:</td><td><textarea name=\'entry\'></textarea></td></tr>'
    form += '<tr><td colspan=2><input style="float: right"type="submit"></td></tr>'
    form += '</table></form>'
    return form
 

@app.route('/')
def guestbook():
    title = '<h1>Guestbook</h1>'
    form = get_form()
    body = '<ul>'
    for entry in get_entries():
        body += '<li>'
        body += f'<strong>{entry["username"]}</strong>:'
        body += f'<p>{entry["entry"]}</p>'
        body += '</li>'
    body += '</ul>'
    return f'{title}{form}{body}'

@app.route('/add/', methods=['POST'])
def add():    
    global entries
    data = f'{request.form["username"]}|{request.form["entry"]}'
    redis.lpush('entries', data)
    return redirect('/')

@app.route('/hi/')
def hi_world():
    return 'Hi World!'

if __name__ == '__main__':
    app.run()

