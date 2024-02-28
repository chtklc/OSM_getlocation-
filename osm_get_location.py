import requests

def get_location(q):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": q,
        "format": "json"
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return {"lat": data[0]["lat"], "lon": data[0]["lon"]}
    else:
        return ("İstek başarısız oldu:", response.status_code)

q = "Fatih Belediyesi"
print(get_location(q))
