from googlesearch import search

# to search
query = "covid-19"

links = []
for j in search(query, tld="co.in", lang='en', num=100, stop=100, pause=2):
    links.append(j)

print(links)
