from progressbar import ProgressBar
import glob
import os

perc = ProgressBar()

path = r"C:\Users\Brenden\Desktop\ODU\Fall 2020\CS432\HW_3\hw3-ranking-blewis1014\Processed_HTML\*.txt"
query = "Xbox"
count = 1

containsQuery = []
all = []

for file in perc(glob.glob(path)):
    # infile = open(file,"r")
    occur = 0
    totalWords = 0
    with open(file, "r", encoding='ISO-8859-1') as f:
        # text = f.read()
        # occur = text.count(query)
        file_name = os.path.basename(file)
        
        for lines in f:
            words = lines.split()
            for i in words:
                totalWords+=1
                if i == query:
                    occur+=1

        file_dict = {"file":file_name,"words:":totalWords,"occurences":occur}
        count+=1
        if (occur > 0) :
            containsQuery.append(file_dict)
        all.append(file_dict)
 

outfile = open("QueryResults.txt","w")
outfile.write("Query: "+query+"\n")
for item in containsQuery:
    outfile.write(str(item)+"\n")

outfile.write("\nTotal # of documents: "+str(len(all)))
outfile.write("\nTotal # of documents that contain query: "+str(len(containsQuery)))
outfile.close()

results = open("QueryResultsForProcessing.txt","w")
for item in containsQuery:
    results.write(str(item)+"\n")
results.close()

print("Done")



