#imports
from bs4 import BeautifulSoup #used to convert HTML code to python objects
import requests #get HTML code from a website
import time #timer

#filter out jobs with an unwanted skill
print('Which skill do you want to filter out (leave blank to display all job posts)')
filter_out_skill = input('>') #you can use input function but it doesnt workin VScode
print(f'filtering out {filter_out_skill}..')

def find_jobs():
    #get HTML code from a website
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text #insert website URL 
    #print(html_text) #test if the HTML was grabbed

    #used to convert HTML code to python objects
    soup = BeautifulSoup(html_text, 'lxml')
    #print(soup) #test if the soup variable works

    #search HTML to find jobs on page 1
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    #print(jobs) #test if the job variable works

    for index, job in enumerate(jobs):
        #search HTML to find the post date for the job post on page 1
        post_date = job.find('span', class_ = 'sim-posted').text
        #print(post_date) #test if the post_date variable works
        

        if 'few' not in post_date: #post dates that include few are usually taken jobs
            #search HTML to find companies for the job post on page 1
            companies = job.find('h3', class_ = 'joblist-comp-name').text.strip() # strip is used to filter out the whitespace
            #print(companies) #test if the companies variable works

            #search HTML to find skills for the job post on page 1
            skills = job.find('span', class_ = 'srp-skills').text.replace(' ','') # alternative way to filter out the whitespace is to use replace
            #print(skills) #test if the skills variable works
            
            #search HTML to find link for the job post on page 1
            link = job.header.h2.a['href']
            #print(link) #test if the link variable works
            
            #filtering condition
            if filter_out_skill not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f"Company Name: {companies.strip()} \n\n")
                    f.write(f"Skills: {skills.strip()} \n\n")
                    f.write(f'More info: {link}')
                print(f'Files saved {index}')

if __name__ == '__main__': #run file in terminal using commad "python main.py"
    while True:
        find_jobs()
        time_wait = 60 #how many minute do you want the timer to update
        print (f'waiting {time_wait} minutes...')
        time.sleep(time_wait * 60)