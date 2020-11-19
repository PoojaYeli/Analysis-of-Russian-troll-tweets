import csv
import random
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)
    return sentiment_dict

if __name__ == "__main__":

    counts = 0
    tweet_data = {}
    count = 0
    # while counts != 13:
    #     counts = counts + 1
    #     with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_"+str(counts)+".csv", errors='ignore')as f:
    with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\tweets_13.csv",
    # with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\final_kmeans_data.csv",
              errors='ignore')as f:
        data_nodes = csv.reader(f)
        # for nodes in data_nodes:
        #     count = count + 1
        #     content = nodes[1]
        #     sentiment_dict = sentiment_scores(content)
        #     sentiment_value = sentiment_dict['compound']
        #
        #     if sentiment_dict['compound'] >= 0.05:
        #         tweet_sentiment = "positive"
        #         # sentiment_value = sentiment_dict['compound']
        #     elif sentiment_dict['compound'] <= - 0.05:
        #         tweet_sentiment = "negative"
        #         # sentiment_value = sentiment_dict['compound']
        #     else:
        #         tweet_sentiment = "neutral"
        #         # sentiment_value = sentiment_dict['compound']
        #     tweet_data[count] = []
        #     tweet_data[count].append(tweet_sentiment)
        #     tweet_data[count].append(sentiment_value)

        for nodes in data_nodes:
            count = count + 1
            tweet_data[count] = []
            # if :
            if "unknown" == nodes[3].lower() or count == 1:
                content = nodes[2]
                tweet_sentiment = ""
                sentiment_value = 0
                tweet_data[count].append(nodes[1])  # author
                tweet_data[count].append(content)   # content
                tweet_data[count].append(nodes[3])  # region
                tweet_data[count].append(nodes[4])  # language
                tweet_data[count].append(nodes[5])  # published date
                tweet_data[count].append(nodes[7])  # following
                tweet_data[count].append(nodes[8])  # followers
                tweet_data[count].append(nodes[10]) # post_ype->retweet
                tweet_data[count].append(nodes[16]) # tweet_id
            else:
                content = nodes[2] + nodes[3]
                tweet_data[count].append(nodes[1])  # author
                tweet_data[count].append(content)  # content
                tweet_data[count].append(nodes[4])  # region
                tweet_data[count].append(nodes[5])  # language
                tweet_data[count].append(nodes[6])  # published date
                tweet_data[count].append(nodes[8])  # following
                tweet_data[count].append(nodes[9])  # followers
                tweet_data[count].append(nodes[11])  # post_ype->retweet
                tweet_data[count].append(nodes[17])  # tweet_id

            if count != 1:
                sentiment_dict = sentiment_scores(content)
                sentiment_value = sentiment_dict['compound']

                if sentiment_dict['compound'] >= 0.05:
                    tweet_sentiment = "positive"
                    # sentiment_value = sentiment_dict['compound']
                elif sentiment_dict['compound'] <= - 0.05:
                    tweet_sentiment = "negative"
                    # sentiment_value = sentiment_dict['compound']
                else:
                    tweet_sentiment = "neutral"
                    # sentiment_value = sentiment_dict['compound']
            else:
                tweet_sentiment = "tweet sentiment"
            tweet_data[count].append(tweet_sentiment)
            tweet_data[count].append(sentiment_value)

    # print(len(tweet_data))
    # random_index = []
    # for x in range(10000):
    #     # random_index[x] = []
    #     random_index.append(random.randint(1,len(tweet_data)))
    #     # random_index.append(random.randint(1,243877))
    # # print(random_index)
    # random_tweet_data = {}
    # c = 0
    # for indv in random_index:
    #     c = c + 1
    #     # random_tweet_data[c] = []
    #     random_tweet_data[c] = (tweet_data[indv])
    # print(len(random_tweet_data))
    #
    # with open('C:\\Users\\pujav\\PycharmProjects\\opti\\RussianTrollDataMining\\Data\\tweet_final_sentiment.csv', 'w',
    with open('C:\\Users\\pujav\\PycharmProjects\\opti\\RussianTrollDataMining\\Data\\tweets_13_write.csv', 'w',
              newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for tweet_indv in tweet_data:
            spamwriter.writerow(tweet_data[tweet_indv])

# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
# # import pandas as pd
# from matplotlib import pyplot as plt
# from sklearn.datasets.samples_generator import make_blobs
# from sklearn.cluster import KMeans
# import csv
# import random
# from datetime import datetime, time as datetime_time, timedelta
# # from numpy.random import random
#
# max_time_min = 1439
# mean = 0
# max_frequency = 35393
# #morning-> 0.0-0.5(00:00-11:59)
# #afternoon-> 0.5-0.75(12:00-17:59)
# #evening-> 0.75-1.0(18:00-23:59)
#
# def time_diff(start, end):
#     if isinstance(start, datetime_time): # convert to datetime
#         assert isinstance(end, datetime_time)
#         start, end = [datetime.combine(datetime.min, t) for t in [start, end]]
#     if start <= end: # e.g., 10:33:26-11:15:49
#         return end - start
#     else: # end < start e.g., 23:55:00-00:25:00
#         end += timedelta(1) # +day
#         assert end > start
#         return end - start
#
# def calculate_mintues_array(list_time):
#     # minutes_list = []
#     # for r in list_time:
#     days, seconds = list_time.days, list_time.seconds
#     hours = days * 24 + seconds // 3600
#     minutes = (seconds % 3600) // 60
#     return minutes + hours * 60
#     # minutes_list.append(final_min)
#     # print(hours, minutes)
#     # return minutes_list
#
# def calculate_mintues(list_time):
#     time_arr = list_time.split(":")
#     final_time = int(time_arr[1]) + (int(time_arr[0]) * 60)
#     return final_time
#
# def normalise_time(time_min):
#     r = float(time_min / max_time_min)
#     return r
#
# def normalise_frequency(time_min):
#     r = float(time_min / max_frequency)
#
#     # r = float(time_min)
#     return r
#
# # X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)
# # plt.scatter(X[:,0], X[:,1])
#
# random_index = []
# for x in range(10000):
#     random_index.append(random.randint(1,9999))
#     # random_index.append(random.randint(1,243877))
#
# X1 = []
# X2 = []
# X3 = []
# count = 0
# published_time_array = []
# with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\final_kmeans_data.csv", errors='ignore')as f:
#     data_nodes = csv.reader(f)
#     for nodes in data_nodes:
#         count = count + 1
#         if count != 1:
#             # published_time = nodes[4].split()
#             # .split(":")[0].isnumeric()
#             # if len(published_time) == 2:
#             #     if published_time[0].split("/")[0].isnumeric():
#             #         if len(published_time[1].split(":")) == 2 and published_time[1].split(":")[0].isnumeric():
#             #             pub_time = published_time[1]
#             # else:
#             #     published_time = nodes[5].split()
#             published_time = ""
#             published_date_time = ""
#             if len(nodes[4].split()) == 2 and nodes[4].split()[0].split("/")[0].isnumeric():
#                 published_time = nodes[4].split()[1]
#                 published_date_time = nodes[4]
#             elif len(nodes[5].split()) == 2 and nodes[5].split()[0].split("/")[0].isnumeric():
#                 published_time = nodes[5].split()[1]
#                 published_date_time = nodes[5]
#             elif len(nodes[6].split()) == 2 and nodes[6].split()[0].split("/")[0].isnumeric():
#                 published_time = nodes[6].split()[1]
#                 published_date_time = nodes[6]
#
#             if published_time != "":
#                 norm_time_in_minutes = normalise_time(float(calculate_mintues(published_time)))
#                 published_time_array.append(published_date_time)
#                 X1.append(np.round(norm_time_in_minutes, 2))
#                 X2.append((float(nodes[10])))
#
#
# # published_time_array = []
# # with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\Data\final_kmeans_data.csv", errors='ignore')as f:
# #     data_nodes = csv.reader(f)
# #     for nodes in data_nodes:
# #         published_time = ""
# #         if len(nodes[4].split()) == 2 and nodes[4].split()[0].split("/")[0].isnumeric():
# #             published_time = nodes[4]
# #         elif len(nodes[5].split()) == 2 and nodes[5].split()[0].split("/")[0].isnumeric():
# #             published_time = nodes[5]
# #         elif len(nodes[6].split()) == 2 and nodes[6].split()[0].split("/")[0].isnumeric():
# #             published_time = nodes[6]
# #
# #         if published_time != "":
# #             published_time_array.append(published_time)
#
# # X3 = []
# date_sorted = sorted(published_time_array, key=lambda x: datetime.strptime(x, '%m/%d/%Y %H:%M'))
# last_date = ''
# for datetime_indv in date_sorted:
#     if len(datetime_indv.split()) == 2:
#         if last_date:
#             # X3.append((float(calculate_mintues_array(time_diff(datetime.strptime(last_date, '%m/%d/%Y %H:%M'), datetime.strptime(datetime_indv, '%m/%d/%Y %H:%M'))))))
#             X3.append(np.round(normalise_frequency(float(calculate_mintues_array(time_diff(datetime.strptime(last_date, '%m/%d/%Y %H:%M'), datetime.strptime(datetime_indv, '%m/%d/%Y %H:%M'))))), 2))
#         last_date = datetime_indv
# if len(X3) != 9999:
#     X3.remove(max(X3))
#     X3.remove(max(X3))
#     X3.append(0)
#     X3.append(0)
#     X3.append(0)
#
# X = np.column_stack((X1,X2,X3))
# # X = np.column_stack((X1,X2))
#
#
#
# kmeans = KMeans(n_clusters=6, init='k-means++', max_iter=3000, n_init=10, random_state=0)
# kmeans.fit_predict(X)
# y_kmeans = kmeans.predict(X)
# community_X_array = {}
# # test_array["cluster0"] = []
# index = 0
# # community_X_array["test"] = {}
# # community_X_array["test"]["i"] = 9
# # community_X_array["test"]["j"] = 8
# while index != len(X):
#     curr_cluster_name = "cluster"+str(y_kmeans[index])
#     if curr_cluster_name not in community_X_array:
#         # community_X_array[curr_cluster_name] = {}
#         community_X_array[curr_cluster_name] = {}
#         community_X_array[curr_cluster_name]["X1"] = []
#         community_X_array[curr_cluster_name]["X2"] = []
#         community_X_array[curr_cluster_name]["X3"] = []
#         community_X_array[curr_cluster_name]["X1"].append(X1[index])
#         community_X_array[curr_cluster_name]["X2"].append(X2[index])
#         community_X_array[curr_cluster_name]["X3"].append(X3[index])
#     else:
#         community_X_array[curr_cluster_name]["X1"].append(X1[index])
#         community_X_array[curr_cluster_name]["X2"].append(X2[index])
#         community_X_array[curr_cluster_name]["X3"].append(X3[index])
#     index = index + 1
# # for indv in np.unique(community_X_array):
# # print(community_X_array["cluster0"]["X1"])
# fig = plt.figure()
# # axes = fig.add_subplot(111)
# axes = fig.add_subplot(111, projection='3d')
# # axes.scatter(X1, X2, c=y_kmeans, s=50, cmap='viridis')
# # for ind_c in y_kmeans:
# # colors = ["0","1","2","3","4","5","6","7","8"]
# # color = ['yellow', 'green', 'blue', 'brown', 'pink', 'grey', 'purple', 'cucumber', 'pine']
# # for g in color:
# #     ix = np.where(y_kmeans_np == g)
# #     # ax.scatter(scatter_x[ix], scatter_y[ix], c = cdict[g], label = g, s = 100)
# #     print(ix)
# # coun = 0
# # for indv in community_X_array:
# #     axes.scatter(community_X_array[indv]["X1"], community_X_array[indv]["X2"],
# #                  community_X_array[indv]["X3"], c=color[coun], s=50, cmap='viridis', label="community"+str(coun))
# #
# # legend1 = axes.legend(*scatter.legend_elements(),
# #                     loc="lower left", title="Classes")
# # axes.add_artist(legend1)
# axes.legend(loc='upper left', fontsize=15)
# # axes.scatter(X1, X2_random, X1_random, c=y_kmeans, s=50, cmap='viridis')
# # # plt.scatter(X[:,0], X[:,1], c="g")
# # axes.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='y')
# axes.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], kmeans.cluster_centers_[:, 2], s=300, c='red')
# axes.set_xlabel('Tweeted time in minutes', fontsize=20, labelpad=15)
# axes.set_ylabel('Setniment value', fontsize=20, labelpad=15)
# axes.set_zlabel('Time difference between tweets', fontsize=20)
# plt.title('k-means clustering', fontsize=20, y=1.08)
# plt.show()