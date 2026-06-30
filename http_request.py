#import requests

#response = requests.get("https://api.github.com/")
#data = response.json()
#response.raise_for_status()
#print("status code:", response.status_code)
#print(data["current_user_ur1"])


#POST - call

payload = {"promot","hello","max_tokens":, "temp":.2}
headers = {"Authorization":"Bearer Fake-key"} #where api key

post = requests.post(
    "https://httpbin.org/post",
    json=payload,
    headers=headers,
    timeout=10
)
post.raise_for_status()
echoed_data = post.json()
print(echoed_data)
