users = {
    'username':'vale11018',
    'email': "Valeria@gmail.com",
    'role': 'user',  
    'session': {
        'token': True
    }
}

def session_required(function):
    
    def wrapper(*args, **kwargs):
        
        user = args[0] if args else kwargs
        session = user['session']

        if session['token']:
            if 'home' in str(function):
                function(*args)
            elif 'user_function' in str(function) and user['role']=='user':
                function(*args)
            elif 'superuserFunction' in str(function) and user['role']=='superuser':
                function(*args)
            elif  'admin_function' in str(function) and user['role']=='admin':
                function(*args)
            else:
                print('Unauthorized access')
        else:
            loggin()
    return wrapper
    



def loggin():
    print("Entre al login")
    pass


@session_required
def home(user):
    print("Entre al home")
    pass
@session_required
def user_function(user):
    user_name = user['username']
    print("Hello, ",user_name,"! This is the user-level area.\nYou can change your name and edit your profile.")
    pass

@session_required
def admin_function(user):
    print("Welcome, Admin! This is the admin-level area.\nYou have access to user management and can perform administrative tasks.")
    pass


@session_required
def superuserFunction(user):
    print("Hello, Super User! This is the superuser-level area.\nYou have full control over the system and can perform any action.")
    pass

#home(users)
#user_function(users)
#admin_function(users)
superuserFunction(users)

