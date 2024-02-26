import requests

card_number = "BT1-010"

url = f"https://digimoncard.io/api-public/search.php?card={card_number}"

response = requests.request(
    method="GET",
    url=url,
    headers={"Content-Type": "application/json"},
    data={}
)
#dif metodo de acceso, forma de acceder
#SOAP protocololo
#REST arquitectectura

print(response.text)

