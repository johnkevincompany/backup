import gspread
from oauth2client.service_account import ServiceAccountCredentials

Name = ["John","Kevin","Oliveira","Edio","Cimeia","Jackob"]
Email = ["John@bol.com","Kevin@bol.com","Oliveira@bol.com","Edio@bol.com","Cimeia@bol.com","Jackob@bol.com"]

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("InstaSheet")
worksheet = spreadsheet.add_worksheet("Subscribers",len(Name),2)

for i in range(1, len(Name)+1):
    worksheet.update_cell(i, 1, Name[i-1])
    worksheet.update_cell(i, 2, Email[i-1])



