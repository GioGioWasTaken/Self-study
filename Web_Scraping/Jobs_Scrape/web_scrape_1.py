from bs4 import BeautifulSoup
import requests
import time
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=electrical+engineering&txtLocation=').text
soup=BeautifulSoup(html_text,"lxml")
jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
print('This list was made out of the site "timesjobs.com"')
def find_jobs():
    for index, job in enumerate(jobs):
     company_name=job.find('h3',class_="joblist-comp-name").text.replace(' ','').replace('(MoreJobs)','*Check the site for more job opportunities in this company')
     skills=job.find('span',class_="srp-skills").text.replace('  ,',',')
     date_published=job.find('span',class_="sim-posted").span.text
     more_info=job.header.h2.a['href']
     if 'few' in date_published:
         with open(f'job_posts/{index}.txt','w') as f:
          f.write(f'''Company name:{company_name.strip()}\nRequired skills:{skills.strip()}\nThis job offer was posted recently\nMore info:{more_info}
        ''') #makes files for each job with the above details.
if __name__=='__main__':
    while True:
        find_jobs()
        time_wait=10 #change the value of time wait to get a minute number, 10 time 60 sec(min)= 10mins etc.
        print(f'Waiting {time_wait} minutes')
        time.sleep(time_wait*60)