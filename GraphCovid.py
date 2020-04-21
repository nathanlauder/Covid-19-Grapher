from graphics import *

# run through the cases.txt file to create 2d list of deaths and cases
def getCases():
    inFile = open('cases.txt', 'r')
    allEntries = []
    for line in inFile:
        line = line.strip()
        line.split('\t')
        line = line.split("\t")
        allEntries.append(line)
        #allCases.append(singleCase)
    #print(allEntries)
    # 0index is the month, 1st is the date, 2nd index is the deaths, 3rd is is confirmed cases
    modifiedCases = []
    for i in range(len(allEntries)):
        singleCase = []
        # get the date and account for dashes
        if allEntries[i][2][1] == '-':
            # get the month
            singleCase.append(allEntries[i][2][2:5])
            singleCase.append(allEntries[i][2][0])
            #print(allEntries[i][2][0])  # date
        else:
            # get the month
            singleCase.append(allEntries[i][2][3:6])
            singleCase.append(allEntries[i][2][0:2])
            #print(allEntries[i][2][0:2]) # date
        # get the deaths
        singleCase.append(int(allEntries[i][3]))
        # get confirmed cases
        singleCase.append(int(allEntries[i][4]))
        modifiedCases.append(singleCase)
    return modifiedCases
    #print(modifiedCases)
    #print(len(modifiedCases))

# set up the graphics window
def makeGraph():
    win = GraphWin("Covid-19 Graph", 1000, 800)
    win.setCoords(0, 0, 1000, 2000000)
    print(1800000-100000)
    # set the title and labels
    title = Text(Point(500, 1950000), "COVID-19 CASES BY DAY")
    title.setSize(24)
    title.draw(win)
    xLabel = Text(Point(500, 30000), "Time (Days since Dec 31st, 2019)")
    xLabel.draw(win)
    yLabel = Text(Point(75, 1950000), "Amount")
    yLabel.draw(win)
    # set the graph axes
    yAxis = Line(Point(75, 100000), Point(75, 1900000))
    yAxis.draw(win)
    xAxis = Line(Point(75, 100000), Point(950, 100000))
    xAxis.draw(win)
    confirmedCasesLabel = Text(Point(450, 1900000), "Confirmed Cases")
    confirmedCasesLabel.setTextColor("blue")
    confirmedCasesLabel.draw(win)
    deathLabel = Text(Point(550, 1900000), "Confirmed Deaths")
    deathLabel.setTextColor("red")
    deathLabel.draw(win)

    # labeling the y axis with numbers
    yCount = 150000
    caseCount = 1000
    while yCount<1900000:
        if caseCount < 1000000:
            num = caseCount/1000
            numLabel = Text(Point(50, yCount), str(num)+" k")
            numLabel.draw(win)
        else:
            num = caseCount/1000000
            numLabel = Text(Point(50, yCount), str(num) + " m")
            numLabel.draw(win)
        yCount+=96550
        caseCount+=109500

    # labeling the x axis in days after Dec 31 2019
    days = 1
    xCount = 80
    while xCount < 945:
        dayLabel = Text(Point(xCount, 80000), str(days))
        dayLabel.draw(win)
        days += 1
        xCount += 18
    cases = getCases()
    # run the line for the confirmed cases
    currentX = 100
    """numbers to set the labels are arbitrary and just what looked best as well as lined 
        up best to represent the data.  dividing int the for loops was done simply to keep 
        the lines inside the graph."""
    currentX = 75
    currentXdeath = 75
    for i in range(len(cases)):
        if i != (len(cases)-1):
            currentY = 110550+int((cases[i][3])/1.1) # have to divide by yCount otherwise it increments in pixels
            nextX = currentX + 8.3
            nextY = 110550+int((cases[i+1][3])/1.1)

            currentYdeath = 110550 + int(
                (cases[i][2]) / 1.1)  # have to divide by yCount otherwise it increments in pixels
            nextXdeath = currentXdeath + 8.3
            nextYdeath = 110550 + int((cases[i + 1][2]) / 1.1)
            #print(i)
            line = Line(Point(currentX, currentY), Point(nextX, nextY))
            line.setFill('blue')
            line.draw(win)
            deathLine = Line(Point(currentXdeath, currentYdeath), Point(nextXdeath, nextYdeath))
            deathLine.setFill('red')
            deathLine.draw(win)
            currentX = nextX
            currentY = nextY
            currentXdeath = nextXdeath
            currentYdeath = nextYdeath
    print(cases[-1])
    y = win.getMouse()
    print(y.getY())
    win.getMouse()
makeGraph()