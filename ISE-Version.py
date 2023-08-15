import requests
import json

url = "https://172.18.149.16:9060/ers/config/op/systemconfig/iseversion"

payload = {}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic YXBpLWFkbWluOmZzcC1XV2NzMQ==',
  'Cookie': 'APPSESSIONID=FC1C0C63EBEC9BD792A03C6E4010A275; JSESSIONIDSSO=F5AA97036C678B25D35B752E8F050595'
}
# REALLY important, when using a self-signed certificate, to add the "verify=False" to any call to ISE.
# The call will fail out if you do not.
response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)