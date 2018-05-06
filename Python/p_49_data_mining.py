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
    pseudo_data_frame.append(tuple(line.split(",")))
  
  data_list = []
  for observation in pseudo_data_frame[1:-1]: #[1:-1]: # skip head/foot: empty rows
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
      
  avg_data  =  [["Month", "Year", "Average"]]
  for date in dates:
    year_month = date
    monthly_values = []
    for observation in data_list:
      if observation[0] == year_month:
        monthly_values.append(observation[1])
        
    year = date.split("-")[0]
    month = date.split("-")[1]
    
    row = [month, year, "{:.2f}".format(average(monthly_values))]
    avg_data.append(row)

  return(avg_data)

def print_info(average_list):
  count = 0
  for row in average_list:
    print("monthly_average_list[{:2}] =".format(count), row)
    count += 1

print_info(get_monthly_averages(get_data_list("table-1.csv")))

'''
monthly_average_list[ 0] = ['Month', 'Year', 'Average']
monthly_average_list[ 1] = ['09', '2008', '437.70']
monthly_average_list[ 2] = ['08', '2008', '485.91']
monthly_average_list[ 3] = ['07', '2008', '510.03']
monthly_average_list[ 4] = ['06', '2008', '556.32']
monthly_average_list[ 5] = ['05', '2008', '575.92']
monthly_average_list[ 6] = ['04', '2008', '497.58']
monthly_average_list[ 7] = ['03', '2008', '440.33']
monthly_average_list[ 8] = ['02', '2008', '503.80']
monthly_average_list[ 9] = ['01', '2008', '611.81']
monthly_average_list[10] = ['12', '2007', '695.40']
monthly_average_list[11] = ['11', '2007', '676.37']
monthly_average_list[12] = ['10', '2007', '635.39']
monthly_average_list[13] = ['09', '2007', '540.43']
monthly_average_list[14] = ['08', '2007', '509.83']
monthly_average_list[15] = ['07', '2007', '532.48']
monthly_average_list[16] = ['06', '2007', '515.02']
monthly_average_list[17] = ['05', '2007', '473.01']
monthly_average_list[18] = ['04', '2007', '472.50']
monthly_average_list[19] = ['03', '2007', '452.91']
monthly_average_list[20] = ['02', '2007', '467.22']
monthly_average_list[21] = ['01', '2007', '490.58']
monthly_average_list[22] = ['12', '2006', '473.50']
monthly_average_list[23] = ['11', '2006', '485.63']
monthly_average_list[24] = ['10', '2006', '440.53']
monthly_average_list[25] = ['09', '2006', '397.06']
monthly_average_list[26] = ['08', '2006', '377.09']
monthly_average_list[27] = ['07', '2006', '403.53']
monthly_average_list[28] = ['06', '2006', '393.59']
monthly_average_list[29] = ['05', '2006', '383.80']
monthly_average_list[30] = ['04', '2006', '413.78']
monthly_average_list[31] = ['03', '2006', '358.87']
monthly_average_list[32] = ['02', '2006', '370.00']
monthly_average_list[33] = ['01', '2006', '445.71']
monthly_average_list[34] = ['12', '2005', '418.95']
monthly_average_list[35] = ['11', '2005', '399.14']
monthly_average_list[36] = ['10', '2005', '322.47']
monthly_average_list[37] = ['09', '2005', '304.24']
monthly_average_list[38] = ['08', '2005', '286.92']
monthly_average_list[39] = ['07', '2005', '298.21']
monthly_average_list[40] = ['06', '2005', '287.55']
monthly_average_list[41] = ['05', '2005', '239.71']
monthly_average_list[42] = ['04', '2005', '199.21']
monthly_average_list[43] = ['03', '2005', '181.16']
monthly_average_list[44] = ['02', '2005', '195.01']
monthly_average_list[45] = ['01', '2005', '192.85']
monthly_average_list[46] = ['12', '2004', '181.77']
monthly_average_list[47] = ['11', '2004', '177.50']
monthly_average_list[48] = ['10', '2004', '153.23']
monthly_average_list[49] = ['09', '2004', '113.23']
monthly_average_list[50] = ['08', '2004', '105.26']
'''
