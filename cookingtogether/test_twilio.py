import urllib.parse

#import ipdb; ipdb.set_trace()

tw_service_num = '+19713510672'
tw_account_sid = 'AC383a2d29ab50db39e2a5556b51269045'
tw_auth_token = 'ef11b3d01084ddabd7353600254838a6'
tw_msg_sid = 'MGc0983f97269a7883e207fda2d4094891'

params = {
    'To': '+19719989511', 
    'From': tw_service_num, 
    'Body': 'postman forever'
}

import http.client

conn = http.client.HTTPSConnection("api.twilio.com")
payload = urllib.parse.urlencode(params)

headers = {
    'Authorization': 'Basic QUMzODNhMmQyOWFiNTBkYjM5ZTJhNTU1NmI1MTI2OTA0NTplZjExYjNkMDEwODRkZGFiZDczNTM2MDAyNTQ4MzhhNg==',
    'Content-Type': 'application/x-www-form-urlencoded'
}

conn.request("POST", f"/2010-04-01/Accounts/{tw_account_sid}/Messages.json", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
