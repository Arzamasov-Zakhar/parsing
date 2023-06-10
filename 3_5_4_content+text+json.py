import requests

for resp in range(1, 161):
    response = requests.get(url=f"https://parsinger.ru/img_download/img/ready/{resp}.png")
    with open(rf"C:\Users\User\PycharmProjects\parsing\image\image{resp}.png", "wb") as file:
        file.write(response.content)