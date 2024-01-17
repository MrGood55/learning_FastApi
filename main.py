
from fastapi import FastAPI

app = FastAPI(
    # title='Trading App'
)

# Lesson 1
@app.get('/')
def hello():
    return 'Hello, world'

# Lesson 2

fake_users = [  
      {'id': 1,'role': 'admin','name': 'Bob'},
    {'id': 2,'role': 'investor','name': 'John'},
    {'id': 3,'role': 'trader','name': 'Matt'},
    ]


@app.get('/{user_id}')
def get_user(user_id):
    return [user for user in fake_users if user.get('id') == user_id]
