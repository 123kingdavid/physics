# file = open('test.txt', 'a') 
# file.write ('my first file') 
# file.write('my first time')
# file.close()
# reader = open('test.txt','r') 
# print(reader.read()) 
import json

def write_file(file_name, content):
    file = open(file_name, 'w') 
    total = file.write (content) 
    file.close() 
    return total 

def read_file(file_name): 
    try: 
        file = open(file_name, 'r') 
        content = file.read() 
        file.close()  
        return content 
    except FileNotFoundError: 
        return '{}'
def store(file_name,data):
    text = json.dumps(data) 
    write_file(file_name ,text) 

def get(file_name):
    text = read_file(file_name) 
    return json.loads (text) 
