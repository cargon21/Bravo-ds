from bs4 import BeautifulSoup
from collections import Counter
import requests

def getUlTag(result):
    pass

def main():
    try:
        URL = "https://www.umb.edu/academics/cla/faculty"
        connection = requests.get(URL, headers = {"User-Agent": "Mozilla/5.0"})

        parser = BeautifulSoup(connection.content, "lxml")

        result2 = parser.findAll("ul")

        departments = [tag for tag in result2[5]]

        for i in departments:
            print(type(i))

    except Exception as e:
        print(f"there was an error: {e})")

main()
