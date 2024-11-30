import requests
from bs4 import BeautifulSoup


def get_images_from_url(url="https://fastcampus.co.kr/data_online_llmservice"):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup.prettify())

    # 모든 img 태그 찾기
    images = soup.find_all('img')
    print(len(images))

    return images


def get_image_urls():
    return [
        "https://cdn.day1company.io/prod/uploads/202411/223557-1189/912-가이드-w-컬러-자유.webp",
        "https://storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202404/114614-472/intro-web.webp",
        "https://storage.googleapis.com/static.fastcampus.co.kr/prod/uploads/202404/163652-1423/group-1410118314.webp"
    ]


if __name__ == "__main__":
    image_urls = get_image_urls()

    for url in image_urls:
        print(url)
