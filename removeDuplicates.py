from progressbar import ProgressBar

perc = ProgressBar()

urls = []

urlFile=open('RankingURLs.txt','r')
urlFileOPen= urlFile.readlines()

count = 1
seen = set()
cleaned = []

print("Adding URLs to list")
for url in perc(urlFileOPen):
    if url not in seen:
        seen.add(url)
        cleaned.append(url)

urlFile.close()

# cleaned = set(urls)




with open("CleanedURLs.txt","w") as f:
    print("Writing cleaned URLs to file:")
    for item in cleaned:
        f.write(item)

