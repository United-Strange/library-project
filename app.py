from librery_oop import Library
from flask import Flask, jsonify

lib = Library("library.db")
app = Flask(__name__)

@app.route('/books')
def get_books_list():
    return jsonify(lib.list_book())

if __name__ == '__main__':
    app.run()