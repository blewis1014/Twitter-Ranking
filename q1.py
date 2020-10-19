import requests
import urllib.request
import http.client
import os.path
from boilerpipe.extract import Extractor

count = 1

def download_HTML():
    urlFile=open('CleanedURLs.txt','r')
    #urlFile=open('testRankingURLs.txt','r')
    urlFileOPen= urlFile.readlines()

    global count

    for url in urlFileOPen:
        print("URI {}: Processing".format(count))
        try:
            response = requests.get(url)
            store_HTML(response.text,count)
            store_proc_HTML(url,count)
        except (requests.exceptions.RequestException):
            print("\tError: URI invalid")
    
        print("URI {}: Finished \n".format(count))
        count+=1

    print("\nDone\nTotal URIs processed: "+str(count-1))



def store_HTML(response,counter):
    rawHtmlOut = open(r"C:\Users\Brenden\Desktop\ODU\Fall 2020\CS432\HW_3\hw3-ranking-blewis1014\Raw_HTML\rawHtmlFile{}.txt".format(counter),"a", encoding="utf-8")
    rawHtmlOut.write(response)
    rawHtmlOut.close()

def store_proc_HTML(source,counter):

    while True:
        try:
            extractor = Extractor(extractor='ArticleExtractor', url=source)
            extracted_text = extractor.getText()
        except (urllib.error.HTTPError, (http.client.IncompleteRead), NameError, LookupError, UnicodeDecodeError):
            print("\tURI invalid")
            return False
        


        procHtmlOut = open(r"C:\Users\Brenden\Desktop\ODU\Fall 2020\CS432\HW_3\hw3-ranking-blewis1014\Processed_HTML\processedHtmlFile{}.txt".format(counter),"a",encoding="utf-8")
        procHtmlOut.write(str(extracted_text))
        procHtmlOut.close()
        return True
    



if __name__ == '__main__':
    download_HTML()

