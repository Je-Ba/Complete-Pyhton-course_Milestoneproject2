"""
Database with list of books
"""


books = [{'name': 'Harry Potter 1' ,'author':'JKR', 'read':False},{'name': 'Harry Potter 2' ,'author':'JKR', 'read':True}]


def add_book():
    name = input('name of book')
    auther = input('auther of book')
    books.append({'name':name,'author':auther, 'read':False})
    return None


def list_all_books():
    for name in range(len(books)):
        print(f"Name:{books[name]['name']}, Author:{books[name]['author']},readbook:{books[name]['read']}")


def delete_books():
    global books
    name=input('what book shall be deleted')
    books = [book for book in books if book['name'] != name]

def mark_read():
    name = input('what book have you read?')
    for book in books:
        if book['name']==name:
            book['read']=True