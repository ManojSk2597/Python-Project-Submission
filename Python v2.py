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

    # Save prettified HTML to a file for inspection
    with open('output.html', 'w', encoding='utf-8') as f:
        f.write(soup.prettify())

    # Find movie titles and years
    movies = []
    for item in soup.select('h3.ipc-title__text'):
        title_tag = item.select_one('h3.ipc-title__text')
        year_tag = item.find_next('span', class_='ipc-metadata-list-summary-item__tc')  # Update this selector

        if title_tag and year_tag:
            title = title_tag.get_text().split('. ', 1)[1].strip()  # Remove ranking number and strip whitespace
            year = year_tag.get_text().strip('()')  # Adjust this based on actual year placement
            movies.append((title, year))

    if not movies:
        print("No movies found. Please check the HTML structure.")
    
    return movies

def pick_random_movie(movies):
    if not movies:
        print("No movies found.")
        return None
    return random.choice(movies)

if __name__ == "__main__":
    movie_list = scrape_movies()
    selected_movie = pick_random_movie(movie_list)

    if selected_movie:
        print(f"Randomly selected movie: {selected_movie[0]} ({selected_movie[1]})")