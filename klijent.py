
import requests
import jwt
 
login = input("Do you have a token? (y/n)")
if(login == 'y'):
        token = input("Enter your token: ")
        try:
                
                print("Hello {}".format(token['number']))

        except:
                print("Something is wrong with token")
        korisnici = input("Unesi ime korisnika: ")
        r = requests.get("http://127.0.0.1:8079/", params={"name":korisnici,'token': token})
        print("Request method: GET, \nResponse status_code: {}, Response data(Prezime korisnika): {}".format(r.status_code, r.text))

elif(login=='n'):
    number = input("Enter your number: ")
    password = input("Enter your password: ")
    r = requests.post("http://127.0.0.1:8079/", params = {
          'number': number,'password': password})
    print("Request method: POST, Response status_code: {},"\
               "Response data: {}".format(r.status_code, r.text))
    print("Copy and save your token!")
else:
    print("Wrong action")
