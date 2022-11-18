import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/b411d0b1ef11bf644de2ae20d8ea798e/flightDeals/users"

print("Welcome to MIA's Flight Club!")
print("We find the best flight deals and email you. ")
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email? ")
email_rep = input("Type your email again. ")
if email == email_rep:
    print("You're in the club!")
else:
    print("Please, make sure that you enter the same email.")


data = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}



response = requests.post(url=SHEETY_API_ENDPOINT, json=data)
print(response.text)