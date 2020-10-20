import ast
import math
import pandas as pd
from operator import itemgetter

collection = []
results = []
inputFile = "FinalURLsForRanking.txt"
query = "Xbox"
CORPUS = 55000000000

def calcTF(doc):
    freq = doc["occurences"]
    total_words = doc["words"]
    tf = float(freq / total_words)
    return round(tf,3)

def calcIDF(allDocuments, corpus):
    numDocs = len(allDocuments)
    idf = math.log2(corpus/numDocs)
    return round(idf,3)

def calcTFIDF(tf,idf):
    return round((tf*idf),3)

def drawResultsTable():
    pass

def printResults():
    for item in results:
        print(str(item)+'\n')

def writeResultsToFile():
    with open("TF-IDF_Results.txt","w") as f:
        for item in results:
            f.write(str(item)+'\n')

def sortTDFDescending():
    sort_list = sorted(results, key=itemgetter('TF-IDF'), reverse=True)
    return sort_list

if __name__ == '__main__':
    with open(inputFile, 'r') as f:
        for line in f:
            content = line.strip()
            collection.append(ast.literal_eval(content))
    
    idf = calcIDF(collection,CORPUS)

    for elem in collection:
        tf = calcTF(elem)
        tfidf = calcTFIDF(tf,idf)
        uri_ranking = {"uri":elem["uri"], "TF":tf, "IDF":idf, "TF-IDF":tfidf}
        results.append(uri_ranking)
    results = sortTDFDescending()
    printResults()
    writeResultsToFile()
