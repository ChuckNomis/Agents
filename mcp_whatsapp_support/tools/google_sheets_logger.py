import gspread

# Google Sheets call-back logger
client = gspread.service_account()
sheet = client.open("Acme Support Logs").sheet1


def log_to_google_sheets(data):
    sheet.append_row([data])
