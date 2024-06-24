import csv
import json
import requests
def load_disaster_data(file_path):
    with open(file_path,"r",newline="",encoding="latin-1") as reader:
        return list(csv.reader(reader))#
def load_city_data(file_path):
    with open(file_path,'r',newline='',encoding='utf-8') as reader:
        return list(csv.reader(reader))#
def display_data(disaster_data, location, iso):
    cl=[]
    for c, i in enumerate(disaster_data,1):
        if location in i[13].lower() and iso==i[9]:#
            cl.append([location,c,i[6],i[25],i[9]])#
    if cl!=[]:
        dl.append(cl)
def get_coordinates(location,api_key):
    url=f'https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={api_key}'
    response=requests.get(url)
    data=response.json()
    if data['status']=='OK':
        latitude=data['results'][0]['geometry']['location']['lat']
        longitude=data['results'][0]['geometry']['location']['lng']
        return [latitude,longitude]
    else:
        return None
def get_nearby_cities(city_data,lat,lon,radius):#
    l=[]
    u_lat=lat+radius
    l_lat=lat-radius
    l_lon=lon-radius
    r_lon=lon+radius
    for i in city_data:
        city_lat=float(i[2])
        city_lon=float(i[3])
        if l_lat<=city_lat<=u_lat and l_lon<=city_lon<=r_lon:
            l.append(i[1])
    return l
def get_country_code(address,api_key):
    url=f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response=requests.get(url)
    data=response.json()
    if data['status']=='OK':
        components=data['results'][0]['address_components']
        for component in components:
            if 'country' in component['types']:
                return component['short_name']
    else:
        return None
def get_iso3_from_code(city_data,iso2):
    for i in city_data:
        if i[5]==iso2:#
            return i[6]#
def create_file(dl):
    with open("result.json", 'w') as file:
        json.dump(dl, file, indent=4)
    print("created")
dl=[]
city_name=input("Enter Your City Name = ")
rad=int(input("Enter Radius(in km) = "))
disaster_data=load_disaster_data("disasterproj.csv")
city_data=load_city_data("worldcities.csv")
api_key='YOUR_API_KEY'
coordinates=get_coordinates(city_name,api_key)
if coordinates:
    lat,lon=coordinates
    radius=(rad/100)*0.9
    nearby_cities=get_nearby_cities(city_data,lat,lon,radius)
    country_code=get_country_code(city_name,api_key)
    if country_code:
        c_name=get_iso3_from_code(city_data,country_code)
        if c_name:
            for city in nearby_cities:
                display_data(disaster_data,city.lower(),c_name)
            create_file(dl)
            print("Ended")
