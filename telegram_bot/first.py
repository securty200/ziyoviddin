import requests
def firstname():
    l=[]
    res = requests.get(
        "https://api.telegram.org/bot6219929580:AAEq3XTWjwOlpzAHIv4N12Y3Qe4lsOX5z-M/getUpdates"
    ).json()

    for result in res["result"]:
        l.append(result["message"]["from"]["first_name"])
        return l[0]
