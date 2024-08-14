# import requests
# #Using sinch to send textmessage to customer
# servicePlanId = "017b4f515b614e9bbdbaed6d23af4cda"
# apiToken = "e874cbee8c1b4b0d879222af2805e6f1"
# sinchNumber = "12084869482"
# toNumbers = ["18653236437","18652366336"]
# url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

# payload = {
#   "from": sinchNumber,
#   "to": toNumbers,
#   "body": "Hello THis is message from JackyNguyen. I'm testing"
# }

# headers = {
#   "Content-Type": "application/json",
#   "Authorization": "Bearer " + apiToken
# }

# response = requests.post(url, json=payload, headers=headers)

# data = response.json()
# print(data)
import requests

# Read numbers from the text file
with open('numbers.txt', 'r') as file:
    toNumbers = [line.strip() for line in file.readlines()]

servicePlanId = "017b4f515b614e9bbdbaed6d23af4cda"
apiToken = "e874cbee8c1b4b0d879222af2805e6f1"
sinchNumber = "12084869482"
url = "https://us.sms.api.sinch.com/xms/v1/" + servicePlanId + "/batches"

payload = {
  "from": sinchNumber,
  "to": toNumbers,
  "body": "Sapphire Nail and SPa in Turkey Creek is having a promotion. Bring this message and get 10 percent off"
}

headers = {
  "Content-Type": "application/json",
  "Authorization": "Bearer " + apiToken
}

response = requests.post(url, json=payload, headers=headers)

data = response.json()
print(data)
