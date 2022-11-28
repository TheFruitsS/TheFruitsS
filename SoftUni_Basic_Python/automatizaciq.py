import webbrowser as wbb


def web_automation():
    chrome_path = '/usr/bin/google-chrome-stable %s'

#/usr/bin/google-chrome-stable %U zamenqm s %s za da se izpalni komandata
    urls = ('apple.com', 'github.com', 'google.com', 'bbc.com', 'stackoverflow.com')

    for url in urls:
        print('Opening: ' + url)
        wbb.get(chrome_path).open(url)


web_automation()
# def e funkciq funkciqta predstavlqva kutiika
# kogato napishem as mojem da zamenim imeto s drugo
