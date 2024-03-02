import pandas as pd

# CSV FORMAT
#   Time  Key  Action
#  13389  s    p
#  13397  s    r
data = pd.read_csv("records/someRecord.csv")

index = 0
numOfRecords = 0
for record in data.Key:
    numOfRecords += 1

# pre-statistics CSV format
# Key  TimeHeld
header = ['Key', 'TimeHeld']
pre_statistics_record = []

for record in data.Key:
    if(data.Action[index] == 'p'):
        key = data.Key[index]
        print(f"pressed {key}")
        press_time = data.Time[index]
        i = 1
        while data.Key[index + i] != key:
            i += 1
        release_time = data.Time[index + i]
        hold_time = release_time - press_time
        pre_statistics_record.append([key, hold_time])
        print(f"{key} has been held for {hold_time}")
    index += 1

framedRecord = pd.DataFrame(pre_statistics_record, columns=header)
framedRecord.to_csv(f'metadata/pre_statistics.csv', index=False)

pre_statistics_data = pd.read_csv("metadata/pre_statistics.csv")
key_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'y', 'z']


preStatisticsLength = 0
for record in pre_statistics_data.Key:
    preStatisticsLength += 1


# statistics CSV format
# Key  AveragePressTime
statistics_header = ['Key', 'AverageHoldTime']
statistics_record = []

for key in key_names:
    total_count = 0
    total_time = 0
    average_time = 0
    for num in range(preStatisticsLength):
        if pre_statistics_data.Key[num][1] == key:
            total_count += 1 
            total_time += pre_statistics_data.TimeHeld[num]
    if total_count > 0:
        average_time = total_time/total_count
        print(f"Key {key} was pressed {total_count}x for {total_time}, the average time was {average_time}")
        statistics_record.append([key, average_time])
        

framedRecord = pd.DataFrame(statistics_record, columns=statistics_header)
framedRecord.to_csv(f'statistics/statistics.csv', index=False)
