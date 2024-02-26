from zeep import Client
# https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL

#consumo de servicio SOAP

client = Client(
    "https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL"
)

# peticion o requests
result = client.service.NumberToWords(5)
print(result)

# cuenta en Postman


#####
client = Client(
    "http://localhost:8000/"
)

# peticion o requests
result = client.service.Saludar("Fabricio")
print(result)

