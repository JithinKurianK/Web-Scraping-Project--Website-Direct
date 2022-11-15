# Import Libraries
from bs4 import BeautifulSoup
import requests,openpyxl

# create excel sheet
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'movies rating'
sheet.append(['Rank','Name','Year','Rating'])

# extract
try:
    source = requests.get('https://www.imdb.com/india/top-rated-malayalam-movies/')
    source.raise_for_status()

    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('tbody',class_="lister-list").find_all('tr')

    for movie in movies:
        rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]

        name = movie.find('td',class_="titleColumn").a.text

        year = movie.find('td',class_="titleColumn").span.text.strip('()')

        rating = movie.find('td',class_="ratingColumn imdbRating").strong.text

        print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])

except Exception as a:
    print(a)
    
# saving data into excel file
excel.save('malayalam movies ratings.xlsx')