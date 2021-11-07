from bs4 import BeautifulSoup
import requests
import re
import csv

urls = ['https://vermontglove.com/glove-shop/the-vermonter',
'https://alpine-luddites.myshopify.com/',
'https://caseknives.com/']

output = [["instagramUrl","facebookUrl","fbLikes","youTubeUrl","twitterUrl"]]

for url in urls:
    fbLikes = None
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")

    instaUrl = content.find(href=re.compile("instagram"))
    if instaUrl != None:
        instaUrl = instaUrl.get('href')
    fbUrl = content.find(href=re.compile("facebook"))
    if fbUrl != None:
        fbUrl = fbUrl.get('href')

        fbResponse = requests.get(fbUrl,timeout=5)
        fbContent = BeautifulSoup(fbResponse.content, "html.parser")
        # print (fbContent)
        fbLikes = fbContent.find('span',attrs={'class':'_52id _50f5 _50f7'})
        if fbLikes != None:
            fbLikes = fbLikes.text

    tubeUrl = content.find(href=re.compile("youtube"))
    if tubeUrl != None:
        tubeUrl = tubeUrl.get('href')
    twitterUrl = content.find(href=re.compile("twitter"))
    if twitterUrl != None:
        twitterUrl = twitterUrl.get('href')
    row = [(instaUrl),(fbUrl),(fbLikes),(tubeUrl),(twitterUrl)]
    output.append(row)


print (output)

    # socialObject = {
    #     "instagram": (instaUrl),
    #     "facebook": (fbUrl),
    #     "fbLikes": (fbLikes),
    #     "youTube": (tubeUrl),
    #     "twitter": (twitterUrl)
    # }
     # print (socialObject)

    # socialObject = {
    #     "facebook": (fbUrl),
    #     "twitter": (twitterUrl),
    #     "instagram": (instaUrl)
    # }
   
    
    # print(str(instaUrl) + '\t' + str(fbUrl) + '\t' + str(tubeUrl) + '\t' + str(twitterUrl)) 
    
    # print (fbUrl.get('href'))
    

# d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 jq4qci2q a3bd9o3v b1v8xokw oo9gr5id
# d2edcug0 hpfvmrgz qv66sw1b c1et5uql oi732d6d ik7dh3pa ht8s03o8 jq4qci2q a3bd9o3v b1v8xokw oo9gr5id