#!/usr/bin/python3
import pandas as pd
import numpy as np
import scipy.stats as stats
from sklearn.metrics import r2_score
# Import required libraries
from scipy.stats import kendalltau
import matplotlib.pyplot as plt
import seaborn as sns
import time, datetime
import sys

sns.set_style("whitegrid")

for file in sys.argv[1:]:
    line_coverage = {}
    branch_coverage = {}
    bugs_found_dict = {}
    line_sum = 0
    line_cov = 0
    branch_sum = 0
    branch_cov = 0
    bugs_found = 0
    timestamp = 0
    with open(file, "r") as f: 
        
        cur_time = 0
        for line in f.readlines():
            data_list = line.split(" ")
            timestamp = int(data_list[0])
            if timestamp != cur_time:
                timeArray = time.localtime(cur_time)
                otherStyleTime = time.strftime("%m--%d %H:%M", timeArray)
                print(otherStyleTime)
                if cur_time != 0:
                    line_coverage[cur_time] = line_cov / line_sum
                    branch_coverage[cur_time] = branch_cov / branch_sum
                    print("line coverage", line_coverage[cur_time], "lin_cov", line_cov, "line_sum", line_sum)
                    print("branch coverage", branch_coverage[cur_time], "branch_cov", branch_cov, "line_sum", branch_sum)
                bug_info = (" ").join(data_list[1:])
                if bug_info.find("No samples found") != -1:
                    bugs_found = 0
                elif bug_info.find("Successfully indexed") != -1:
                    bugs_found = int(data_list[3])
                bugs_found_dict[cur_time] = bugs_found
                cur_time = timestamp
                line_sum = 0
                line_cov = 0
                branch_sum = 0
                branch_cov = 0
                bugs_found = 0
                continue
            if data_list[2].find("executed") != -1:
                per = data_list[2].split(":")[-1]
                per = float(per[:per.find("%")])
                sum = float(data_list[-1])
            if data_list[1] == "Lines":
                line_cov += sum * (per / 100)
                line_sum += sum
                # print("line_cov", line_cov)
                # print("line_sum", line_sum)
            if data_list[1] == "Branches":
                branch_cov += sum * (per / 100)
                branch_sum += sum
                # print("branch cov", branch_cov)
                # print("branch sum", branch_sum)
        timeArray = time.localtime(timestamp)
        otherStyleTime = time.strftime("%m--%d %H:%M", timeArray)
        line_coverage[cur_time] = line_cov / line_sum
        branch_coverage[cur_time] = branch_cov / branch_sum
    
    #scatter plot for the dataset
    ax1 = plt.subplot(121)
    ax1.set_xlabel("TimeStamp")
    ax1.set_ylabel("Coverage")

    timestamp = list(line_coverage.keys())
    object_time = int(timestamp[0])
    for k in range(len(timestamp)):
        timestamp[k] = str((int(timestamp[k]) -  object_time) // 60)
    line_coverage_value = line_coverage.values()
    branch_coverage_value = branch_coverage.values()
    print(len(timestamp))
    step = len(timestamp) // 5
    print(type(timestamp))
    print(step)
    p1 = ax1.scatter(timestamp, line_coverage_value, color = 'b')
    p2 = ax1.scatter(timestamp, branch_coverage_value, color = 'r')
    # ax1.set_xticks([0, 20, 40, 60, 80], [timestamp[0], timestamp[20], timestamp[40], timestamp[60], timestamp[80]])
    ax1.legend((p1, p2), ('Line Coverage', 'Branch Coverage'),loc = 'best')
    ax1.set_title((file.split("/")[-1]).split(".")[0])
    plt.xticks([0 * step, 1 * step, 2 * step, 3 * step, 4 * step], [timestamp[0 * step], timestamp[1 * step], timestamp[2 * step], timestamp[3 * step], timestamp[4 * step]], size = 10, rotation = -20)
    ax2 = plt.subplot(122)
    ax2.set_xlabel("TimeStamp")
    ax2.set_ylabel("Bugs Found")
    bugs_found_value = bugs_found_dict.values()
    print(len(timestamp), len(bugs_found_value))
    p3 = ax2.scatter(timestamp, bugs_found_value)
    # ax2.set_xticks([0, 20, 40, 60, 80], [timestamp[0], timestamp[20], timestamp[40], timestamp[60], timestamp[80]])
    ax2.legend([p3], ['Bugs Found'],loc = 'best')
    ax2.set_title(file.split("/")[-1].split(".")[0])
    # labels = ax1.get_xticklabels()
    # plt.setp(labels, rotation=45, horizontalalignment='right')
    plt.xticks([0 * step, 1 * step, 2 * step, 3 * step, 4 * step], [timestamp[0 * step], timestamp[1 * step], timestamp[2 * step], timestamp[3 * step], timestamp[4 * step]], size = 10, rotation = -20)
    plt.show()





# filename = ""
# # df = pd.read_excel(filename)
# X = [1, 2, 3, 4, 5, 6, 7]
# Y = [1, 3, 6, 2, 7, 4, 5]
# '''
# r: Pearson’s correlation coefficient
# p-value: long-tailed p-value
# '''
# pearson_corr = stats.pearsonr(X, Y)
# print("pearson correlation", pearson_corr)

# # Calculating Kendall Rank correlation
# kendall_corr, _ = kendalltau(X, Y)
# print('Kendall Rank correlation: %.5f' % kendall_corr)

# # Calculating R^2 correlation
# # R2= 1- SSres / SStot
# r2 = r2_score(X, Y)
# print('r2 score is', r2)

# #datasets
# decision_effectiveness = [1,2,3,4,5,6,7,8,9]
# coverage_decision = [0, 0.1, 0.12, 0.14, 0.21, 0.25, 0.5, 0.75, 1.00]
# modified_effectiveness = [4,7,4,2,2,5,7,8,9]
# coverage_modified = [0.13, 0.21, 0.43, 0.07, 0.53, 0.31, 0.67, 0.87, 0.25]
# #scatter plot for the dataset\
# # plt.xlabel("Coverage")
# # plt.ylabel("Timeout")

# # p1 = plt.scatter(coverage_decision, decision_effectiveness, color = 'b')
# # p2 = plt.scatter(coverage_modified, modified_effectiveness, color = 'r')
# # plt.legend((p1, p2), ('Decision Coverage', 'Modified Coverage'),loc = 'best')
# # plt.scatter
# # plt.show()

# x1 = [1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,5,6,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9]
# y1 = [4,5,6,6,4,5,6,6,7,2,3,4,5,6,7,8,9,5,4,2,3,4,5,6,7,2,4,5,7,4,3,5,6,8,8,9,3]
# # ax=sns.boxplot(x="day",y="total_bill",hue="smoker",data=tips,palette="Set3")
# # ax=sns.boxplot(x="day",y="total_bill",data=[x1,y1],palette="Set3")
