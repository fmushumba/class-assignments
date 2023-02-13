from flask import Flask,request
application=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy


application.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data2.db'
db=SQLAlchemy(application)
application.app_context().push()

class Book(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    book_name=db.Column(db.String(80), nullable=False)
    author= db.Column(db.String(80), nullable=False)
    publisher=db.Column(db.String(80),nullable=False)

    
    def __repr__(self):
        return f"{self.book_name} written by{self.author}"
@application.route('/')
def index():
    return 'Hello'
    
@application.route('/books')
def get_books():
    books=Book.query.all()
    output=[]
    for book in books:
        book_data={'book name':book.book_name,'author':book.author,'publisher':book.publisher}
        output.append(book_data)
    return {'books':output}

@application.route('/books/<id>')
def get_books(id):
    book=Book.query.get_or_404(id)
    return {'book name':book.book_name,'author':book.author,'publisher':book.publisher}

@application.route('/books',methods=['POST'])
def add_book():
    book=Book(book_name=request.json['book name'],author=request.json['author'])
    db.session.add(book)
    db.session.commit()
@application.route('/books',methods=['DELETE'])
def delete_book(id):
    book=Book.query.get(id)
    db.session.delete(book)
    db.session.commit()