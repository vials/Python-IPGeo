import requests

# IPStack API for IP Geolocation parsed by python3.
# Make sure to install the requests module: 'pip install requests' or 'python3 -m pip install requests'
# To retrieve a key, sign up on: 'https://ipstack.com' to retrieve a free API key. Once you have it, edit the Token variable with your updated key.
# To run: 'python3 lookup.py'

IP = input("Enter Target IP: ")

r = requests.get("http://api.ipstack.com/1.3.3.7?access_key=d343f129a1e16f630632ba017655305c")
for index, element in enumerate(r.json()):
    print("{}: {}".format(element, r.json()[element]))
