import numpy
import sys
import csv

def cleanData(inputFileName):
	
	if not inputFileName:
   		print "Please enter Input file as an arguement while running the program \n for ex: python pgmName filename.csv\n"
	try:
		#fileHandle = open("/Users/Apoorva/Downloads/file1_1.csv", 'r')
		fileHandle = open(inputFileName, 'r')
	except IOError:
		print "File is not found, please enter a valid file\n"
	
	list_ratings = []
	movieDict = {}
	for line in fileHandle:
		movieIDSplit = line.split(':')
		movieDict[movieIDSplit[0]]= {}
		
		usersRating=movieIDSplit[1].split(',')
		for user in usersRating:
			userIdAndRating = user.split('_')
			movieDict[movieIDSplit[0]][userIdAndRating[0]]=userIdAndRating[1]
			try:
				list_ratings.append(userIdAndRating[1])
			except ValueError:
				pass
	
	na = numpy.array(list_ratings).astype(numpy.float)
	meanOfRating = numpy.mean(na)
	stdOfRating = numpy.std(na)
	
	print "mean of all ratings", meanOfRating
	print "Std deviation of ratings", stdOfRating	

	with open("clean_File_2.csv", "w+") as oFileHandle:
		fieldnames = ['movieID', 'userID', 'nRating']
    		writer = csv.DictWriter(oFileHandle, fieldnames=fieldnames)
		writer.writeheader()
		for eachMovie in movieDict.keys():
			for eachUserId in movieDict[eachMovie].keys():
				try:
					nRating = (meanOfRating - int(movieDict[eachMovie][eachUserId]))/stdOfRating
					writer.writerow({'movieID': eachMovie, 'userID': eachUserId, 'nRating': nRating})
				except ValueError:
                                	nRating = (meanOfRating - meanOfRating)/stdOfRating
					writer.writerow({'movieID': eachMovie, 'userID': eachUserId, 'nRating': nRating})

	fileHandle.close()
	oFileHandle.close()
	return "clean_File_2.csv"
	

if __name__ == "__main__":
	inputFileName = sys.argv[1]
	outputFileName = cleanData(inputFileName)
        print "Look for an output file with name:", outputFileName



