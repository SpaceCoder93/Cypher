import os
from supabase import create_client, Client
import gotrue.errors
import threading
from dotenv import load_dotenv

class Authentication(threading.Thread):
    def __init__(self):
        super().__init__()
        load_dotenv()
        __url = str(os.getenv("SUPABASE_URL"))
        __key = str(os.getenv("SUPABASE_KEY"))
        self.supabase = Client(__url, __key)

    def signin(self, username, password):
        try:
            data = self.supabase.auth.sign_in_with_password({"email": username, "password": password})
            data = dict(data)
            data = data['user']
            data = dict(data)
            f = open('a.txt', 'w')
            f.writelines(str(data))
            print(data['id'])
        except gotrue.errors.AuthApiError as e:
            if str(e) == 'Invalid login credentials':
                print("Wrong Password")

    def signup(self, username, password):
        data = self.supabase.auth.sign_up({"email": username, "password": password})
        print(data)

    def signout(self):
        res = self.supabase.auth.sign_out()

Authentication().signin('virajpardkar@gmail.com', '123456')
#Authentication().signup('virajpardkar@gmail.com', '123456')
#Authentication().signout()