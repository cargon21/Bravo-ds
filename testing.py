import re

deg = r"PhD|MA|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|Juris Doctor"
patterns2 = r"\s*(PhD|MA|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|Juris Doctor)\s*|(University of \w+, \w+)|\(|\)|,"
uni = r"\s*University|College|UMass"

patterns = r"\s*(PhD|MA|BA|BFA|MFA|MM|MA|MS|DPhil|AB|MUPP|MEd|MNEd|JD|LCSW|ABD|Juris Doctor)\s*|\d+|(University of [a-z]+, [a-z]+)|\(|\)|,"

degrees2 = [
['MA, Theater Education, Emerson College BFA, Design Technology, New York University'],
['PhD (History of Medicine) Johns Hopkins University BA (History) Wesleyan University'],
['PhD, University of Iowa 2017'],
['MA UMass Boston'],
['PhD, Language and Literacy Education, Pennsylvania State University MA, Applied Linguistics, University of Massachusetts Boston BA, Greek Philology/Linguistics, National University of Athens, Greece'],
['MFA, University of California, Berkeley  BFA & BA, University of Colorado, Boulder']
]
degrees = [
['MFA, Painting and Printmaking, Yale University, 1997 BAA, Plan II (Honors Humanities) and Studio Art (Painting),The University of Texas at Austin, 1995'],
['PhD, American Studies, Boston University'],['PhD, Wayne State University'],['PhD, Columbia University 1985'],
    ['PhD in Applied Linguistics and Technology, Iowa State University'],['PhD University of California Berkeley'],['PhD, Emory University'],
    ['PhD, American University'],['PhD in Language, Literacy and Culture, Stanford University'],
    ['PhD, University of Minnesota, 1993 Grado de Licenciada (MA Equivalent): Universidad Complutense de Madrid Licenciatura (BA eq): Universidad Complutense de Madrid'],['MA, Boston College'],['PhD, Economics, University of Massachusetts Amherst'],['PhD, Economics, University of Massachusetts Amherst'],['MA, Boston University'],['PhD 2003, Boston University'],['PhD, City University of New York Graduate Center, 2010'],['PhD, Northwestern University'],['PhD, University of Pennsylvania'],['PhD, Brown University'],
    ['PhD, University of Chicago, 1974'],['PhD, Clinical Psychology, Boston University'],['PhD University of Michigan'],['MA (Humanitarian Assistance), Tufts University, 2013 PhD (History), University of Minnesota, 1999 BA (History), University of Toronto, 1986'],['PhD, University of Michigan, Music Education with a cognate in Wind Conducting MMEd, University of Michigan, Music Education BEd, University of Toronto BMus, University of Western Ontario, Music and French'],['PhD, Michigan State University'],['PhD Harvard University'],['PhD, Duke University MA, Harvard University BA, Smith College'],
    ['PhD (History) University of Southern California MA (History) University of Southern California MA (History) National University of Singapore BAs (History and Economics) Peking University'],
    ['PhD, University of Illinois, Chicago, 2015'],['PhD, MIT, 1990'],['PhD, Oxford University'],

    ['PhD, Wesleyan University'],['BA, Bridgewater State College American Academy of Dramatic Arts'],['PhD, University of Minnesota  MA, The University of West Florida BS, Eastern Michigan University'],['PhD, Rutgers University'],['PhD, University of Illinois, Chicago'],['PhD, The University of Pennsylvania (2007)'],['PhD, English, New York University MFA, Poetry, University of Pittsburgh BA, English and French, Baldwin-Wallace College'],['PhD (Communication), University of California Davis, 2017 MA (Professional Communication), Royal Roads University, 2013 BA (Professional Writing, Institutional Communication) and Advanced French Proficiency Certificate, York University, 2010'],
    ['PhD, Duke University'],['PhD, University of Illinois at Chicago BA, Northwestern University'],['PhD, University of Connecticut MA, Trinity College'],['PhD, Second Language Education, OISE, The University of Toronto MA, TESOL, California State University, Los Angeles BA, Economics and Drama, Franklin and Marshall College'],['PhD, American University'],['PhD, University of Pennsylvania (2001)'],['PhD, Princeton University'],['PhD, University of Cambridge MPhil, University of Cambridge BA, Williams College'],
    ['PhD, University of Kentucky, 2007'],['MFA, Scenic Design, Minnesota State University at Mankato BA, Theatre, St. Cloud State University'],['PhD, Counseling Psychology, University of Maryland College Park BS, Psychology, University of Florida'],['PhD, State University of New York, Stony Brook MA, Hunter College, CUNY'],['PhD, Indiana University'],['PhD, University of Iowa, 2017 MPhil, Chinese University of Hong Kong, 2012 MA, Hong Kong University of Science and Technology, 2010  BA, Fudan University, 2009'],['PhD, Michigan State University'],['PhD, Harvard University'],
    ['PhD, Language and Literacy Education, Pennsylvania State University MA, Applied Linguistics, University of Massachusetts Boston BA, Greek Philology/Linguistics, National University of Athens, Greece'],['PhD, University of Notre Dame'],['PhD, New School for Social Research'],['PhD, American Studies and Slavic Languages and Literatures, Yale University'],['PhD, Florida State University MA, North Carolina State University BA, University of Kansas'],
    ['PhD in Public Policy and Economics, University of Michigan'],['PhD, Cornell University, 1992 MA, Cornell University, 1989'],['PhD New York University'],['PhD, Harvard University'],['PhD (Communication Studies), 2012, University of Texas at Austin'],['PhD, Political Science, Harvard University'],['PhD, Yale University'],['PhD, French Linguistics, Indiana University - Bloomington'],['PhD University of Pennsylvania'],['PhD New York University'],['MEd DePaul University'],
    ['PhD Columbia University BA Williams College'],['PhD University of Texas at Austin'],['PhD, Economics, University of California-Berkeley'],['PhD, The New School For Social Research, 2005'],['PhD, University of Massachusetts Amherst'],['PhD, Art History, University of Southern California, 2004 MA, Art History, University of Southern California, 2001 BA, Art History, Scripps College, 1995'],
    ['B.A., Bard College M.A., Ph.D. University of Connecticut'],['PhD, University of Minnesota'],['PhD Stanford University'],['PhD, English, Purdue University MA, English, American University of Beirut BA, English, American University of Beirut'],['PhD, University of California, Berkeley'],['PhD, University of California-Berkeley'],['PhD (History of Medicine) Johns Hopkins University BA (History) Wesleyan University'],['PhD, Department of Ethnic Studies, University of California, San Diego'],['PhD, The University of Michigan (2009)'],
    ['PhD, Clinical Psychology, Boston University BA, Psychology, University of Pennsylvania'],['PhD 1973, Yale University'],['PhD, State University of New York, Albany'],['PhD Brown University'],['PhD, University of London MPhil, Cambridge University (UK)'],['PhD, University of California, Los Angeles'],['PhD, Economics, University of Massachusetts Amherst'],['PhD, University of Illinois, Chicago'],['PhD, London School of Economics, 2002'],['PhD, University of Nebraska – Lincoln'],['PhD, Harvard University, Classical Philology, 2020 AB, Princeton University, Classics, 2014'],
    ['PhD in English (writing studies), University of Illinois at Urbana-Champaign  MA in English, University of Maine'],
    ['PhD, Linguistics, Georgetown University MS, Linguistics, Georgetown University BA, Italian and French Studies, The University of Virginia'],['PhD, Economics, University of Southern California, Los Angeles'],["PhD, University of Nevada, Reno MS, Geography, University of Nevada, Reno MA, Queen's University of Belfast BA, University of Oregon"],['PhD, Catholic University of America'],['PhD, University of Minnesota'],['PhD, Pennsylvania State University'],['PhD 1986, University of California, Berkeley'],
    ['PhD, African Diaspora (Latin American and the Caribbean) History, Howard University (2005) MA, African Diaspora History, Howard University (2000) BA, Computer Science, Florida Agricultural and Mechanical University (1997)'],['PhD, Cornell University, 2001'],['PhD, Columbia University, 2015 MA, Columbia University, 2009 MA, Brandeis University, 2008 BA, Wesleyan University, 2003'],['PhD, Boston University'],['PhD, University of Delaware'],['Juris Doctor, Northeastern University School of Law'],['PhD, University of Pennsylvania, 2005'],['PhD, University of Iowa, 2017 MPhil, Chinese University of Hong Kong, 2012 MA, Hong Kong University of Science and Technology, 2010  BA, Fudan University, 2009'],
    ['BA, Sociology and Gender Studies, Marlboro College MPPA, Public Policy and Administration, University of Massachusetts Amherst CAGS, Advanced Feminist Studies, University of Massachusetts Amherst PhD, Public Health, University of Massachusetts Amherst'],['PhD, Northeastern University'],['MFA, University of Michigan'],['PhD, University of Florida'],['PhD, DePaul University'],['PhD, University of Chicago'],['PhD, Brandeis University'],['PhD Harvard University'],
    ['PhD (History) Columbia University MPhil (Economic and Social History) University of Oxford BA (History) University of Chicago'],['PhD, Florida State University'],['PhD, University of Connecticut, 1988'],['PhD, New York University'],['MA, University of Chicago'],['PhD, York University'],['PhD, Stony Brook University MA, Tufts University BA, Middlebury College'],['PhD, University of Massachusetts Boston'],['PhD, Stanford University'],['MFA 1993, University of Colorado MFA 2015, Transart Institute PhD Candidate, Transart Institute'],
    ['PhD, University of California, Berkeley'],['MA, Theater Education, Emerson College BFA, Design Technology, New York University'],['PhD (Mass Communication), 2012, University of Florida MA (Advertising), 2008, The University of Texas at Austin BA (French Culture, American Culture, and Mass Communications), 2004, Sogang University'],['MA, English Studies, University of Guelph EdD, English Education (Teaching Literature), Teachers College, Columbia University'],['PhD, Applied Linguistics, The Pennsylvania State University MA, French, Concentration in Teaching, University of Massachusetts Amherst BA, Teaching of French, University of Illinois at Urbana-Champaign'],['PhD, New York University'],
    ['PhD 1994, University of California, Berkeley'],['PhD, American University'],['PhD, University of Wisconsin - Madison'],['PhD (Communication), 2012, University of Maryland MA (Communication), 2007, University of Texas - Arlington MA (Linguistics), 2003, Beijing Foreign Studies University BA (English), 2000, Yantain University'],['MA, Boston University'],['PhD, University of Massachusetts'],['PhD, Psychology, Boston College MA, Psychology, Boston College BA, Psychology, Bowdoin College LICSW'],
    ['PhD, Cultural Anthropology, Duke University MA, Cultural Anthropology, Duke University  BA, History, North Carolina Central University BA, Modern Foreign Languages (Spanish), North Carolina Central University'],['MFA, Boston University, 2011 BA, University of Pennsylvania, 2004'],['PhD, University of Massachusetts Amherst'],['PhD, Harvard University'],['PhD, University of Michigan BA, Swarthmore College'],['PhD, Translation Studies, University of Ottawa'],['PhD, Emory University'],['PhD, Columbia University, 2014'],
    ['MEd, Instructional Design, University of Massachusetts Boston MA, Applied Linguistics, University of Massachusetts Boston MS, Information Technology, University of Massachusetts Boston MBA with a focus on Human Resources, University of Massachusetts Boston BA, Computer Science, minoring in Italian, University of Massachusetts Boston'],['PhD, University of Massachusetts Amherst'],
    ['PhD, Mass Media, Michigan State University, East Lansing, Michigan MS, Journalism and Mass Communication, Iowa State University, Ames, Iowa BA, Journalism and Mass Communication, Drake University, Des Moines, Iowa'],['PhD, University of California - Irvine'],['PhD, Harvard University MDiv, Harvard Divinity School BA, University of California at Santa Barbara'],['PhD, University of Michigan'],['PhD in Curriculum and Instruction, University of Florida'],['PhD, University of Toulouse, II (France), 1996'],
    ['JD, Harvard Law School PhD, Massachusetts Institute of Technology'],['PhD, University of Pittsburgh MA, University of Arizona'],['PhD, University of California, Los Angeles MA, Spanish, University of California, Los Angeles, 2011 BA, University of Chicago'],['PhD, Brown University'],
    ['PhD, Brandeis University MA, Columbia University'],['PhD, Brown University'],['PhD University of Texas, Austin BA, Oberlin College'],['PhD, University of Wisconsin'],['PhD (History) University of Chicago MA (History) University of Chicago BA (History and Political Science) University of California, Berkeley Diplome, Alliance Française (Paris)'],['PhD, American Studies, Boston University'],['PhD, University of Massachusetts Amherst'],['PhD, University of Chicago, 2011 MA, University of Chicago, 2005 BA, Northwestern University, 2002'],
    ['PhD, University of Houston'],['PhD, Rice University'],['MS in Community Development and Applied Economics, with graduate certificate in Ecological Economics, University of Vermont, 2006 PhD in Resource Economics, University of Massachusetts Amherst, 2010'],['PhD in Sociology. Northeastern University Post Doc. National Academy of Education/Spencer Foundation'],['MA, Northeastern University'],['PhD, University of Michigan BA, Mount Holyoke College'],['PhD, Economics, University of Nebraska-Lincoln'],['PhD, University of Kentucky'],
    ['PhD, State University of New York at Buffalo'],['PhD Brown University'],['PhD, Binghamton University (SUNY)'],['PhD, Department of Ethnic Studies, University of California, San Diego'],['MM, New England Conservatory BMus, University of Miami'],['PhD, University of Minnesota'],['PhD, University of Connecticut MA, Trinity College'],
    ['PhD, Art History, Emory University 2015 MA, Art History,Tufts University BA, Art, Colby College'],['PhD, Public Policy Analysis-Urban Planning and Policy, University of Illinois at Chicago MUPP, Master of Urban Planning and Policy, University of Illinois at Chicago BA, Soviet and East European Studies, Boston University'],['PhD, History, Johns Hopkins University'],['PhD, University of California, Los Angeles'],['PhD, University of California, Irvine'],['PhD, Art History, Northwestern University, 2001 MA, Art History, Florida State University, 1995 BA, English, Longwood College, 1985'],
    ['PhD, Princeton University BA, Yale University'],["PhD, Women's Studies, Clark University MA, Women's Studies, Ohio State University BA, Women's Studies & Cultural Area Studies, College of Wooster"],
    ['PhD, Department of Linguistics, National and Kapodistrian University of Athens, Greece BA, Italian Language and Literature, Aristotle University of Thessaloniki, Greece'],['PhD, University of Pennsylvania, 2005'],
    ['PhD, Cornell University, 1992 MA, Cornell University, 1989'],['PhD, University of Michigan, 1991'],["PhD, Women's Studies, Clark University MA, Women's Studies, Ohio State University BA, Women's Studies & Cultural Area Studies, College of Wooster"],['MA UMass Boston'],
    ['PhD, Michigan State University'],['PhD, Urban Studies, University of Wisconsin-Milwaukee MA, Speech Communication, University of Maine BA, Speech Communication, Miami University'],['PhD, Harvard University'],['PhD, Harvard University'],['Ph.D. in Archaeology, Simon Fraser University (Burnaby, BC), August 2017 MA. in Archaeology, Simon Fraser University (Burnaby, BC), March 2012 BA. Honours in Anthropology, Pontificia Universidad Católica del Ecuador (Quito, ECU), March 2007'],['PhD, Philosophy, MIT, 2010'],['PhD University of Pennsylvania'],
    ['PhD, Princeton University'],['PhD, University of Utah MFA, University of Illinois BA, Carnegie Mellon University'],['PhD, University of Iowa'],['PhD (Communication), University of Missouri, 2016 MA (Magazine, Newspaper, and Online Journalism), Syracuse University, 2008 BA (Political Science), Western University, 2007'],['PhD (History) University of Pennsylvania BA (History) Oberlin College'],['PhD, Economics, University of Southern California, Los Angeles'],['PhD, University of Washington AB, Brown University'],['PhD, Boston College'],['PhD Princeton University'],
    ['PhD, Cinema and Media Studies and English Language and Literature, University of Chicago, Chicago, IL BA (English), St. Olaf College, Northfield, MN'],['PhD, Cinema and Media Studies and English Language and Literature, University of Chicago, Chicago, IL BA (English), St. Olaf College, Northfield, MN'],['MFA, Boston University'],
    ['PhD, New York University'],['PhD, Brandeis University, 1977'],['PhD, University of California, Santa Barbara'],['PhD Princeton University'],['PhD, University of Toronto'],['PhD, Northwestern University, 1999'],['PhD Brandeis University'],['PhD Bryn Mawr College MA (History) Bryn Mawr College (1977) MA (American Studies) London University (1976) BA (History) Cambridge University (1975)'],['PhD, Boston University'],['PhD, New York University'],['PhD, University of Massachusetts Amherst'],['PhD, Western Michigan University'],
    ['MFA 1993, University of Colorado MFA 2015, Transart Institute PhD Candidate, Transart Institute'],['PhD, University of North Carolina, Chapel Hill'],['PhD, History, Binghamton University – State University of New York (SUNY) MA, History, Northwestern University BA, English, University of Maryland Eastern Shore (UMES)'],
    ['PhD, York University'],['PhD, University of Toronto, 2008'],
    ['PhD Harvard University']

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





