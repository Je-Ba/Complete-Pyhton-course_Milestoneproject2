from utils import database

user_options={
    'a':database.add_book,
    'l':database.list_all_books,
    'r':database.mark_read,
    'd':database.delete_books,
    }

User_choice = input('Select operation (a,l,r or d)')

while User_choice != 'q':
    if User_choice in user_options:
        select_function = user_options[User_choice]
        select_function()
    else:
        print('Unknown command. Please try again.')
    User_choice = input('Select operation (a,l,r or d)')

