from datetime import date, datetime
import mysql.connector as mysql
import time
from plyer import notification


def send_notification():
    notification.notify(
    title = "It's time to update your expenses!!!",
    timeout = 20
    )


def dateFormat(date):
    cnt = 0
    j = 0
    for i in date:
        j+=1
        if i=='/':
            cnt+=1
            if cnt==2:
                new_date = date[:j] + "20" + date[j:]
    new_date = datetime.strptime(new_date, "%m/%d/%Y")
    new_date = datetime.date(new_date)
    new_date = str(new_date)
    return new_date


def extractData(username, ie):
        new_list = []
        con = mysql.connect(host='localhost', user='root',
                                        password='Mahendra@$28', database='expensetracker')
        cursor = con.cursor()
        if(ie == 'e'):
            cursor.execute("select* from expenses where username = '"+username+"' order by date DESC limit 7")
            edata = cursor.fetchall()
            cursor.execute("commit")
            for i in edata:
                i = list(i)
                i[0] = str(i[0])
                i[3] = int(i[3])
                new_list.append(i[0:len(i)-1])
        elif(ie == 'i'):
            cursor.execute("select* from incomes where username = '"+username+"' order by date DESC limit 5")
            idata = cursor.fetchall()
            cursor.execute("commit")
            for i in idata:
                i = list(i)
                i[0] = str(i[0])
                i[3] = int(i[3])
                new_list.append(i[0:len(i)-1])
        con.close()
        return new_list

def analysisData(username, ie, dates):
        new_list = []
        con = mysql.connect(host='localhost', user='root',
                                        password='Mahendra@$28', database='expensetracker')
        cursor = con.cursor()
        if(ie == 'e'):
            cursor.execute("select* from expenses where username = '"+username+"' and date BETWEEN '"+dates[0]+"' and '"+dates[1]+"' order by date ASC")
            edata = cursor.fetchall()
            cursor.execute("commit")
            for i in edata:
                i = list(i)
                i[0] = str(i[0])
                i[3] = int(i[3])
                new_list.append(i[0:len(i)-1])
        elif(ie == 'i'):
            cursor.execute("select* from incomes where username = '"+username+"' and date BETWEEN '"+dates[0]+"' and '"+dates[1]+"' order by date ASC")
            idata = cursor.fetchall()
            cursor.execute("commit")
            for i in idata:
                i = list(i)
                i[0] = str(i[0])
                i[3] = int(i[3])
                new_list.append(i[0:len(i)-1])
        con.close()
        return new_list
