import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"

temp = "./hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com","mail.google.com","www.linkedin.com","linkedin.com"]

now = dt.now()

while True:
    if dt(now.year, now.month, now.day, 8) < now < dt(now.year,
    now.month, now.day, 18):
        print("It's working time!")
        with open(host_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website +"\n")
    else:
        with open(host_path, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            for line in lines:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("All done! Go out and play!")
    time.sleep(5)
