import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/Fandom"
    response = requests.get(url)
    return response.json()

    if data["success"] and "data" in data:
        data["data"]
    