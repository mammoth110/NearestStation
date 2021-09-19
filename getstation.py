import requests
import xmltodict

# 住所・ランドマークから緯度、経度を取得する
# https://www.geocoding.jp/api/?q=東京タワー
def getcoordinate(full_address):
    url = 'http://www.geocoding.jp/api/'
    payload = {'q': full_address}
    result = requests.get(url, params=payload)
    resultdict = xmltodict.parse(result.text)
    codes = resultdict['result']['coordinate']
    lat = codes['lat']  # 緯度
    lng = codes['lng']  # 経度
    return lat, lng

# express.heartrails.com
def getstations(lat, lng):
    url = 'http://express.heartrails.com/api/xml'
    payload = {'method': 'getStations',
        'x': lng,
        'y': lat
    }
    result = requests.get(url, params=payload)
    resultdict = xmltodict.parse(result.text)
    stations = resultdict['response']['station']
    return(stations)

if __name__ == "__main__":
    full_address = "東京タワー"
    lat, lng = getcoordinate(full_address)
    print(lat, lng)
    stations = getstations(lat, lng)
    num = len(stations)
    print(num, '個の最寄り駅を表示します')
    for station in stations:
        print(station['name'], station['line'], station['distance'])