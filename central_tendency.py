import statistics as Stat

# prints a menu to the console to get user directions
def menu (outputFile):
    answer = 0
    mydata = enterData() # gets the dataset from the user

    while answer != 7:
        if answer < 0 or answer > 7:
            print("That is not a valid response. Please try again")
        else:
            print("1. Get the arithmetic mean of the data")
            print("2. Get the median of the data")
            print("3. Get the mode of the data")
            print("4. Get the standard deviation of the data")
            print("5. Show all listed measures of central tendency")
            print("6. Input new data")
            print("7. Exit the program")

            answer = int(input("Please enter the number corresponding to your choice: "))
            if answer == 1:
                calcMean(mydata, outputFile)
            elif answer == 2:
                calcMedian(mydata, outputFile)
            elif answer == 3:
                calcMode(mydata, outputFile)
            elif answer == 4:
                standardDeviation(mydata, outputFile)
            elif answer == 5:
                outputFile.write("\n")
                calcMean(mydata, outputFile)
                calcMedian(mydata, outputFile)
                calcMode(mydata, outputFile)
                standardDeviation(mydata, outputFile)
                outputFile.write("\n")
            elif answer == 6:
                mydata = enterData()
            elif answer == 7:
                break

# prompts user for data and stores in a list
def enterData():
    data = []
    response = input("Please enter your data points separated by commas:  ")
    formatted = response.replace(" ", "").split(",")
    for i in formatted:
        data.append(int(i))

    return(data)

def calcMean(data, file):
    file.write("Mean: {}\n".format(Stat.mean(data)))

def calcMedian(data, file):
    file.write("Median: {}\n".format(Stat.median(data)))

def calcMode(data, file):
    try:
        file.write("Mode: {}\n".format(Stat.mode(data)))
    except:
        file.write("A distinct Mode does not exist for this data.\n")

def standardDeviation(data, file):
    file.write("Sample Standard Deviation: {}\n".format(Stat.stdev(data)))

def main():
    output = open("Averages.txt", "w")
    menu(output)
    output.close()


main()
