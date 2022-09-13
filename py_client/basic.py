import requests
# from pip._vendor import requests
# endpoint="https://httpbin.org/status/200/"
# endpoint="https://httpbin.org/anythig"
endpoint="http://localhost:8000/api/"

resp= requests.get(endpoint,json={"abc":123})

print(resp.headers)
print(resp.text)
# print(resp.json())
# print(res.status_code)