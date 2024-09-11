import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver


URL = "https://www.yanolja.com/reviews/domestic/3012015?sort=HOST_CHOICE"


def crawl_yanolja_reviews():
    print("hi")
    reviews = []
    driver = webdriver.Chrome()
    driver.get(URL)

    time.sleep(3)

    scroll_count = 10

    for i in range(scroll_count):
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight);')
        print(f'# crawling data {i+1} / {scroll_count}')
        time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    review_containers = soup.select(
        '#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select(
        '#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div.css-1mwn02k:first-child > div > p.css-1irbwe1')

    print("=============")
    print(f"# done : {len(review_containers)}")

    for i in range(len(review_containers)):
        review_text = review_containers[i].find(
            'p', class_='content-text').text
        review_starts = review_containers[i].find_all(
            'path', {'fill': '#FDBD00'})
        star_count = len(review_starts)
        date = review_date[i].text

        review_dict = {
            'review': review_text,
            'starts': star_count,
            'date': date
        }

        reviews.append(review_dict)

    with open('./resource/reviews.json', 'w') as f:
        json.dump(reviews, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    crawl_yanolja_reviews()
