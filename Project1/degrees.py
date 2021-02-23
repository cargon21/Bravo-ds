#----------------------------------------------------------------------------------------------------------------
# Carson Sytner and Jordan DeGiacomo
# Date: 2-15-21
# Purpose: Uses the BeatuifulSoup package to scrape the UMB Wesbite for faculty degree data.
# The data is then added to a CSV file.
#-----------------------------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup, NavigableString
import requests
import itertools
import csv
import re

# Function that returns the request connection
def connect(dURL):
    return requests.get(dURL, headers={"User-Agent": "Mozilla/5.0"})

# Function that returns the parser
def parse(deptConnection):
    return BeautifulSoup(deptConnection.content, "lxml")

# Function that returns a list of all the faculty member in a given program
def getFacultyMembers(dURL, program = ""):
    deptConnection = connect(dURL)
    deptParser = parse(deptConnection)
    mInclude = "faculty_staff/bio"
    pageImages = len(deptParser.findAll("img"))

    # Does not work with Latino studies pages because the wrapper class is not named linkList

    # Special case where for the cinema studies program
    if program in dURL and program != "":
        facultyLink = [i.find("a").get("href") for i in deptParser.findAll(class_="first") if "cinema_studies" in i.find("a").get("href")]
        cinemaLink = "https://www.umb.edu" + facultyLink[0]
        cinemaConnection = connect(cinemaLink)
        cinemaParser = parse(cinemaConnection)

        results = [i.find("a") for i in cinemaParser.findAll(class_="units-row")]

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

# Returns the Degrees and Universities with a given faculty member link
def getBioPages(bioURL):
    bioConnection = connect(bioURL)
    bioParser = parse(bioConnection)
    degrees = [i.findNext("p").get_text().strip() for i in bioParser.findAll("h4") if i.get_text().strip() == "Degrees"]

    return degrees

# Returns a list with the Degree and University names
def getData(data):
    patterns = r"\s*(PhD|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|MPhil|BS|Juris Doctor|MA/MPhil)\s*" \
               r"|\d+|(University of [a-z]+, [a-z]+)|\(|\)|,|(College of \w*)"
    deg = r"PhD|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|MPhil|BS|Juris Doctor|MA/MPhil"
    uni = r"\s*University|College|UMass|MIT|London School|New School"

    # Split by regular expressions and remove commas for more accurate pairing
    degContent = re.split(patterns, data[0])
    degContent = [re.sub(",", "", i.strip()) for i in degContent if i and (re.search(uni, i) or re.search(deg, i))]

    return degContent

# Dictionary formatting for convenient CSV writing
def getDictionary(li):
    returnList = []

    for i in li:
        inserted = False # Set a flag
        tempDict = {"University" : i[1]}

        # Checks if value already exists
        for j in returnList:
            if tempDict["University"] in j.values() and i[0] in j.keys():
                j[i[0]] += 1
                inserted = True
            elif tempDict["University"] in j.values() and i[0] not in j.keys():
                j[i[0]] = 1
                inserted = True

        if not inserted:
            tempDict[i[0]] = 1
            returnList.append(tempDict)

    return returnList

# Writes the data into the CSV file
def writeCSV(fileName, finalResult, fields):
    with open(fileName, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()

        # writing data rows
        writer.writerows(finalResult)

def main():
    # All degree fields
    fields = ["University", "PhD", "BA", "BFA", "MFA", "MM", "MS", "DPhil", "AB", "MUPP", "MEd", "MNEd",
              "JD", "LCSW", "ABD", "MPhil", "BS", "Juris Doctor", "MA", "MA/MPhil"]

    baseURL = "https://www.umb.edu"
    departmentsURL = "https://www.umb.edu/academics/cla/faculty"

    # Connect to the UMB Website
    try:
        connection = connect(departmentsURL)
        parser = parse(connection)
        result = parser.findAll("ul")

    except Exception as e:
        print(f"there was an error: {e})")

    # The fifth 'ul' tag has the department names
    departments = [i for i in result[5]]

    # Create list with faculty members from each program
    faculty = []
    for i in departments:
        if not isinstance(i, NavigableString):
            if "https" in i.a["href"] and "cinema" in i.a["href"]: # edge case for the cinema studies page (different format)
                faculty.append(getFacultyMembers(i.a["href"], "cinema"))
            elif ("latino/faculty" not in i.a["href"]): # Latino Studies Program uses different classes
                dURL = baseURL + i.a["href"]
                faculty.append(getFacultyMembers(dURL))

    # Transform into 1-D list with duplicates removed
    chainedResults = list(set(itertools.chain.from_iterable(faculty)))

    # The ">= 1" ensures there are not miscellaneous lists
    chainedResults = [getBioPages(i) for i in chainedResults if len(getBioPages(i)) >= 1]

    data = []
    for i in chainedResults:
        if len(i[0]) > 3 and len(getData(
                i)) % 2 == 0:  # % 2 eliminates the values which had two consecutive degrees and then the school
            temp = getData(i)
            if len(temp) > 2: # Formatting for lists with more than one degree / University
                for j in range(0, (len(temp) - 1), 2):
                    data.append([temp[j], temp[j + 1]])
            else:
                data.append(temp)

    # Remove unusual corner cases
    data = [i for i in data if i[0] in fields and i[1] not in fields]

    finalResult = getDictionary(data)

    fileName = "umb_faculty_education.csv"

    writeCSV(fileName, finalResult, fields) # Write to the CSV file

    print("Program Finished")
main()