from lxml import html
import requests

class Course:
    def __init__ (self, code, title, credit):
        self.subject = code[0: 4]
        self.code = code[5: len(code)]
        self.title = title
        self.credit = credit
    def printCourse(self):
        print self.subject + self.code + ' - ' + self.title + ' (' + self.credit + ')'

Catalog = requests.get('http://prog-crs.ust.hk/ugcourse/2017-18/COMP')
CatalogTree = html.fromstring(Catalog.content)

courseCode = CatalogTree.xpath('//div[@class="crse-code"]/text()')
courseTitle = CatalogTree.xpath('//div[@class="crse-title"]/text()')
courseCredit = CatalogTree.xpath('//div[@class="crse-unit"]/text()')
courses = []
for i in range(len(courseCode)):
    credit = courseCredit[i][0: len(courseCredit[i]) - 10]
    newCourse = Course(courseCode[i], courseTitle[i], credit)
    courses.append(newCourse)
    courses[i].printCourse()

