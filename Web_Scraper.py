import requests
import html
from bs4 import BeautifulSoup


def main():
    url = "https://example.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')

        for p in paragraphs:
            text = html.unescape(p.get_text())
            print(text)
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


if __name__ == "__main__":
    main()