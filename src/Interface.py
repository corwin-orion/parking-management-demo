class Interface:
    def __init__(self):
        self.users = ['Administrator']
        self.currentUser = None
        self.state = 'login'
    
    def update(self):
        if self.currentUser == None:
            self.state = 'login'
        
    def display(self):
        if self.state == 'login':
            print("Welcome to Parking Management Login.")
            # TODO: Take username and password to log in
