# API =[YOUR API KEY]
import requests


def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}"
    response = requests.get(url)
    contents = response.json()
    data = contents["list"]
    nr = 8 * days
    data = data[:nr]
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=2, kind="Sky"))


