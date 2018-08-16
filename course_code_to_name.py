# modules needed: google, urllib.request, BeautifulSoup4
from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup
import re


class Part2:
    def __init__(self, num_searches=10):
        self.SEARCH_COUNT = num_searches
        self.no_result_count = 0

    # public interface
    def url_to_title_list(self, course_code, university):
        url_list = self.__searcher(course_code, university)
        title_list = []
        for url in url_list:
            try:
                html = self.__url_to_html(url)
                title = self.__html_to_title(html)
                # remove all non alphanumeric characters from title
                # credit: https://stackoverflow.com/a/1276774
                title = re.sub(r'\W+', ' ', title)

                # remove course code and university name from title
                title_broken_into_words = title.split()
                title_broken_into_words = [word for word in title_broken_into_words
                                           if word not in self.keywords]
                if (len(title_broken_into_words)) == 0:
                    continue
                title = ' '.join(title_broken_into_words)
                title_list.append(title)
                print(title)
            except urllib.error.HTTPError:
                print("url_to_html didnt work for url: ", url)
                self.no_result_count += 1
            except AttributeError:
                print("html_to_title didnt work for url: ", url)
                self.no_result_count += 1

        if self.no_result_count == self.SEARCH_COUNT:
            print("\nSearch didn't work\n")
        else:
            print("\nSearch worked\n")
        return title_list

    # helper functions
    def __searcher(self, course_code, university):
        # break course_code and university into individual keywords
        course_code_keywords = course_code.split()
        university_keywords = university.split()
        self.keywords = course_code_keywords + university_keywords

        query = course_code + ' ' + university
        output = []
        [output.append(j) for j in search(query, stop=self.SEARCH_COUNT)]
        return output

    def __url_to_html(self, url_in):
        opened = urllib.request.urlopen(url_in)
        html_doc = opened.read()
        return html_doc

    def __html_to_title(self, html_in):
        soup = BeautifulSoup(html_in, 'html.parser')
        return soup.title.string

# test cases
test_one = Part2()
title_list_one = test_one.url_to_title_list('EECS 370', 'University of Michigan')
# print(title_list_one)

test_two = Part2()
title_list_two = test_two.url_to_title_list('EECS 281', 'University of Michigan')
