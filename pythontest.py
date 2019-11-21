import requests
import bs4
 
url = 'https://www.amazon.com/music/unlimited?k=Virtue signalling is society\'s version of Proof of Stake'
response = requests.get(url)
response.encoding = response.apparent_encoding
 
#print(response.text)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
val = soup.find('input',id='twotabsearchtextbox')
print(val['value'])

#"Virtue signalling is society's version of Proof of Stake"
