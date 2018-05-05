# p_49_data_mining.py
# Brendan Knapp
# 2018-04-30
# 
'''
Write a python program to calculate the average for each month of every year.
'''
def average(nums):
  sum = 0
  for num in nums:
    sum += float(num)
  len = 0
  for num in nums:
    len += 1
  average = sum / len
  return(average)

def get_data_list(path):
  data = open(path, "r").read().split("\n")
  pseudo_data_frame = []
  
  for line in data:
    # pseudo_data_frame.append([line.split(",")[0], line.split(",")[-1]])
    pseudo_data_frame.append(tuple(line.split(",")))
  
  data_list = []
  for observation in pseudo_data_frame[1:-1]: #[1:-1]: # skip column headers last, empty row
    date = observation[0]
    year = date.split("-")[0]
    month = date.split("-")[1]
    value = observation[-1]
    data_list.append(["-".join([year, month]), value])

  return(data_list)

  
def get_monthly_averages(data_list):
  dates = []
  for observation in data_list:
    if observation[0] not in dates:
      dates.append(observation[0])

  # data_dict = {}
  # avg_data = list()
  avg_data  =  [["Month", "Year", "Average"]]
  for date in dates:
    year_month = date
    monthly_values = []
    for observation in data_list:
      if observation[0] == year_month:
        monthly_values.append(observation[1])
    # print(year_month)
    year = date.split("-")[0]
    month = date.split("-")[1]
    # print(year_month)
    row = [month, year, "{0:.2f}".format(average(monthly_values))]
    # year_month = year_month.split("-")
    avg_data.append(row)
    
    # data_list = []
    # for k, v in data_dict.items():
      # data_list.append([k, v])
    
  # for 
  
  # avg_list = list(map(lambda x: sum(data_dict[x]), data_dict))

  return(avg_data)

count = 0
for row in get_monthly_averages(get_data_list("table-1.csv")):
  print("monthly_average_list[{}] = ".format(count), row)
  count += 1
  
# get_monthly_averages(get_data_list("table-1.csv"))
