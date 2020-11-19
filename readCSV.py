import csv
import matplotlib.pyplot as plt

# colors = ['tan', 'red', 'lime', 'grey', 'orange', 'blue', 'green', 'yellow', 'brown', 'violet', 'aqua', 'coral', 'navy']
hashtag_count = {}
positive_count = "positive_count"
negative_count = "negative_count"
neutral_count = "neutral_count"
hashtag_positive_count = {}
hashtag_negative_count = {}
hashtag_neutral_count = {}

if __name__ == "__main__":
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1])
    # maga 15536
    # local 26088
    # tcot 15458
    # news 131030
    # sports 48846
    # politics 39858
    # topnews 15149
    # world 27622
    langs = ['#maga', '#local', '#tcot', '#news', '#sports', '#politics', '#topnews', '#world']
    students = [15536, 26088, 15458, 131030, 48846, 39858, 15149, 27622]
    ax.bar(langs, students, align='center', alpha=0.5)
    ax.set_xticks('number of tweets')
    ax.set_xticklabels('Hashtags')
    # plt.ylabel('number of tweets')
    # plt.xlabel('Hashtags')
    plt.title('Trending tweets')
    plt.show()
    # with open(r"C:\Users\pujav\PycharmProjects\opti\RussianTrollDataMining\sentimentAnalysisOutput1.csv", errors='ignore')as f:
    #     data_nodes = csv.reader(f)
    #     for nodes in data_nodes:
    #         hashtag = nodes[0]
    #         if hashtag not in hashtag_positive_count:
    #             hashtag_positive_count[hashtag] = int(nodes[2])
    #         else:
    #             hashtag_positive_count[hashtag] = hashtag_positive_count[hashtag] + int(nodes[2])
    #         if hashtag not in hashtag_negative_count:
    #             hashtag_negative_count[hashtag] = int(nodes[4])
    #         else:
    #             hashtag_negative_count[hashtag] = hashtag_negative_count[hashtag] + int(nodes[4])
    #         if hashtag not in hashtag_neutral_count:
    #             hashtag_neutral_count[hashtag] = int(nodes[6])
    #         else:
    #             hashtag_neutral_count[hashtag] = hashtag_neutral_count[hashtag] + int(nodes[6])
    #
    # hashtag_max_pos_neg = {}
    # hashtag_max_neutral = {}
    # if len(hashtag_negative_count) == len(hashtag_positive_count) and len(hashtag_positive_count) == len(hashtag_neutral_count):
    #     for indv in hashtag_positive_count:
    #         if hashtag_positive_count[indv] == hashtag_negative_count[indv] and hashtag_positive_count[indv] != 0:
    #             print(indv, hashtag_positive_count[indv], hashtag_neutral_count[indv])
    #             hashtag_max_pos_neg[indv] = hashtag_positive_count[indv]
    #             hashtag_max_neutral[indv] = hashtag_neutral_count[indv]
    # else:
    #     print("Not equal")
    # for indvp in hashtag_max_pos_neg:
    #     if hashtag_max_pos_neg[indvp] > 100:
    #     # if hashtag_max_pos_neg[indvp] == max(hashtag_max_pos_neg.values()):
    #         print("max equal-pos:", indvp, hashtag_max_pos_neg[indvp])
    #         print("max equal-neu", indvp, hashtag_max_neutral[indvp])

    # for indv in hashtag_positive_count:
    #     if max(hashtag_positive_count.values()) == hashtag_positive_count[indv]:
    #         print("Max positive:", indv, max(hashtag_positive_count.values()))
    # for indv in hashtag_negative_count:
    #     if max(hashtag_negative_count.values()) == hashtag_negative_count[indv]:
    #         print("Max negative:", indv, max(hashtag_negative_count.values()))
    # for indv in hashtag_neutral_count:
    #     if max(hashtag_neutral_count.values()) == hashtag_neutral_count[indv]:
    #         print("Max neutral:", indv, max(hashtag_neutral_count.values()))
