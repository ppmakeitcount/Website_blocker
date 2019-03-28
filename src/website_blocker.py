from datetime import datetime as dt
import time
host_path = "/etc/hosts"
websites = ["www.facebook.com", "facebook.com"]
redirect = "127.0.0.1"
while True:
  if 9 < dt.now().hour < 16:
    print("working hours")
    with open(host_path, "r+") as file:
      content = file.read()
      # print(content)
      for website in websites:
        if website in content:
          pass
        else:
          file.write(f"{redirect} {website} \n")
  else:
    print("Fun hours")
    with open(host_path, "r+") as file:
      content = file.readlines()
      # print(content)
      file.seek(0)
      for line in content:
        if not any(website in line for website in websites):
          file.write(line)
      file.truncate()
      
  time.sleep(5)