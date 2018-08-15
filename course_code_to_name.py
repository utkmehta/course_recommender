from googlesearch import search
import urllib.request
from bs4 import BeautifulSoup


def searcher(course_code, university):
    query = course_code + ' ' + university
    output = []
    [output.append(j) for j in search(query, stop=10)]
    return output


def url_to_html(url_in):
    wp = urllib.request.urlopen(url_in)
    pw = wp.read()
    return pw


def html_to_title(html_in):
    soup = BeautifulSoup(html_in, 'html.parser')
    return soup.title.string


url_list = searcher('EECS 370', 'University of Michigan')
for url in url_list:
    try:
        html = url_to_html(url)
        title = html_to_title(html)
        print(title)
    except:
        print("didnt work for url: ", url)

