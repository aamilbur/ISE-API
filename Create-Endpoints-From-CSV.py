import pandas
import requests
import json

#  Read in CSV data
data = pandas.read_csv("Lab Phones.csv")

mac_array = data.to_numpy()
#print(mac_array)

# Loop through CSV data
for x in mac_array:
    mac_address = x[0]
    description = x[1]
    location = x[2]
    name = x[0]

    # Post CSV data to ISE
    payload = json.dumps({
        "description": description,
        "mac": mac_address,
        "name": name,
        # "location": location,
        "staticGroupAssignment": True,
        "groupId": "2d9e4de0-3153-11ee-b15b-9ede33f33e33"
    })
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Basic YXBpLWFkbWluOmZzcC1XV2NzMQ==',
        'Cookie': 'APPSESSIONID=B72E52108156594F343FCC79E6666435; JSESSIONIDSSO=ED489004E68DF345CFB31A91E687B95B'
    }
    url = "https://172.18.149.16:443/api/v1/endpoint"
    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    print(response.text)


