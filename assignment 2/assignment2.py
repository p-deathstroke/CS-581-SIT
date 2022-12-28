# Author: Preet Dabhi
# Purpose :youtube.py searches YouTube for videos matching a search term and max results
# To run from terminal window:   python3 dabhi.py 
from googleapiclient.discovery import build      # use build function to create a  service object
import csv
import sys
# put your API key into the API_KEY field below, in quotes
API_KEY = "AIzaSyCGppa2rPabsC5-PrORhD-8CbmzczdSoyE"
API_NAME = "youtube"
API_VERSION = "v3"       # this should be the latest version

# initializing empty array for storing youtube data
youtubeData = []

youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
   
# search for videos matching search term;
#  retrieve the YouTube records matching search term and max
def youtubeSearch(search_max,search_term):
    youtube = build(API_NAME, API_VERSION, developerKey=API_KEY)
    search_data = youtube.search().list(q=search_term, part="id,snippet",maxResults=search_max).execute()

    headers = ['Video Id', 'Views', 'Likes*', 'Comments*', 'Duration', 'Title']

    # open a file for writing
    video_file = open('youtubeDataFile.csv', 'w', encoding='utf-8')
    # create the csv writer object
    csvWriter = csv.DictWriter(video_file, fieldnames=headers)
    # writes headers to csv
    csvWriter.writeheader()

    print()  
    print('----------------------------------------------------------')  
    print('Video Id, Views, Likes*, Comments*, Duration, Title')
    print('----------------------------------------------------------')
    # search for videos matching search term;
    
    for search_instance in search_data.get("items", []):
        if search_instance["id"]["kind"] == "youtube#video":
        
            videoId = search_instance["id"]["videoId"]  
            title = search_instance["snippet"]["title"]        
            video_data = youtube.videos().list(id=videoId,part="statistics,contentDetails").execute()

            for video_instance in video_data.get("items",[]):
                duration = video_instance["contentDetails"]["duration"] 
                viewCount = video_instance["statistics"]["viewCount"]

                if 'likeCount' not in video_instance["statistics"]:
                    likeCount = 0
                else:
                    likeCount = video_instance["statistics"]["likeCount"]
            
                if 'commentCount' not in video_instance["statistics"]:
                    commentCount = 0
                else:
                    commentCount = video_instance["statistics"]["commentCount"]
        
                # write records in csv file
                csvWriter.writerow({
                    "Video Id" : videoId,
                    "Views" : viewCount,
                    "Likes*" : likeCount,
                    "Comments*" : commentCount,
                    "Duration" : duration,
                    "Title" : title
                })
                # add data to array for analysing
                if viewCount != '0':            
                    youtubeData.append({
                        "Video Id" : videoId,
                        "Views" : viewCount,
                        "Likes*" : likeCount,
                        "Comments*" : commentCount,
                        "Duration" : duration,
                        "Title" : title,
                        "Like Percentage" : 0 if viewCount == '0' else f'{int(likeCount) / int(viewCount) * 100:0.3f}',
                })
            
            # print each record on console              
            print(' | ', videoId, ' | ', f'{int(viewCount):,}', ' | ', f'{int(likeCount):,}', ' | ', f'{int(commentCount):,}', ' | ', duration, ' | ', title)
            # print(youtubeData)
            


def highestLikesPercentageFirst(youtubeData):
# array sorting
    youtubeData.sort(reverse=True, key=lambda x : float(x.get("Like Percentage")))

    print()  
    print('-------------Highest Percentage First-------------')  
    print('Rank, Like Percentage, View count, Like count*, Title')
    print('------------------------------------------------------')

    # printing the data
    for x,rd in enumerate(youtubeData, 1):
        print(str(x), ' | ', rd['Like Percentage'], ' | ', f"{int(rd['Views']):,}", ' | ', f"{int(rd['Likes*']):,}", ' | ', rd['Title'])
        if x == 5:
            break

    # printing only 5 data
    if (len(youtubeData) < 5):
        test = 5 - len(youtubeData)
        
        for y in range(test):
            print(len(youtubeData) + y + 1)

def highestCommentCountFirst(youtubeData):
    youtubeData.sort(reverse=True, key=lambda x : float(x.get("Comments*")))

    print()  
    print('-------------Highest Comments First-------------')  
    print('Rank, View count, Comment count*, Title')
    print('------------------------------------------------------')

    # printing the data
    for x,rd in enumerate(youtubeData, 1):
        print(str(x), ' | ', f"{int(rd['Views']):,}", ' | ', f"{int(rd['Comments*']):,}", ' | ', rd['Title'])
        if x == 5:
            break

    # printing only 5 data
    if (len(youtubeData) < 5):
        test = 5 - len(youtubeData)
        
        for y in range(test):
            print(len(youtubeData) + y + 1)

# user input for search term and maximum number of search results
print('Please enter the number of YouTube records to search')
search_max = input()

print('Please enter the search term')
search_term = input()

# calling the functions
youtubeSearch(int(search_max), search_term)
highestLikesPercentageFirst(youtubeData)
highestCommentCountFirst(youtubeData)