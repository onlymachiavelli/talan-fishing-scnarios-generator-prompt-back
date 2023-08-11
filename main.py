
#http 
import requests 
from linkedin_scraper import Person, actions, Company
from selenium import webdriver
driver = webdriver.Chrome()

"""

myLogin = {
    "user"  :"tmakaveli643@gmail.com" , 
    "pass" : "BestDeveloper643"
}

print("Posts : " , posts)
import base64

encoded_string = "AQH8uMIcAv0-uAAAAYnaeAxEVyQEeFeGg-_e1CG3ZQWlUQTCbX0vgH0OcZZQH8pjZ28Dlj6M0IeDQNuqzORoCaYwzQf3XDVA8PilNXDVHjmCuPX6A-QsqfCW"

decoded_bytes = base64.b64decode(encoded_string)
decoded_string = decoded_bytes.decode('utf-8')

print(decoded_string)
"""

from flask import Flask, request, jsonify






app = Flask(__name__)

@app.route("/", methods=['POST'])
def shit():
    myLogin :dict= request.json

    print(myLogin)
    actions.login(driver, myLogin['user'], myLogin['pass']) # if email and password isnt given, it'll prompt in terminal
    #person = Person("https://www.linkedin.com/in/ahmedhbaieb77/", driver=driver)
    comp= Company("https://www.linkedin.com/company/talan-tunisie/posts/", driver=driver)

    #scrap posts 
    #posts = person.get_posts(driver=driver, scroll=True, close_on_complete=False)


    return str(comp)


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000, debug=True)