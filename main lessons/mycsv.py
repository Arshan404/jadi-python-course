import csv

# مسیر فایل با r"" تا از مشکل \ جلوگیری شود
file_path = r"D:\py projects\jadi python course\research-and-development-survey-2024-csv-notes.csv"

with open(file_path, encoding="utf-8") as my_file:
    csv_data = csv.DictReader(my_file)  # خواندن به صورت دیکشنری
    lines = list(csv_data)              # تبدیل به لیست از دیکشنری‌ها
    print(lines)                        # چاپ محتوا

    #csv_data = csv.reader(my_file)
    """
    # چاپ همه ردیف‌ها
    for row in csv_data:
        print(row)
    """

outfile = open('mycsv.csv' , mode="w" , newline= '')
csv_writer = csv.writer(outfile , delimiter= "|" )
csv_writer.writerow([1,2,3])
csv_writer.writerow(['jadi' , 'madi' , 'paadi'])
outfile.close()

with open('mycsv.csv', mode="r", newline='') as infile:
    csv_reader = csv.reader(infile, delimiter="|")
    for row in csv_reader:
        print(row)