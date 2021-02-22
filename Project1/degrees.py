from bs4 import BeautifulSoup, NavigableString
import requests
import itertools
import csv
import re

def getFacultyMembers(dURL, program = "-1"):
    deptConnection = requests.get(dURL, headers={"User-Agent": "Mozilla/5.0"})
    deptParser = BeautifulSoup(deptConnection.content, "lxml")
    mInclude = "faculty_staff/bio"
    pageImages = len(deptParser.findAll("img"))
    # pageHeader = deptParser.find(class_="dept_link") In case you want the departments

    # DOES NOT WORK FOR NATIVE AMERICAN STUDIES, AND LATINO STUDIES PAGES
    # Does not work with Native American Studies because the first category isn't the full time faculty
    # Does not work with Latino studies pages because the wrapper class is not named linkList

    # Special case where for the cinema studies program
    if program in dURL:
        facultyLink = [i.find("a").get("href") for i in deptParser.findAll(class_="first") if "cinema_studies" in i.find("a").get("href")]
        cinemaLink = "https://www.umb.edu" + facultyLink[0]
        cinemaConnection = requests.get(cinemaLink, headers={"User-Agent": "Mozilla/5.0"})
        cinemaParser = BeautifulSoup(cinemaConnection.content, "lxml")

       # print(cinemaLink)
        results = [i.find("a") for i in cinemaParser.findAll(class_="units-row")]
       # print(results)

        results = [i for i in cinemaParser.findAll(class_="units-row staff-groups")]

        # Sort by length
        results.sort(key=len)

        # The largest section will have the full-time faculty
        results = results[len(results) - 1]

        # Gets all the bios for each faculty member
        results = set(i.get("href") for i in results.findAll("a") if mInclude in i.get("href"))

        return list(results)

    # Case where there are images for the faculty members
    elif pageImages > 3:
        results = set(i.get("href") for i in deptParser.find(class_="units-row staff-groups").findAll("a")
                      if mInclude in i.get("href"))
        return list(results)

    # Case where there are not images for the faculty members
    elif pageImages == 3:
        results = ["https://www.umb.edu" + i.get("href") for i in deptParser.find(class_="linkList").findAll("a")]
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
    
def csvFile():
    with open("umbFaculty.csv", "w") as csvFileIn:
        writer = csv.writer(csvFileIn, delimiter=',', quotechar='"')
        writer.writerow('Degree Name', 'School Name') # write header
        # write the rest of the file; each row is a list of strings or numbers
        writer.writerows()

# This prints all the Degrees but the on garbage element is ['...']
def getBioPages(chainedResults):
   newURL = chainedResults
   bioConnection = requests.get(newURL, headers={"User-Agent": "Mozilla/5.0"})
   bioParser = BeautifulSoup(bioConnection.content, "lxml")
   degreesTag = [i for i in bioParser.findAll("h4") if i.get_text().strip() == "Degrees"]
    
   for i in degreesTag:
       degreesList = [i.findNext("p").get_text().strip()]
       print(degreesList, "\n")  

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
                if "https" in i.a["href"] and "cinema" in i.a["href"]:
                    faculty.append(getFacultyMembers(i.a["href"], "cinema" ))
                elif("latino" not in i.a["href"]):
                    dURL = baseURL + i.a["href"]
                    faculty.append(getFacultyMembers(dURL))
        
        # Right now the results are chained and just being printed, set length = 270
        chainedResults = set(itertools.chain.from_iterable(faculty))
        #print (chainedResults)
        chainedResults = list(set(itertools.chain.from_iterable(faculty)))
        
        for i in chainedResults:
            getBioPages(i)

    except Exception as e:
        print(f"there was an error: {e})")

main()

