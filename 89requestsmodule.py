import requests


#  GET Request (Website se data mangwana)
# 1. Ek website par GET request bheji
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

# 2. Check kiya ki kya website sahi chal rahi hai (Status Code 200 matlab OK)
print(response.status_code) # Output: 200

# 3. Website ne jo data bheja use text format mein print kiya
print(response.text) 
# Output: Ek JSON data dikhega (jaise user ID, title)




#  POST Request (Website par apna data bhejna)

url = "https://jsonplaceholder.typicode.com/posts"

# Jo data humein internet par bhejna hai, use dictionary mein likha
my_data = {
    "title": "Harry Bhai",
    "body": "Python Course is Awesome",
    "userId": 1
}

# requests.post se data server par bhej diya
response = requests.post(url, json=my_data)

print(response.status_code) # Output: 201 (Created - matlab data submit ho gaya)
print(response.text) # Server se confirmation message aayega



from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/blogpost/django-cheatsheet/"
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)
    