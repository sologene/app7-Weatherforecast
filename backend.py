API = "69edf0567adcaa338e8d5b987fa569a2"
import requests


def get_data(place, days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API}"
    response = requests.get(url)
    contents = response.json()
    data = contents["list"]
    nr = 8 * days
    data = data[:nr]

    if kind == "Temperature":
        data = [dit["main"]["temp"] for dit in data]
    if kind == "Sky":
        data = [dit["weather"][0]["main"] for dit in data]
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo", days=2, kind="Sky"))


