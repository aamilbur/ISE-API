import http.client
import json

conn = http.client.HTTPSConnection("10.83.114.253")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'X-Auth-Access-Token': 'cbff351d-b9cb-4d63-85aa-a6d30f28a595'
}
conn.request("GET", "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks", payload, headers, verify=False)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))