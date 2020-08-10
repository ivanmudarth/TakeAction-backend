import unittest
from getURL import getURL

output_urls = ["https://www.canadahelps.org/en/donate-to-coronavirus-outbreak-response/",
               "https://www.gofundme.com/c/blog/fundraising-for-coronavirus", "https://www.who.int/emergencies/diseases/novel-coronavirus-2019/donate"]


class TestStringMethods(unittest.TestCase):
    def test_URL(self):
        INPUT_URLS = ['https://globalnews.ca/news/7007527/coronavirus-cases-saskatchewan-may-20/',
                      'https://globalnews.ca/news/7007402/coronavirus-1-new-case-people-in-campbellton-symptom-watch/']
        OUTPUT_URLS = [output_urls, output_urls]

        for input, output in zip(INPUT_URLS, OUTPUT_URLS):
            self.assertEqual(getURL(input), output)


if __name__ == "__main__":
    unittest.main()

# how to run this test
# cd in to utils directory
# python -m unittest getURLtest.py
