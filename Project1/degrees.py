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
   degrees = [i.findNext("p").get_text().strip() for i in bioParser.findAll("h4") if i.get_text().strip() == "Degrees"]

   # for i in degreesTag:
   #     degreesList = [i.findNext("p").get_text().strip()]
   #     print(degreesList)

   return degrees

def getData(data):      # returns a dictionary with the Degree name and University name
    deg = r"PhD|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|MPhil|BS|Juris Doctor|MA/MPhil"
    patterns = r"\s*(PhD|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|MPhil|BS|Juris Doctor|MA/MPhil)\s*|\d+|(University of \w+, \w+)|\(|\)|,|(College of \w*)"
    uni = r"\s*University|College|UMass|MIT|London School|New School"
    m = []

    # if "," not in data[0]:          # decided to split the data into items with commas and without commas
    m = re.split(patterns, data[0])
    m = [re.sub(",", "", i.strip()) for i in m if i and (re.search(uni, i) or re.search(deg, i))]

    # else:
    #     m = re.split(patterns, data[0])
    #     m = [re.sub(",", "", i.strip()) for i in m if i and (re.search(uni, i) or re.search(deg, i))]

    return m

def getDictionary(li):  # We determined the easiest way to write into a csv file with the data we had was with a dictionary
    final = []

    for i in li:
        boolean = True
        dictionary = {}
        dictionary["University"] = i[1]

        for j in final:
            if dictionary["University"] in j.values() and i[0] in j.keys():
                j[i[0]] += 1
                boolean = False
            elif dictionary["University"] in j.values() and i[0] not in j.keys():
                j[i[0]] = 1
                boolean = False

        if boolean:
            dictionary[i[0]] = 1
            final.append(dictionary)

    return final


def main():
    try:
        baseURL = "https://www.umb.edu"
        departmentsURL = "https://www.umb.edu/academics/cla/faculty"
        connection = requests.get(departmentsURL, headers={"User-Agent": "Mozilla/5.0"})

        parser = BeautifulSoup(connection.content, "lxml")

        result2 = parser.findAll("ul")

        departments = [tag for tag in result2[5]]  # the 5th 'ul' tag was the dept name

        faculty = []
        for i in departments:
            if not isinstance(i, NavigableString):                      # edge case for the cinema studies page (different format)
                if "https" in i.a["href"] and "cinema" in i.a["href"]:
                    faculty.append(getFacultyMembers(i.a["href"], "cinema" ))
                elif("latino" not in i.a["href"]):
                    dURL = baseURL + i.a["href"]
                    faculty.append(getFacultyMembers(dURL))
        
        
        chainedResults = set(itertools.chain.from_iterable(faculty))    # took all of the faculty links and linked them together, and removed duplicates
        
        chainedResults = list(set(itertools.chain.from_iterable(faculty)))  # needed them as a list so we could iterate over the items

        chainedResults = [getBioPages(i) for i in chainedResults if len(getBioPages(i)) >= 1]   # getBioPages was returning empty lists hence the >= 1

        data = []
        for i in chainedResults:
            if len(i[0]) > 3 and len(getData(i)) % 2 == 0:  # used % 2 to eliminate the values which had two consecutive degrees and then the school
                temp = getData(i)                           # this eliminated edge cases that would have add alot of time
                if len(temp) > 2:
                    for j in range(0, (len(temp) - 1), 2):
                        data.append([temp[j], temp[j+1]])
                else:
                    data.append(temp)

        fields = ["University", "PhD", "BA", "BFA", "MFA", "MM", "MS", "DPhil", "AB", "MUPP", "MEd", "MNEd",
                  "JD", "LCSW", "ABD", "MPhil", "BS", "Juris Doctor", "MA", "MA/MPhil"]

        data = [i for i in data if i[0] in fields]

        finalResult = getDictionary(data)

        # name of csv file
        filename = "university_records.csv"

        print(len(finalResult))

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)

            # writing headers (field names)
            writer.writeheader()

            # writing data rows
            writer.writerows(finalResult)


    except Exception as e:
        print(f"there was an error: {e})")

main()