import re

deg = r"PhD|MA|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|Juris Doctor"
patterns = r"\s*(PhD|MA|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|Juris Doctor)\s*|\d+|(University of \w+, \w+)|\(|\)|,"
uni = r"\s*University|College|UMass"

patterns2 = r"\d+"

degrees = [
['MA, Theater Education, Emerson College BFA, Design Technology, New York University'],
['PhD (History of Medicine) Johns Hopkins University BA (History) Wesleyan University'],
['PhD, University of Iowa 2017'],
['MA UMass Boston'],
['PhD, Language and Literacy Education, Pennsylvania State University MA, Applied Linguistics, University of Massachusetts Boston BA, Greek Philology/Linguistics, National University of Athens, Greece'],
['MFA, University of California, Berkeley  BFA & BA, University of Colorado, Boulder']
]


for i in degrees:
    if "," not in i[0]:
        m = re.split(patterns, i[0])
        m = [re.sub(",", "", i.strip()) for i in m if i and (re.search(uni, i) or re.search(deg, i))]
        print(m)

    else:
        m = re.split(patterns, i[0])
        m = [re.sub(",", "", i.strip()) for i in m if i and (re.search(uni, i) or re.search(deg, i))]

        print(m)



# li = [ ['PhD', 'Cornell University'],['MA', 'Cornell University'],['MA', 'Northeastern University'],['PhD', 'University of Chicago Chicago'],
# ['BA', 'St. Olaf College'],['PhD', 'University of Pennsylvania'],['PhD', 'University of Pennsylvania'],['PhD', 'Yale University'],
# ['PhD', 'Michigan State University'],['PhD', 'Boston University'],['PhD', 'Boston University'],['MFA', 'Minnesota State University at Mankato'],
# ['BA', 'St. Cloud State University'],['PhD', 'Iowa State University'],['PhD', 'University of Texas at Austin'],
# ['PhD', 'University of Connecticut 1988'],['PhD', 'University of Massachusetts Amherst'],['PhD', 'University of California Berkeley'],
# ['PhD', 'University of California Los'],['MA', 'University of California Los'],['BA', 'University of Chicago'],['PhD', 'Columbia University'],
# ['JD', 'PhD'],['MFA', 'Boston University'],['PhD', 'Howard University'],['MA', 'Howard University'],
# ['BA', 'Florida Agricultural and Mechanical University'],['PhD', 'Bryn Mawr College'],['MA', 'Bryn Mawr College'],['MA', 'London University'],
# ['BA', 'Cambridge University'],['PhD', 'Brown University'],['PhD', 'University of Massachusetts Amherst'],['PhD', 'Clark University'],
# ['MA', 'Ohio State University'],['BA', 'College of Wooster'],['PhD', 'Florida State University'],['MA', 'North Carolina State University'],
# ['BA', 'University of Kansas'],['PhD', 'The University of Pennsylvania'],['PhD', 'University of Kentucky 2007'],['PhD', 'Emory University'],
# ['PhD', 'University of Illinois at Chicago'],['BA', 'Northwestern University'],['PhD', 'University of Delaware'],
# ['PhD', 'University of Michigan 1991'],['BA', 'Marlboro College MPPA'],['PhD', 'University of Massachusetts Amherst'],
# ['PhD', 'University of Pennsylvania 2005'],['PhD', 'The University of Toronto'],['MA', 'California State University'],
# ['BA', 'Franklin and Marshall College'],['PhD', 'University of Toulouse II'],['PhD', 'University of Washington'],
# ['AB', 'Brown University'],['PhD', 'University of Missouri 2016'],['MA', 'Syracuse University'],['BA', 'Western University'],
# ['PhD', 'The University of Michigan'],['PhD', 'University of California San'],['PhD', 'University of Michigan Music'],
# ['MM', 'University of Michigan Music'],['PhD', 'Wesleyan University'],['PhD', 'Princeton University'],['BA', 'Yale University'],
# ['PhD', 'Emory University'],['PhD', 'Brown University'],['PhD', 'Binghamton University'],['PhD', 'University of Michigan'],
# ['PhD', 'Northeastern University'],['PhD', 'Clark University'],['MA', 'Ohio State University'],['BA', 'College of Wooster'],
# ['BA', 'Bridgewater State College American Academy of Dramatic Arts'],['PhD', 'University of California Los'],
# ['PhD', 'University of California Santa'],['MS', 'University of Vermont 2006'],['PhD', 'University of Massachusetts Amherst'],
# ['PhD', 'University of Pennsylvania'],['PhD', 'University of London'],['MPhil', 'Cambridge University'],['PhD', 'Boston University'],
# ['PhD', 'American University'],['PhD', 'University of California Berkeley'],['MM', 'University of Miami'],['PhD', 'Boston University'],
# ['MA', 'UMass Boston'],['PhD', 'University of Iowa'],['MA', 'Boston University'],['PhD', 'Brown University'],
# ['PhD', 'Pennsylvania State University'],['PhD', 'University of Illinois Chicago'],['PhD', 'University of Nevada Reno'],
# ['MS', 'University of Nevada Reno'],['MA', "Queen's University of Belfast"],['BA', 'University of Oregon'],['PhD', 'University of Florida'],
# ['MFA', 'University of Colorado'],['MFA', 'PhD'],['PhD', 'University of Illinois Chicago'],['PhD', 'Wayne State University'],
# ['PhD', 'New York University'],['MFA', 'University of Pittsburgh'],['BA', 'Baldwin-Wallace College'],['PhD', 'Boston College'],
# ['MA', 'Boston College'],['BA', 'Bowdoin College LICSW'],['PhD', 'University of Connecticut'],['MA', 'Trinity College'],
# ['PhD', 'University of Iowa 2017'],['MPhil', 'Chinese University of Hong Kong'],['MA', 'Hong Kong University of Science and Technology'],
# ['BA', 'Fudan University'],['PhD', 'American University'],['PhD', 'Binghamton University – State University of New York'],
# ['MA', 'Northwestern University'],['BA', 'University of Maryland Eastern Shore'],['PhD', 'University of Nebraska – Lincoln'],
# ['PhD', 'University of Massachusetts Amherst'],['PhD', 'University of Florida'],['MA', 'The University of Texas at Austin'],
# ['BA', 'Sogang University'],['PhD', 'University of Pittsburgh'],['MA', 'University of Arizona'],['PhD', 'University of Notre Dame'],
# ['MEd', 'University of Massachusetts Boston'],['MA', 'University of Massachusetts Boston'],['MS', 'University of Massachusetts Boston M'],
# ['BA', 'University of Massachusetts Boston'],['BA', 'University of Massachusetts Boston'],['MA', 'University of Chicago'],
# ['PhD', 'State University of New York at Buffalo'],['PhD', 'Brandeis University'],['MA', 'Columbia University'],
# ['PhD', 'University of Southern California'],['MA', 'University of Southern California'],['MA', 'National University of Singapore'],
# ['BA', 'Peking University'],['PhD', 'Duke University'],['MA', 'Duke University'],['BA', 'North Carolina Central University'],
# ['BA', 'North Carolina Central University'],['MA', 'University of Guelph EdD'],['PhD', 'University of Southern California'],
# ['MEd', 'DePaul University'],['PhD', 'Northwestern University'],['PhD', 'University of Utah'],['MFA', 'University of Illinois'],
# ['BA', 'Carnegie Mellon University'],['PhD', 'University of Chicago Chicago'],['BA', 'St. Olaf College'],['PhD', 'Harvard University'],
# ['PhD', 'Harvard University MDiv'],['BA', 'University of California at Santa Barbara'],['PhD', 'Michigan State University'],
# ['PhD', 'Michigan State University'],['PhD', 'University of Maryland'],['MA', 'University of Texas - Arlington'],
# ['MA', 'Beijing Foreign Studies University'],['BA', 'Yantain University'],['PhD', 'University of Illinois at Chicago'],
# ['MUPP', 'University of Illinois at Chicago'],['BA', 'Boston University'],['PhD', 'Princeton University'],['PhD', 'Harvard University'],
# ['PhD', 'University of Texas at Austin'],['PhD', 'University of Minnesota 1993'],['MA', 'BA'],['PhD', 'University of Maryland College Park'],
# ['BS', 'University of Florida'],['PhD', 'University of California Berkeley'],['PhD', 'University of Michigan'],
# ['PhD', 'University of Massachusetts Amherst'],['PhD', 'University of Chicago 2011'],['MA', 'University of Chicago 2005'],
# ['BA', 'Northwestern University'],['PhD', 'MIT'],['PhD', 'London School of Economics'],['PhD', 'Western Michigan University'],
# ['PhD', 'University of Pennsylvania'],['PhD', 'University of Ottawa'],['PhD', 'Harvard University'],
# ['PhD', 'University of Chicago'],['MA', 'University of Chicago'],['BA', 'University of California Berkeley'],['MA', 'Emerson College'],
# ['BFA', 'New York University'],['PhD', 'University of California Davis'],['MA', 'Royal Roads University'],
# ['BA', 'York University'],['PhD', 'University of Chicago'],['PhD', 'New York University'],['PhD', 'University of Minnesota'],
# ['PhD', 'Cornell University'],['MA', 'Cornell University'],['MFA', 'University of Colorado'],['MFA', 'PhD'],
# ['PhD', 'Harvard University'],['PhD', 'University of California Irvine'],['PhD', 'Rice University'],
# ['PhD', 'University of Massachusetts Amherst'],['PhD', 'Brandeis University'],['PhD', 'Princeton University'],
# ['PhD', 'University of Cambridge'],['MPhil', 'University of Cambridge'],['BA', 'Williams College'],
# ['PhD', 'Michigan State University'],['MS', 'Iowa State University'],['BA', 'Drake University'],['PhD', 'University of Athens Greece'],
# ['BA', 'University of Thessaloniki Greece'],['PhD', 'Johns Hopkins University'],['BA', 'Wesleyan University'],['PhD', 'Harvard University'],
# ['PhD', 'Oxford University'],['PhD', 'University of Minnesota'],['MA', 'The University of West Florida'],['BS', 'Eastern Michigan University'],
# ['PhD', 'Stanford University'],['PhD', 'Columbia University'],['MPhil', 'University of Oxford'],['BA', 'University of Chicago'],
# ['PhD', 'Princeton University'],['PhD', 'University of Massachusetts Amherst'],['PhD', 'Indiana University - Bloomington'],
# ['PhD', 'University of California Berkeley'],['PhD', 'New York University'],['PhD', 'University of North Carolina'],
# ['PhD', 'University of Massachusetts Boston'],['PhD', 'University of Kentucky'],['PhD', 'Yale University'],
# ['PhD', 'University of Toronto 2008'],['PhD', 'University of Houston'],['PhD', 'York University'],['PhD', 'University of Florida'],
# ['PhD', 'Princeton University'],['PhD', 'University of Pennsylvania 2005'],['MA', 'Tufts University'],
# ['PhD', 'University of Minnesota 1999'],['BA', 'University of Toronto 1986'],['PhD', 'Boston University'],['PhD', 'Duke University'],
# ['PhD', 'Florida State University'],['PhD', 'Northwestern University'],['PhD', 'University of California-Berkeley'],
# ['PhD', 'Brandeis University'],['PhD', 'New York University'],['PhD', 'University of California - Irvine'],['PhD', 'University of Michigan'],
# ['PhD', 'New York University'],['PhD', 'Georgetown University'],['MS', 'Georgetown University'],['BA', 'The University of Virginia'],
# ['PhD', 'Harvard University'],['MA', 'Boston College'],['PhD', 'The New School For Social Research'],['PhD', 'Northwestern University'],
# ['MA', 'Florida State University'],['BA', 'Longwood College'],['PhD', 'Boston University'],['PhD', 'University of Massachusetts Amherst'],
# ['PhD', 'University of Illinois at Urbana-Champaign'],['MA', 'University of Maine'],['PhD', 'University of Minnesota'],
# ['PhD', 'University of Iowa 2017'],['MPhil', 'Chinese University of Hong Kong'],['MA', 'Hong Kong University of Science and Technology'],
# ['BA', 'Fudan University'],['PhD', 'Harvard University'],['PhD', 'University of Toronto'],['PhD', 'Johns Hopkins University'],
# ['PhD', 'Harvard University'],['PhD', 'Brown University'],['PhD', 'University of Wisconsin-Milwaukee'],['MA', 'University of Maine'],
# ['BA', 'Miami University'],['PhD', 'Yale University'],['PhD', 'Brown University'],['PhD', 'York University'],
# ['PhD', 'University of Massachusetts Amherst'],['PhD', 'University of Illinois Chicago'],['PhD', 'Columbia University'],['BA', 'Williams College'],
# ['PhD', 'MIT'],['PhD', 'in Sociology. Northeastern University Post Doc. National Academy of Education/Spencer Foundation'],
# ['PhD', 'Purdue University'],['MA', 'American University of Beirut'],['BA', 'American University of Beirut'],['PhD', 'Duke University'],
# ['MA', 'Harvard University'],['BA', 'Smith College'],['PhD', 'State University of New York'],['MA', 'Hunter College'],
# ['PhD', 'New York University'],['PhD', 'Harvard University'],['AB', 'Princeton University'],['PhD', 'Emory University 2015'],
# ['MA', 'Tufts University'],['BA', 'Colby College'],['PhD', 'DePaul University'],['PhD', 'Columbia University'],['MA', 'Columbia University'],
# ['MA', 'Brandeis University'],['BA', 'Wesleyan University'],['PhD', 'Stanford University'],['PhD', 'University of Connecticut'],
# ['MA', 'Trinity College'],['PhD', 'Harvard University'],['PhD', 'University of Southern California'],['PhD', 'Stanford University'],
# ['PhD', 'New School for Social Research'],['PhD', 'American University'],['PhD', 'University of California-Berkeley'],
# ['PhD', 'University of Texas Austin'],['BA', 'Oberlin College'],['PhD', 'University of Michigan'],['BA', 'Swarthmore College'],
# ['PhD', 'University of Massachusetts'],['PhD', 'The Pennsylvania State University'],['MA', 'University of Massachusetts Amherst'],
# ['BA', 'University of Illinois at Urbana-Champaign'],['PhD', 'University of California Los'],['PhD', 'University of Wisconsin - Madison'],
# ['PhD', 'Brandeis University'],['PhD', 'Rutgers University'],['PhD', 'University of Pennsylvania'],['BA', 'Oberlin College'],
# ['PhD', 'University of Southern California'],['MA', 'University of Southern California'],['BA', 'Scripps College'],
# ['PhD', 'University of Chicago 1974'],['PhD', 'Boston College'],['PhD', 'Catholic University of America'],
# ['Juris Doctor', 'Northeastern University School of Law'],['PhD', 'Indiana University'],['MFA', 'Yale University'],
# ['BA', 'The University of Texas at Austin'],['PhD', 'Boston University'],['BA', 'University of Pennsylvania'],
# ['MA', 'Boston University'],['PhD', 'University of Nebraska-Lincoln'],['PhD', 'Cornell University'],['PhD', 'New York University'],
# ['PhD', 'University of Minnesota'],['MFA', 'Boston University'],['BA', 'University of Pennsylvania 2004'],
# ['PhD', 'University of California Berkeley'],['PhD', 'Columbia University 1985'],['PhD', 'Stony Brook University'],
# ['MA', 'Tufts University'],['BA', 'Middlebury College'],['PhD', 'University of California San'],['PhD', 'State University of New York'],
# ['PhD', 'University of Wisconsin'],['PhD', 'University of Michigan'],['BA', 'Mount Holyoke College'],
# ['PhD', 'City University of New York Graduate Center'],['MFA', 'University of Michigan'],['PhD', 'Pennsylvania State University'],
# ['MA', 'University of Massachusetts Boston'],['BA', 'University of Athens Greece'] ]
#
# # li = [
# # ['PhD', 'Stanford University'],
# # ['PhD', 'University of Michigan Music'],
# # ['MM', 'University of Michigan Music'],
# # ['University of Toronto BMus', 'University of Western Ontario'],
# # ['PhD', 'University of California-Berkeley'],
# # ['PhD', 'University of Connecticut'],
# # ['MA', 'Trinity College'],
# # ['PhD', 'University of Kentucky 2007'],
# # ['PhD', 'Princeton University'],
# # ['MA', 'University of Massachusetts Boston'],
# # ['BA', 'University of Athens Greece'],
# # ['PhD', 'State University of New York'],
# # ['MA', 'Hunter College'],
# # ['PhD', 'Pennsylvania State University'],
# # ['PhD', 'Pennsylvania State University'],
# # ['MA', 'Pennsylvania State University'],
# # ['MA', 'Pennsylvania State University']
# # ]
#
# final = []
#
# li.sort(key = lambda x: x[1])
#
# for i in li:
#     boolean = True
#     dictionary = {}
#     dictionary["University"] = i[1]
#
#     for j in final:
#         if dictionary["University"] in j.values() and i[0] in j.keys():
#             j[i[0]] += 1
#             boolean = False
#         elif dictionary["University"] in j.values() and i[0] not in j.keys():
#             j[i[0]] = 1
#             print(j[i[0]])
#             boolean = False
#
#     if (boolean):
#         dictionary[i[0]] = 1
#         final.append(dictionary)
#
# summ = 0
#
# for i in final:
#     for key, value in i.items():
#         if isinstance(value, int):
#             summ += value
#
#
#
# print(len(li))
# print("Sum:", summ)
# print(len(final))
#





