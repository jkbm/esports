import requests
from bs4 import BeautifulSoup
from .models import Match, Tournament, Player

def addHTC2016():
    data = requests.get("http://www.gosugamers.net/hearthstone/events/606-2016-hearthstone-world-championship")
    return data

def add_matches():
    page = addHTC2016()
    soup = BeautifulSoup(page.text, 'html.parser')
    matches = soup.find_all(class_='schedule')
    everymatch = []
    for match in matches:
        ais = match.find_all('a')
        contents = {}
        x = 0
        y = 0
        l = []
        for a in ais:
            if x != 3:                
                c = a.contents[0].replace('\r\n',"").replace(' ','').replace('(김천수)', '').replace('(哈姆士郎)', '')
                l.append(c)
                x += 1
            else:
                c = a.contents[0].replace('\r\n',"").replace(' ','').replace('(김천수)', '').replace('(哈姆士郎)', '')
                l.append(c)
                contents[y] = l
                l = []
                y += 1
                x = 0
        everymatch.append(contents) 
    
    for group in everymatch:
        for key, value in group.items():
            print("{0}{1}{2}".format(value[0], value[3], value[2]))
            p1 = Player.objects.get(name=value[0])
            p2 = Player.objects.get(name=value[2])
            score = "{0}-{1}".format(value[3][0],value[3][2])
            print(score)
            m = Match.objects.create(
                date="2016-10-26",
                player1=p1,
                player2=p2,
                score=score,
                format="Bo7",
                stage="Groups",
                finished=True,
                tournament=Tournament.objects.get(pk=13)
                )
