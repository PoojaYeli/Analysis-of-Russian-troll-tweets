import csv
from datetime import datetime, time as datetime_time, timedelta
import re
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
plt.style.use('seaborn-deep')

# def days_between(d1, d2):
#     d1 = datetime.strptime(d1, "%m/%d/%Y")
#     d2 = datetime.strptime(d2, "%m/%d/%Y")
#     return abs((d2 - d1).days)

def remove_max_hashtag(d, key):
    r = dict(d)
    del r[key]
    return r

def time_diff(start, end):
    if isinstance(start, datetime_time): # convert to datetime
        assert isinstance(end, datetime_time)
        start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
    if start <= end: # e.g., 10:33:26-11:15:49
        return end - start
    else: # end < start e.g., 23:55:00-00:25:00
        end += timedelta(1) # +day
        assert end > start
        return end - start

def calculate_mintues(list_time):
    # minutes_list = []
    # for r in list_time:
    days, seconds = list_time.days, list_time.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    return minutes + hours * 60
    # minutes_list.append(final_min)
    # print(hours, minutes)
    # return minutes_list

if __name__ == '__main__':

    # hashtag_all = {}
    hashtag_all = ["#maga", "#tcot", "#news", "#world", "#sports", "#topnews", "#politics", "#local"]
    # hashtag_all = ["#fakenews"]
    # hashtag_all = ["#thingsmoretrustedthanhillary", "#cosproject"]
    hashtag_all_count = {}
    trending_hashtags = {}
    count = 0
    published_datetime_maxhashtag = []
    vnb = '#FakeNews'
    # temp = "#[a-zA-Z0-9_]+"

    # while count != 13:
    #     count = count + 1
        # with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweetedtime_test.csv", errors='ignore')as f:
    with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_1.csv", errors='ignore')as f:
    # with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_"+str(count)+".csv", errors='ignore')as f:
        data_nodes = csv.reader(f)
        for nodes in data_nodes:
            date_time = nodes[5]
            for htag in nodes[2].split():
                if htag.startswith("#"):
                    htag_lowercase = re.sub(r"(\W+)$", "", htag.lower())
                    if htag_lowercase in hashtag_all:
                        if htag_lowercase not in hashtag_all_count:
                            hashtag_all_count[htag_lowercase] = 1
                        else:
                            hcount = hashtag_all_count[htag_lowercase] + 1
                            hashtag_all_count[htag_lowercase] = hcount
                        if date_time.split()[0].split("/")[0].isnumeric():
                            if htag_lowercase not in trending_hashtags:
                                trending_hashtags[htag_lowercase] = []
                                trending_hashtags[htag_lowercase].append(date_time)
                            else:
                                trending_hashtags[htag_lowercase].append(date_time)

                    # htagcopy = htag
                    # if htagcopy.lower() == '#news':
                    #     if date_time.split()[0].split("/")[0].isnumeric():
                    #         published_datetime_maxhashtag.append(date_time)
                    # if htagcopy is '#news':

            for ctag in nodes[3].split():
                if ctag.startswith("#"):
                    ctag_lowercase = re.sub(r"(\W+)$", "", ctag.lower())

                    if ctag_lowercase in hashtag_all:
                        if ctag_lowercase not in hashtag_all_count:
                            hashtag_all_count[ctag_lowercase] = 1
                        else:
                            hcount = hashtag_all_count[ctag_lowercase] + 1
                            hashtag_all_count[ctag_lowercase] = hcount
                        if nodes[6].split()[0].split("/")[0].isnumeric():
                            if ctag_lowercase not in trending_hashtags:
                                trending_hashtags[ctag_lowercase] = []
                                trending_hashtags[ctag_lowercase].append(nodes[6])
                            else:
                                trending_hashtags[ctag_lowercase].append(nodes[6])

                            # ctagcopy = ctag
                            # if ctagcopy.lower() == "#news":
                            #     if nodes[6].split()[0].split("/")[0].isnumeric():
                            #         published_datetime_maxhashtag.append(nodes[6])

    # print(hashtag_all)
    # trending_hashtags = {}
    # max_hashtag = max(hashtag_all, key=hashtag_all.get)
    # print("MAX:", max_hashtag, hashtag_all[max_hashtag])
    # for indv in hashtag_all_count:
        # if indv == "#thingsmoretrustedthanhillary" or indv == "#cosproject":
        # if hashtag_all_count[indv] > 15000:
        #     print(indv, hashtag_all_count[indv])

            # trending_hashtags[indv] = hashtag_all_count[indv]
    # second_max = remove_max_hashtag(max_hashtag)
    # second_max_hashtag = max(second_max, key=second_max.get)
    # print(second_max_hashtag, second_max[second_max_hashtag])
    #
    # print(published_datetime_maxhashtag)
    # print(len(published_datetime_maxhashtag))
    # for indv in trending_hashtags:
    #     print(indv, len(trending_hashtags[indv]))
    # date_sorted = sorted(published_datetime_maxhashtag, key=lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))

    # timediffminutes_pjnet = []
    # timediffminutes_maga = []
    # timediffminutes_local = []
    # timediffminutes_topnews = []
    # timediffminutes_0 = []
    # timediffminutes_politics = []
    # timediffminutes_blacklivesmatter = []
    # timediffminutes_business = []
    # timediffminutes_world = []
    # timediffminutes_tcot = []
    # timediffminutes_news = []
    # timediffminutes_health = []
    # timediffminutes_sports = []


    # print(max(hashtag_all_count.values()))
    time_diff_minutes = []
    all_time_diff_minutes = []
    all_trending_hashtags = []
    for indv_hashtag in trending_hashtags:
        time_diff_minutes = []
        date_sorted = sorted(trending_hashtags[indv_hashtag], key=lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))
        last_date = ''
        for datetime_indv in date_sorted:
            if len(datetime_indv.split()) == 2:
                if last_date:
                    time_diff_minutes.append(calculate_mintues(time_diff(datetime.strptime(last_date, '%m/%d/%Y %H:%M'), datetime.strptime(datetime_indv, '%m/%d/%Y %H:%M'))))
                last_date = datetime_indv
        print(date_sorted)
        # print(time_diff_minutes)
        # print(len(time_diff_minutes))
        # recounted = Counter(time_diff_minutes)
        # print(recounted)
        all_time_diff_minutes.append(time_diff_minutes)
        all_trending_hashtags.append(indv_hashtag)
        print(indv_hashtag, len(time_diff_minutes))
    plt.hist(all_time_diff_minutes, bins=[0,2,4,5,7,9,10,12,14,15,17,19,20,25,30,35,40,45,50,60,70,80,90,100,110,1159],  alpha=0.5,
    # plt.hist(all_time_diff_minutes, bins=[0,2,4,5,7,9,10,12,14,15,17,19,20,25,30,35,40,45,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250],  alpha=0.5,
    #          color=['red', 'black'], label=all_trending_hashtags)
             color=['red', 'orange', 'blue', 'green', 'yellow', 'brown', 'violet', 'navy'], label=all_trending_hashtags)
    # plt.hist(all_time_diff_minutes, bins=[0,2,4,5,7,9,10,12,14,15,17,19,20,25,30,35,40,45,50,60,70,80,90,100,110,1159],  alpha=0.5, color=colors, label=all_trending_hashtags)
    # plt.hist(all_time_diff_minutes, bins=[0,1,2,3,4,5,6,7,8,9,10,15,20,25,30,35,40,45,50,1159])
    plt.ylabel('Tweets')
    plt.xlabel('Frequency')
    plt.title('Distribution of trending tweets')
    plt.legend(loc='upper right')
    plt.show()



    # Extract date; eg- 10/1/2017 19:58-> mm/dd/yyyy hh:mm
    # pub_clone = {}
    # for data in published_datetime_maxhashtag:
    #     data_split = data.split()
    #     if len(data_split) == 2:
    #         time = data_split[1]
    #         data_date_split = data_split[0].split("/")
    #         if len(data_date_split) == 3:
    #             # year = data_date_split[2]
    #             if data_date_split[2].isnumeric():
    #                 year = int(data_date_split[2])
    #                 month = int(data_date_split[0])
    #                 date = int(data_date_split[1])
    #                 # time = data_split[1]
    #                 if year not in pub_clone:
    #                     pub_clone[year] = {}
    #                 if month not in pub_clone[year]:
    #                     pub_clone[year][month] = {}
    #                 if date not in pub_clone[year][month]:
    #                     pub_clone[year][month][date] = []
    #                 pub_clone[year][month][date].append(time)
    # # print(pub_clone)

    # Sorting the dict and taking difference
    # full_time_diff_in_minutes = []
    # time_list = []
    # time_list_last_element = ''
    # date_sorted = dict(sorted(pub_clone.items()))
    # for year_clone in date_sorted:
    #     for month_clone in date_sorted[year_clone]:
    #         for day_clone in date_sorted[year_clone][month_clone]:
    #             date_sorted[year_clone][month_clone][day_clone] = sorted(pub_clone[year_clone][month_clone][day_clone], key=lambda x: (len(x), x))
    #             time_list = date_sorted[year_clone][month_clone][day_clone]
    #             print(time_list)
    #             time_diff_list = []
    #             if len(time_list) == 1:
    #                 # if datetime.strptime(time_list_last_element, '%H:%M') > datetime.strptime(time_list[0], '%H:%M'):
    #                 #     time_diff_list = [datetime.strptime(time_list[0], '%H:%M') - datetime.strptime(time_list_last_element, '%H:%M')]
    #                 # else:
    #                     time_diff_list = [datetime.strptime(time_list_last_element, '%H:%M') - datetime.strptime(time_list[0], '%H:%M')]
    #                     # time_diff_list = [datetime.strptime(time_list_last_element, '%H:%M') - datetime.strptime(time_list[0], '%H:%M')]
    #             else:
    #                 time_diff_list = [datetime.strptime(time_list[i + 1], '%H:%M') - datetime.strptime(time_list[i], '%H:%M') for i in range(len(time_list) - 1)]
    #             # full_time_diff_in_minutes.append(calculate_mintues(time_diff_list))
    #             print(calculate_mintues(time_diff_list))
    #             # res = [[i + 1] - date_sorted[year_clone][month_clone][day_clone][i] for i in range(len(date_sorted[year_clone][month_clone][day_clone]) - 1)]
    #             # print(date_sorted)
    #             time_list_last_element = max(time_list)
    #         # print(time_list_last_element)
    # print(full_time_diff_in_minutes)
    # # Taking time difference
    # # for yr in date_sorted:
    # #     for mon in date_sorted[yr]:
    # #         for day in date_sorted[yr][mon]:

