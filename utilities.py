from cProfile import label
from datetime import date, datetime
from turtle import color
from matplotlib.ft2font import BOLD
import mysql.connector as mysql
from matplotlib import patches, pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show(username, date1, date2, choice):
    date1 = dateFormat(date1)
    date2 = dateFormat(date2)
    dateList = [date1, date2]
    eSheetData = analysisData(username, "e", dateList)
    ePlotData = getRefinedData(eSheetData)
    iSheetData = analysisData(username, "i", dateList)
    iPlotData = getRefinedData(iSheetData)
    if(choice == "e"):
        eLabellist = []
        eAmountlist = []
        for i in ePlotData:
            eLabellist.append(i)
            eAmountlist.append(ePlotData[i])

        bars = plt.bar(eLabellist, eAmountlist, color = "#7D9EF9")
        plt.bar_label(bars, labels=eAmountlist, color = "red", fontsize = 12)
        plt.title("Category wise expense from {} to {}".format(date1, date2), fontsize = 25, color = "#5DADE2")
        plt.ylabel("Amount in Rupees", color = "Red", fontsize = 20)
        plt.xlabel("Categories", color = "green", fontsize = 20)
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()
        
    elif(choice == "t"):
        iSum = 0
        exSum = 0
        for item in iPlotData.keys():
            iSum+=iPlotData[item]
        for item in ePlotData.keys():
            exSum+=ePlotData[item]
        savings = iSum - exSum
        list = [exSum, savings]
        label = "Expense", "Savings"
        label1 = ["Total Expense: {} Rs.".format(exSum), "Total Savings: {} Rs.".format(savings)]
        explode = (0, 0.1)
        plt.pie(list, labels= label, explode=explode, shadow=True,autopct='%1.1f%%', radius=0.8, textprops={'fontsize': 14})
        plt.title("Expense Analysis from {} to {}".format(date1, date2), fontsize = 25, color = "#5DADE2")
        plt.legend(label1, title ="Total Income: {} Rs.".format(iSum),  loc = "lower right")
        mng = plt.get_current_fig_manager()
        mng.window.state('zoomed')
        plt.show()

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
            cursor.execute("select* from expenses where username = '"+username+"' order by date DESC limit 15")
            edata = cursor.fetchall()
            cursor.execute("commit")
            for i in edata:
                i = list(i)
                i[0] = str(i[0])
                i[3] = int(i[3])
                new_list.append(i[0:len(i)-1])
        elif(ie == 'i'):
            cursor.execute("select* from incomes where username = '"+username+"' order by date DESC limit 10")
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

#Converts raw data fetched from database to useable dictionary form.
def getRefinedData(ls):
    newEdata = dict()
    for i in ls:
        i = list(i)
        i[3] = int(i[3])
        key = i[1]
        val = i[3]
        if key in newEdata:
            sum = newEdata[key]
            sum+= val
            newEdata[key] = sum
        else:
            newEdata[key] = val
    return newEdata
