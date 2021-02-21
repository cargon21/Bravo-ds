from bs4 import BeautifulSoup, NavigableString
from collections import Counter
import requests
import itertools

def getFacultyMembers(dURL):
    deptConnection = requests.get(dURL, headers={"User-Agent": "Mozilla/5.0"})
    deptParser = BeautifulSoup(deptConnection.content, "lxml")
    mInclude = "faculty_staff/bio"
    pageImages = len(deptParser.findAll("img"))
    # pageHeader = deptParser.find(class_="dept_link") In case you want the departments

    # DOES NOT WORK FOR NATIVE AMERICAN STUDIES, AND LATINO STUDIES PAGES
    # Does not work with Native American Studies because the first category isn't the full time faculty
    # Does not work with Latino studies pages because the wrapper class is not named linkList

    # Special case where for the cinema studies program
    if "cinema_studies" in dURL:
        facultyLink = [i.find("a").get("href") for i in deptParser.findAll(class_="first") if "cinema_studies" in i.find("a").get("href")]
        cinemaLink = "https://www.umb.edu" + facultyLink[0]
        cinemaConnection = requests.get(cinemaLink, headers={"User-Agent": "Mozilla/5.0"})
        cinemaParser = BeautifulSoup(cinemaConnection.content, "lxml")
        print(cinemaLink)
        results = [i.find("a") for i in cinemaParser.findAll(class_="units-row")]
        print(results)

        # Not done

    # Case where there are images for the faculty members
    elif pageImages > 3:
        results = set(i.get("href") for i in deptParser.find(class_="units-row staff-groups").findAll("a")
                      if mInclude in i.get("href"))
        return list(results)

    # Case where there are not images for the faculty members
    elif pageImages == 3:
        results = [i.get("href") for i in deptParser.find(class_="linkList").findAll("a")]
        return results

    return []

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

def getIndPages():
    newURL = ""
    indConnection = requests.get(newURL, headers={"User-Agent": "Mozilla/5.0"})

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
                if "https" in i.a["href"] and "inema" in i.a["href"]:
                    faculty.append(getFacultyMembers(i.a["href"]))
                elif("latino" not in i.a["href"]):
                    dURL = baseURL + i.a["href"]
                    faculty.append(getFacultyMembers(dURL))
        
        # Right now the results are chained and just being printed, set length = 270
        chainedResults = set(itertools.chain.from_iterable(faculty))
        print (chainedResults)

    except Exception as e:
        print(f"there was an error: {e})")

main()
