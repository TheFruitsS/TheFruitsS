import re
from collections import deque

data = '22Managing Your First Impression29/01/2022Pass02/02/2022CompletedDownload21Developing a High Reliability Organization28/01/2022Pass02/02/2022CompletedDownload20Developing your Executive Presence08/01/2022Pass12/01/2022CompletedDownload19Stress Management02/01/2022Pass04/01/2022CompletedDownload18Risk Management01/01/2022Pass04/01/2022CompletedDownload17Business Ethics for the Office25/12/2021Pass28/12/2021CompletedDownload16Business Etiquette26/11/2021Pass29/11/2021CompletedDownload16Business Etiquette10/11/2021Re-submit11/11/2021RejectedDownload15Administrative Skills06/11/2021Pass08/11/2021CompletedDownload14Communication Skills23/10/2021Pass25/10/2021CompletedDownload13Negotiation Techniques09/10/2021Pass12/10/2021CompletedDownload12Creative Thinking and Innovation03/10/2021Pass04/10/2021CompletedDownload11Managing Time02/10/2021Pass04/10/2021CompletedDownload10Managing Change26/09/2021Pass27/09/2021CompletedDownload9Human Resources Management25/09/2021Pass27/09/2021CompletedDownload8Succession Planning28/08/2021Pass01/09/2021CompletedDownload7Performance Management07/08/2021Pass10/08/2021CompletedDownload6Motivating Employees08/05/2021Pass10/05/2021CompletedDownload5Building a Better Team02/05/2021Pass03/05/2021CompletedDownload4Building a Strong Customer Care Team30/04/2021Pass03/05/2021CompletedDownload3Strategic Planning28/03/2021Pass30/03/2021CompletedDownload2Operations Management02/03/2021Pass09/03/2021CompletedDownload1Introduction to Business Management19/12/2020Pass21/12/2020CompletedDownload'
pattern = r'[A-z a-z]+'
result = re.findall(pattern, data)
print(result)

mylist = deque(list(dict.fromkeys(result)))
mylist.reverse()
mylist.remove('Pass')
mylist.remove('Re')
mylist.remove('submit')
mylist.remove('CompletedDownload')
mylist.remove('RejectedDownload')
print(mylist)

file1 = open(r'./mid_exam_fundamentals/course_predmets.txt', 'w')
for predmet in mylist:
        file1.write(predmet+'\n')

file1.close()

