from datetime import date, datetime

def dateFormat(date):
    new_date = date[:4] + "20" + date[4:]
    new_date = datetime.strptime(new_date, "%d/%m/%Y")
    new_date = datetime.date(new_date)
    new_date = str(new_date)
    return new_date