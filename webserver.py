from flask import Flask, request
from resources import Entry
from EntryManager import EntryManager

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/test")
def hello_test():
    return "<p>Hello, Test!</p>"


@app.route("/api/entries/")
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    result = []
    for entry in entry_manager.entries:
        result.append(entry.json())
    return result


@app.route("/api/save_entries/", methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    result = request.get_json()
    for value in result:
        entry = Entry.from_json(value)
        entry_manager.entries.append(entry)
    entry_manager.save()
    return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


FOLDER = '/Users/Yauheniya_Hrebianko/Documents/Project'

entry_manager = EntryManager(FOLDER)
entry_manager.load()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)