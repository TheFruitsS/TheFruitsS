import re
data_times = int(input())



data1 = []

for _ in range(data_times+1):
    datas = input()
    data1.append(datas)

    regex = r'(^[A-Z][a-z]{3,}\s[A-Z][a-z]{3,})#{1,}([A-Z][a-z]+[[&]?[[A-z]+]?){0,2}(\d{2}[A-z]+\d*\s{1}[JSC|Ltd.]+)'

    data_process = re.search(regex, datas).groups()
    if data_process:
        print(data_process)
    else:
        continue


