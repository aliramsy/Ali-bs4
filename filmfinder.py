from bs4 import BeautifulSoup
import requests



def finding_movie():
    name=input("type the name of the movie:").replace(" ","+")
#print(name)
    page_link=f"https://www.film2movie.asia/search/{name}"
    print(page_link)
    content=requests.get(page_link).text
    soup=BeautifulSoup(content, "lxml")
    main_tags=soup.find_all("div", class_="content")
    for main_tag in main_tags:
        detail=main_tag.find("a", class_="more-link")
        link=detail["href"]
        print("this is the link of the whole page:")
        print(link)
        return link
        

finding_movie()

#def finding_link():
#    name=finding_movie()
#    content=requests.get(name).text
#    soup=BeautifulSoup(content, "lxml")
#    main_tag=soup.find("div", class_="content")
#    first_details=main_tag.find_all("p")
#
#    for first_detail in first_details:
#        #description=first_detail.find("strong")
#        second_detail=first_detail.find("a")
#        try:
#            third_detail=second_detail["href"]
#            #print(description)
#            #print(third_detail)
#        except:
#            continue
#        #if "ref" not in third_detail and "redirect" not in third_detail: 
#            #print(third_detail)
#        print(third_detail)
#finding_link()