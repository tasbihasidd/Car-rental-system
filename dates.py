from datetime import datetime

date_string = "2024-04-30"
date_object = datetime.strptime(date_string, "%Y-%m-%d")
print(date_object)