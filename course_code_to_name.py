from googlesearch import search
import urllib.request


def searcher(course_code, university):
    query = course_code + ' ' + university
    output = []
    [output.append(j) for j in search(query, stop=10)]
    return output


def url_to_title(url_in):
    wp = urllib.request.urlopen(url_in)
    pw = wp.read()
    return pw


search_result = searcher('EECS 370', 'University of Michigan')
print(search_result)

html = url_to_title('https://web.eecs.umich.edu/~profmars/index.html%3Fp=26.html')
print(html)
