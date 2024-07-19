import requests
from bs4 import BeautifulSoup
import random

def scrape_movies():
    url = "https://www.imdb.com/chart/top/"
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    response = requests.get(url, headers=headers)
    print(f"Response status code: {response.status_code}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    element = soup.find_all('h3', class_='ipc-title__text')
    element = element[1:-1]

    random_movie = random.choice(element)

    print(f"Random movie selected: {random_movie.get_text()}")

if __name__ == "__main__":
    movie_list = scrape_movies()
   