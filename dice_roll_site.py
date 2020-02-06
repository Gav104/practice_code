import time
import mechanicalsoup

browser = mechanicalsoup.Browser()

for i in range(4):
    page = browser.get("http://olympus.realpython.org/dice")
    tag = page.soup.select("#result")[0]
    time_tag = page.soup.select("#time")
    timer1 = time_tag[0].text
    timer = timer1[: timer1.find(" - ")]

    result = tag.text

    print(f"The result of your dice roll is: {result} @ {timer}")
    time.sleep(4)

    if i < 3:
        time.sleep(4)
