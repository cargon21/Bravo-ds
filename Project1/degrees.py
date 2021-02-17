from bs4 import BeautifulSoup, NavigableString
from collections import Counter
import requests

def getFacultyMembers(dURL):
    deptConnection = requests.get(dURL, headers={"User-Agent": "Mozilla/5.0"})
    deptParser = BeautifulSoup(deptConnection.content, "lxml")
    mInclude = "faculty_staff/bio"

    # -----------------------------------------
    # Works when the pages have no Images
    # results = [i.get("href") for i in deptParser.find(class_="linkList").findAll("a")]
    #
    # for i in results:
    #     print(str(i))
    # -----------------------------------------

    # -----------------------------------------
    # This part works when the full time faculty members are listed first (for pages with images)
    results = [i.get("href") for i in deptParser.find(class_="units-row staff-groups").findAll("a") if mInclude in i.get("href")]

    results = set(results)
    for i in results:
        pass
        print(i)
    # -----------------------------------------

    return ""

    # -----------------------------------------
    # This part is incomplete (for pages with images)
    # resultsImg = deptParser.findAll(class_="units-row staff-groups")
    #
    # s = []
    # for i in resultsImg:
    #     i = i.findAll("a")
    # for i in resultsImg:
    #     i = i.findAll("a")
    #     #print(len(i))
    #     for j in i:
    #         if mInclude in j.get("href") and len(i) > 16:
    #             s.append(j.get("href"))
    # s = set(s)
    # for i in s:
    #     print(i)

def main():
    try:
        baseURL = "https://www.umb.edu"
        departmentsURL = "https://www.umb.edu/academics/cla/faculty"
        connection = requests.get(departmentsURL, headers={"User-Agent": "Mozilla/5.0"})

        parser = BeautifulSoup(connection.content, "lxml")

        result2 = parser.findAll("ul")

        departments = [tag for tag in result2[5]]

        faculty = []
        for i in departments:
            if not isinstance(i, NavigableString):
                if("https" not in i.a['href'] and "africana" in i.a['href']):
                    dURL = baseURL + i.a['href']
                    faculty.append(getFacultyMembers(dURL))

    except Exception as e:
        print(f"there was an error: {e})")

main()
