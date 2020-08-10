import urllib.request
from typing import List
from bs4 import BeautifulSoup


def getURL(url: str) -> List[str]:

    bank = {"covid-19": 0, "virus": 0, "rally": 0, "pandemic": 0, "contaminate": 0,
            "distancing": 0, "coronavirus": 0, "deaths": 0, "coronavirus": 0, "cases": 0}

    with urllib.request.urlopen(url) as url:
        html = url.read()
    soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    for word in text.split():
        # print(word)v
        if word.lower() in bank:
            bank[word.lower()] += 1

    counter = 0

    for word in bank:
        if bank[word] >= 3:
            counter += 1

    if counter >= 3:
        return ["https://www.canadahelps.org/en/donate-to-coronavirus-outbreak-response/",
                "https://www.gofundme.com/c/blog/fundraising-for-coronavirus",
                "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate"
                ]

    return ["google.com"]


# if __name__ == "__main__":
##    output = getURL("https://toronto.ctvnews.ca/ontario-records-323-new-covid-19-cases-amid-record-number-of-tests-completed-in-single-day-1.4961672")
# print(output)
