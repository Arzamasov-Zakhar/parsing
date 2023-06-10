import requests




for i in range(1, 501):
    url = "https://parsinger.ru/task/1/" + str(i) + ".html"
    response = requests.get(url=url)
    if response.status_code == 200:
        print(response.text)