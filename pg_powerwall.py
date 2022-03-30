#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pypowerwall, json, smtplib
import requests

# Optional: Turn on Debug Mode
# pypowerwall.set_debug(True)

# Credentials for your Powerwall - Customer Login Data
password='XXXXXXXXXX'                 # Powerwall Password - Found inside the powerwall gateway
email='xxxxxxxxx@xxxxx.xxx'           # Login email
host = "NNN.NNN.NNN.NNN"              # IP Address of your Powerwall Gateway
timezone = "America/Los_Angeles"      # Your local timezone

# Little Snitch URL
url = "https://nosnch.in/xxxxxxxxxx"

# SMTP
password = "xxxxxxxxxx"               # SMTP email password
username = "xxxxx@xxx.xx"             # SMTP email username
smtphost = "xxxx.xxx.xxx"             # SMTP hostname
msg['From'] = "xxxxx@xxx.xxx"         # FROM email address
recipients = ['xxxxx@xxx.xxx']        # TO email address

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

x = json.loads(pw.poll('/api/system_status/grid_status'))
y = x["grid_status"]

if(y == "SystemGridConnected"):
  print("grid connected")
  data = requests.get(url).json
if(y == "SystemIslandedActive"):
  print("grid not connected")
  msg = MIMEMultipart()
  message = "Grid Is Down"
  msg['To'] = ", ".join(recipients)
  msg['Subject'] = "Grid Is Down #gridisdown"
  msg.attach(MIMEText(message, 'plain'))
  server = smtplib.SMTP(smtphost)
  server.login(username, password)
  server.sendmail(msg['From'], recipients, msg.as_string())
  server.quit()
