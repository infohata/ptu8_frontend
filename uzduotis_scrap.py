from bs4 import BeautifulSoup
import requests
import random

# with open('delfi.html', 'r') as f:
#     html = f.read()

# soup = BeautifulSoup(html, "html.parser")

# first_list = []
# second_list = []
# for element in soup.select('.CBarticleTitle'):
#     kazkas = element.get_text().split(":")
#     if len(kazkas) == 1:
#         continue
#     else:
#         first_list.append(kazkas[0])  
#         second_list.append(kazkas[1])
# random.shuffle(second_list)

# merged_list = list(map(lambda x, y: f"{x}: {y}", first_list, second_list))
# for i, sentence in enumerate(merged_list,1):
#     print(f"{i}: {sentence}")


# def get_quotes():
#     quotes = []
#     for i in range(1, 11):
#         url = f'http://quotes.toscrape.com/page/{i}/'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         for element in soup.select('.text'):
#             quotes.append(element.get_text())
#     return quotes


# Function to fetch quotes from website
# def get_quotes():
#     quotes = []
#     for i in range(1, 11):
#         url = f'http://quotes.toscrape.com/page/{i}/'
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         quotes.extend(soup.select('.quote'))
#     return quotes

    

   




