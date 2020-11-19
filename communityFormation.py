# test = {}
    # test[1] = {}
    # test[1][2] = {}
    # test[1][2][3] = []
    # test[1][2][3].append('123')
    # test[1][2][3].append('213')
    # test[1][2][3].append('231')
    # print(test)
import csv
import networkx as nx

if __name__ == '__main__':
    count = 0
    year_morning_tweet = {}
    year_afternoon_tweet = {}
    year_evening_tweet = {}
    morning_tweet = 0  # 12am to 11:59am-> 0-11:59
    afternoon_tweet = 0  # 12pm to 5:59pm-> 12-17:59
    evening_tweet = 0  # 6pm to 11:59pm-> 18-23:59
    outlier = 0

    # form community based on year and time
    while count != 13:
        count = count + 1
        count_str = str(count)
        with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_"+count_str+".csv", errors='ignore')as f:
            data_nodes = csv.reader(f)
            #for csv heading
            outlier = outlier - 1
            for nodes in data_nodes:
                # nodes[5]-> Published date
                if len(nodes[5].split()) == 2:
                    if len(nodes[5].split()[0].split("/")) == 3:
                        year_str = nodes[5].split()[0].split("/")[2]
                        if year_str.isnumeric():
                            year = int(year_str)
                            if year not in year_morning_tweet:
                                year_morning_tweet[year] = 0
                            if year not in year_afternoon_tweet:
                                year_afternoon_tweet[year] = 0
                            if year not in year_evening_tweet:
                                year_evening_tweet[year] = 0
                        else:
                            outlier = outlier + 1
                        hour_str = nodes[5].split()[1].split(":")[0]
                        if hour_str.isnumeric():
                            hour = int(hour_str)
                            if hour <= 11:
                                # morning_tweet = morning_tweet + 1
                                year_morning_tweet[year] = year_morning_tweet[year] + 1
                            elif hour >= 12 and hour <= 17:
                                afternoon_tweet = afternoon_tweet + 1
                                year_afternoon_tweet[year] = year_afternoon_tweet[year] + 1
                            elif hour >= 18 and hour <= 23:
                                evening_tweet = evening_tweet + 1
                                year_evening_tweet[year] = year_evening_tweet[year] + 1
                        else:
                            outlier = outlier + 1
                    else:
                        outlier = outlier + 1
                else:
                        outlier = outlier + 1
    print(year_morning_tweet)
    print(year_afternoon_tweet)
    print(year_evening_tweet)
    print(outlier)

    # 15, 16, 17
    # 330789, 283489, 283489, 407919, 446277, 259700, 397051, 300702, 255666
    # 12, 13, 14, 18
    # 162, 240, 84, 85,61, 53, 2770, 4501, 442, 2462, 579, 4192

    #total number of tweets
    total_morning_tweets = sum(year_morning_tweet.values())
    total_afternoon_tweets = sum(year_afternoon_tweet.values())
    total_evening_tweets = sum(year_evening_tweet.values())
    print("toatl morning tweets:", total_morning_tweets)
    print("toatl afternoon tweets:", total_afternoon_tweets)
    print("toatl evening tweets:", total_evening_tweets)
    print("toatl tweets:", total_morning_tweets + total_afternoon_tweets + total_evening_tweets)

    # total, outlier, total_mor, total_aft, total_eve
    # 2902634, 43573,  1141238, 1035849, 725547

    #form community based on time
    # while count != 13:
    #     count = count + 1
    #     count_str = str(count)
    #     with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_"+count_str+".csv", errors='ignore')as f:
    #         # C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining
    #         data_nodes = csv.reader(f)
    #         #for csv heading
    #         outlier = outlier - 1
    #         for nodes in data_nodes:
    #             # nodes[5]-> Published date
    #             if len(nodes[5].split()) == 2:
    #                 year_str = nodes[5].split("/")[0]
    #                 hour_str = nodes[5].split()[1].split(":")[0]
    #                 # print(hour.isnumeric())
    #                 if hour_str.isnumeric():
    #                     hour = int(hour_str)
    #                     if hour <= 11:
    #                         morning_tweet = morning_tweet + 1
    #                     elif hour >= 12 and hour <= 17:
    #                         afternoon_tweet = afternoon_tweet + 1
    #                     elif hour >= 18 and hour <= 23:
    #                         evening_tweet = evening_tweet + 1
    #                 else:
    #                     outlier = outlier + 1
    #             else:
    #                 outlier = outlier + 1
            # print("morning", count, ":", morning_tweet)
            # print("afternoon", count, ":", afternoon_tweet)
            # print("evening", count, ":", evening_tweet)
            # print("outlier", count, ":", outlier)

    # print("morning:", morning_tweet)
    # print("afternoon:", afternoon_tweet)
    # print("evening:", evening_tweet)
    # print("outlier:", outlier)