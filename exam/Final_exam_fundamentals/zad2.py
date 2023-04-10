import re
data_times = int(input())



data1 = []

for _ in range(data_times+1):
    datas = input()
    data1.append(datas)

    regex = r'(^[A-Z][a-z]{3,}\s[A-Z][a-z]{3,})#{1,}([A-z]+&?[[A-Za-z]+]?&?[A-Za-z]+)(\d{2}\w*\s*\d*[Ltd.|JSC]+)'

    data_process = re.findall(regex, datas)
    if data_process:
        print(data_process)
    else:
        continue


