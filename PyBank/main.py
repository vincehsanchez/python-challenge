import os 
import csv

csv_path = os.path.join("/Users/vincehsanchez/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv")
txt_path = os.path.join("/Users/vincehsanchez/Documents/GitHub/python-challenge/PyBank/analysis/budget_analysis.txt")
net_total = 0

with open(csv_path) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csv_reader)
    profitLoss_file = csv.reader(csvfile)
    profitLoss_list = [] 
    change_list = []
    date_list = []
    # Reads each row
    for row in csv_reader:
        profitLoss_row = int(row[1])
        date_row = row[0]
        net_total += profitLoss_row
        total_months = (csv_reader.line_num-1) #https://docs.python.org/3/library/csv.html?highlight=line_num#csv.csvreader.line_num
    #need to find and create list of profitLoss differences for average change
        profitLoss_list.append(int(row[1])) #needed to have as integer, not string
        date_list.append(row[0])
    for c in range(len(profitLoss_list)-1):
        change_list.append(profitLoss_list[c+1]-profitLoss_list[c]) #when finding difference in change we lose a value or one less than first list
        avgChange = round((sum(change_list))/(total_months-1), 2)
        greatest_increase = max(change_list)
        greatest_decrease = min(change_list)
        #need to find date and month of min, we have month number, but add 1 since we lost a value
        max_month_num = change_list.index(max(change_list))+1
        min_month_num = change_list.index(min(change_list))+1
    #use month number to find date value in date_row
        max_date = date_list[max_month_num]
        min_date = date_list[min_month_num]
#Pretty formatting
print(f"\nFinancial Analysis")
print(f"\n------------------------------")
print(f"\nTotal Months: {total_months}")
print(f"\nTotal: ${net_total}")
print(f"\nAverage Change: ${avgChange}")
print(f"\nGreatest Increase in Profits: {max_date} $({greatest_increase})") #needs date 
print(f"\nGreatest Decrease in Profits: {min_date} $({greatest_decrease})") #needs date
 
#output file
with open (txt_path, 'w') as txtFile:
    txtWriter = csv.writer(txtFile)
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Financial Analysis"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"------------------------------"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Total Months: {total_months}"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Total: ${net_total}"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Average Change: ${avgChange}"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Greatest Increase in Profits: {max_date} $({greatest_increase})"])
    txtWriter.writerow([f" "])
    txtWriter.writerow([f"Greatest Decrease in Profits: {min_date} $({greatest_decrease})" ])

#bcs assisatnt pointed out it was including a lost value to calculate average.
#bcs assistant clarified text file output formatting