import numpy as np 
from skimage import io
import requests
from bs4 import BeautifulSoup


url="https://apod.nasa.gov/apod/astropix.html"

content = requests.get(url).content

soup = BeautifulSoup(content,'lxml')

image_tags = soup.findAll('img')
print(image_tags)
image_tag= image_tags[0].get('src')
url=f"https://apod.nasa.gov/apod/{image_tag}"

request= requests.get(url).content
file= open("astro_pic.jpeg", "wb")
file.write(request)
file.close()