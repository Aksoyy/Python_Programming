from flask import Flask

app = Flask(__name__)

entries = [
        {
                "username":"Hamdi",
                "entry":"Bisey"
        },
        {
                "username":"Gunay",
                "entry":"Selam"
        },
        {
                "username":"Betty",
                "entry":"Unicorn"
        }
]

@app.route('/')
def guestbook():
    """
    <strong>Hamdi</strong>
    <p>Bisey</p>
    """

    title = "<h1>GuestBook</h1>"
    form = "<form>"
    form += "<tr></tr>"
    form += "<p><input type='text' name='username'></p>"
    form += "<p><textarea name='entry'></textarea></p>"

    form += "</form>"

    body = "<ul>"
    for entry in entries:
        body += "<li>
        body += f'<strong>{entry["username"]}<strong>'
        body += f'<p>{entry["entry"]}</p>
        body += "</li>"
    body += "</ul>"


return f'{title}{form}{body}'

@app.route("/add/", methods=["POST"])
def add_to_guestbook(text)
    global entries
    entries.append({
        "username":"test",
        "entry":"entry"
    })