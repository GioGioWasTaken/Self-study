#Read the README.md file in the github repository
from bs4 import BeautifulSoup
from datetime import datetime
import requests
timern=datetime.now()
timern_h=timern.strftime("%H")
timern_d=timern.day
#print("The current time is:",timern_d,type(timern_d))
html_text=requests.get('https://weather.com/weather/tenday/l/15f2041e80f76f962e3ee2654983dbdec946f91bd000dfe7efd08a8fadbb909d')
soup=BeautifulSoup(html_text.text,"lxml")
ten_d_forecast=soup.find_all('div',class_="DailyForecast--DisclosureList--nosQS")
for day in ten_d_forecast:
 rain_stat=day.find('div',class_="DaypartDetails--Content--2Yg3_ DaypartDetails--contentGrid--2_szQ").find('span',class_="DailyContent--value--1Jers").text
 if '%' in rain_stat:
  rain_stat= int(rain_stat.replace('%',''))
  #print((rain_stat),type(rain_stat))
 rain_stat_night=day.find('div',class_="DaypartDetails--Content--2Yg3_ DaypartDetails--contentGrid--2_szQ").find_all('span',class_="DailyContent--value--1Jers")[-2].text
 rain_stat_night= int(rain_stat_night.replace('%',''))
 date=day.find('span',class_="DailyContent--daypartDate--3VGlz").text
 #print(date)
 Remove_Day = ['Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu']
 for o in Remove_Day:
  date=date.replace(o,'')
 date=int(date)
 def day_wea():
  if rain_stat<=50:
     print(f"There's no need to take an umbrella today, as the chance it'll rain is {rain_stat}%.")
  else:
     print(f"There's a {rain_stat}% chance it'll rain today. Please, take an umbrella")
     return
 def night_wea():
   if rain_stat_night <= 50:
    print( f"There's no need to take an umbrella this evening, as the chance it'll rain is {rain_stat_night}%." )
   else:
    print( f"There's a {rain_stat_night}% chance it'll rain tonight. Please, take an umbrella.")
    return
 if timern_d == date:
    if int(timern_h) >= 17:
        night_wea()
    else:
        day_wea()
