from bs4 import BeautifulSoup
import requests
import time


#name=input("write the type of job you are looking for:")
name="python"
#unaware=input("write the skill you are unaware with:")
unaware="linux"
content= requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtLocation=&txtKeywords="+name).text
soup= BeautifulSoup(content, "lxml")


def jobfinder():
    main_tags= soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    for count,main_tag in enumerate(main_tags,1):
        published= main_tag.find("span", class_="sim-posted").text
        if "few" in published:
            skill= main_tag.find("span", "srp-skills").text.strip().replace(" ", "")
            if unaware not in skill:
                detail= main_tag.find("ul", class_="list-job-dtl clearfix").li
                description= detail.text.strip()[16:-16].replace("  "," ")
                link= detail.a["href"]
                title= main_tag.find("h3", class_= "joblist-comp-name").text.strip().replace(" ", "")
                with open(f"foundjobs/{count}", "w") as file:
                    file.write("NEW JOB: \n")
                    file.write(f"THE TITLE OF THE JOB IS:{title} \n")
                    file.write(f"THE DESCRIPTION OF THE JOB IS:{description} \n")
                    file.write(f"VIWE MORE IN:{link} \n")
                    file.write(f"THE REQUIRED SKILL OF JOB IS:{skill} \n")
                print("###################")
                print("NEW JOB:")
                print(f"THE TITLE OF THE JOB IS:{title}")
                print(f"THE DESCRIPTION OF THE JOB IS:{description}")
                print(f"VIWE MORE IN:{link}")
                print(f"THE REQUIRED SKILL OF JOB IS:{skill}")



if __name__=="__main__":
    while True:
        jobfinder()
        time.sleep(6000)