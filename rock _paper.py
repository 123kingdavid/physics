import random 
import storage  

USER_WIN = 1
COMPUTER_WIN = 3 
DRAW = 2

def get_user_choice(prompt=''):
    while True:
        try:
              user_choice = int(input(prompt)) 
              if user_choice in [1,2,3]:
                   return user_choice 
              raise ValueError
        except ValueError:
              print('only numbers 1- 3 allowed') 
        

def display_instruction():
     print('choose one.')     
     print('1. rock') 
     print('2. paper') 
     print('3. scissors') 

def get_computer_choice():
     return random.randint(1,3) 

def  determine_winner(user_choice,computer_choice):
     if user_choice == computer_choice:
          return DRAW  
     elif (user_choice == 1 and computer_choice == 3)or \
          (user_choice == 2 and computer_choice ==1)or \
          (user_choice == 3 and computer_choice ==2):
        return USER_WIN
     else:
          return COMPUTER_WIN  

def display_winner(win):
     if win==USER_WIN:
          print("user win")  
     elif win == COMPUTER_WIN:
          print('computer win') 
     elif win == DRAW:
          print("it is a draw")  

def add_score(win):
     if win == USER_WIN:
          return 2
     else:
          return 0   


def create_user(user_name): 
     return{'username': user_name, 'score':0} 

def sign_up():
     user_name = input("insert a user name") .strip() 
     return create_user(user_name) 

def sign_in(users,username):
     user = users.get(username)
     if user: 
          return user 

def login(): 
     users = storage.get('user.json')
     print('1.sign up') 
     print('2 sign in')
     print('3. exit page') 
     response = int(input('>>> ')) 
     if response == 1:
          user = sign_up() 
          users = save_user(users, user) 
          storage.store('users.json',users) 
          return user  
     elif response == 2:
          username = input('username: ')
          user = sign_in(users,username) 
          return user              

def save_user(users,user):
     key = user['username']  
     users[key] = user 
     return users          
             
def main(): 
     users = storage.get("users.json")
     user = None
     print("welcome to rock paper and scissors!")

     while user == None:
          user = login() 
          if not user:
               print('invalid username') 
     display_instruction() 
     while True:     
      user_choice = get_user_choice('choice: ') 
      computer_choice = get_computer_choice() 
      result = determine_winner(user_choice, computer_choice)
      user['score'] += add_score(result) 
      save_user(users,user) 
      storage.store('users.json,', user )
      display_winner(result) 
      print('score: ', user['score']) 
      
if __name__  == "__main__": 
     while True:
      main()      
    


    
        
    

          
    
    
    

            
                  