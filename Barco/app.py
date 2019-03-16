import numpy as np
import pandas as pd
import json
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# from flask import Flask

names_of_cities=["Agra","Ahmedabad","Aizawl","Ajmer","Akola","Aligarh","Allahabad","Alwar","Amravati","Amritsar","Anantapur","Bareilly","Bathinda","Begusarai","Belgaum","Bellary","Bhagalpur","Bharatpur","Bhavnagar","Bhilwara","Bhopal","Bijapur","Bikaner","Bokaro","Bulandshahr","Chandigarh","Chandrapur","Chennai","Coimbatore","Cuttack","Darbhanga","Davanagere","Dehradun","Dewas","Dhanbad","Dhule","Durg","Erode","Etawah","Faridabad","Farrukhabad","Firozabad","Gaya","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Gwalior","Hyderabad","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jalna","Jammu","Jamnagar","Jhansi","Jodhpur","Junagadh","Kadapa","Karimnagar","Karnal","Katihar","Khammam","Kolhapur","Kolkata","Kollam","Korba","Kota","Kozhikode","Kurnool","Latur","Lucknow","Ludhiana","Madurai","Mathura","Mau","Meerut","Mirzapur","Muzaffarnagar","Muzaffarpur","Mysore","Nagpur","Nanded","Nashik","Nellore","New Delhi","Nizamabad","Pali","Panipat","Parbhani","Patiala","Patna","Pondicherry","Pune","Purnia","Raichur","Raipur","Rajkot","Rampur","Ranchi","Ratlam","Rewa","Rohtak","Sagar","Saharanpur","Salem","Sambalpur","Satara","Satna","Shahjahanpur","Sikar","Siliguri","Singrauli","Solapur","Sonipat","Srinagar","Surat","Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tumkur","Udaipur","Ujjain","Vadodara","Varanasi","Visakhapatnam","Warangal"]
df_main_data = pd.read_excel("showme.xlsx")
# df1 = df_main_data

def moveon():
    global names_of_cities
    df=pd.read_excel("showme.xlsx")
    df1=pd.read_excel("seethis.xlsx")
    hit_data={}
    # df1.head(100)
    def api1():
        df2=pd.read_excel("C:\\Users\\Debasish\\OneDrive\\ML\\barco\\showme.xlsx")
        X = df2.iloc[0:,:7].values
        y = df2.iloc[0:,7:].values
        X_train = X
        y_train = y
        x_test = X
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(x_test)
        ans=[]
        for i in y_pred:
            ans.append(float(i[0]))
        hit_data={
            "cities":names_of_cities,
            "result":list(ans),
            "prm1":True,
            "prm2":True,
            "Growth_Rate":True,
            "Literacy Rate":True,
            "Rank_City":True,
            "prm3":True,
        }
        return hit_data
    hit_data=api1()
    df1.set_index(list(dict(df1).keys()))
    values1={}
    def api2():
        s=0
        for i in names_of_cities:
                values1[i]=[str(df1[2004][s]),str(df1[2005][s]),str(df1[2006][s]),str(df1[2007][s]),str(df1[2008][s]),str(df1[2009][s]),str(df1[2010][s]),str(df1[2011][s]),str(df1[2012][s]),str(df1[2013][s]),str(df1[2014][s]),str(df1[2015][s]),str(df1[2016][s]),str(int(hit_data["result"][s]))]
                s+=1
    api2()
    hit_data["bhai"]=values1
    print(hit_data)
    return hit_data

def api22(df1, ans123):
    df1.set_index(list(dict(df1).keys()))
    values1={}
    s=0
    for i in names_of_cities:

        try:
            values1[i]=[str(df1[2004][s]),str(df1[2005][s]),str(df1[2006][s]),str(df1[2007][s]),str(df1[2008][s]),str(df1[2009][s]),str(df1[2010][s]),str(df1[2011][s]),str(df1[2012][s]),str(df1[2013][s]),str(df1[2014][s]),str(df1[2015][s]),str(df1[2016][s]),str(int(ans123["result"][s]))]
            s+=1
        except:
            pass
    return values1

# api2()
# values2={}
# values2[1]=[values1]


def moveon12():
    df3=df_main_data.copy()
    del df3["Growth Rate"]
    del df3["Y"]
    X = df3
    y = df_main_data["Y"]
    # names_of_cities=["Agra","Ahmedabad","Aizawl","Ajmer","Akola","Aligarh","Allahabad","Alwar","Amravati","Amritsar","Anantapur","Bareilly","Bathinda","Begusarai","Belgaum","Bellary","Bhagalpur","Bharatpur","Bhavnagar","Bhilwara","Bhopal","Bijapur","Bikaner","Bokaro","Bulandshahr","Chandigarh","Chandrapur","Chennai","Coimbatore","Cuttack","Darbhanga","Davanagere","Dehradun","Dewas","Dhanbad","Dhule","Durg","Erode","Etawah","Faridabad","Farrukhabad","Firozabad","Gaya","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Gwalior","Hyderabad","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jalna","Jammu","Jamnagar","Jhansi","Jodhpur","Junagadh","Kadapa","Karimnagar","Karnal","Katihar","Khammam","Kolhapur","Kolkata","Kollam","Korba","Kota","Kozhikode","Kurnool","Latur","Lucknow","Ludhiana","Madurai","Mathura","Mau","Meerut","Mirzapur","Muzaffarnagar","Muzaffarpur","Mysore","Nagpur","Nanded","Nashik","Nellore","New Delhi","Nizamabad","Pali","Panipat","Parbhani","Patiala","Patna","Pondicherry","Pune","Purnia","Raichur","Raipur","Rajkot","Rampur","Ranchi","Ratlam","Rewa","Rohtak","Sagar","Saharanpur","Salem","Sambalpur","Satara","Satna","Shahjahanpur","Sikar","Siliguri","Singrauli","Solapur","Sonipat","Srinagar","Surat","Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tumkur","Udaipur","Ujjain","Vadodara","Varanasi","Visakhapatnam","Warangal"]
    hit_data = {}
    def api12():
        X_train = X
        y_train = y
        x_test = X
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(x_test)
        ans2=[]
        for i in y_pred:
            ans2.append(i)
        return ans2

    hit_data["bhai"] = api22(df3, api12())
    print(hit_data)
    # values2[1]=[values1]
    return hit_data

def moveon13():
    global ans2
    df4=df_main_data
    df4y=df4["Y"]
    del df4["OverallLi"]
    del df4["Y"]
    ans2.clear()
    names_of_cities=["Agra","Ahmedabad","Aizawl","Ajmer","Akola","Aligarh","Allahabad","Alwar","Amravati","Amritsar","Anantapur","Bareilly","Bathinda","Begusarai","Belgaum","Bellary","Bhagalpur","Bharatpur","Bhavnagar","Bhilwara","Bhopal","Bijapur","Bikaner","Bokaro","Bulandshahr","Chandigarh","Chandrapur","Chennai","Coimbatore","Cuttack","Darbhanga","Davanagere","Dehradun","Dewas","Dhanbad","Dhule","Durg","Erode","Etawah","Faridabad","Farrukhabad","Firozabad","Gaya","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Gwalior","Hyderabad","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jalna","Jammu","Jamnagar","Jhansi","Jodhpur","Junagadh","Kadapa","Karimnagar","Karnal","Katihar","Khammam","Kolhapur","Kolkata","Kollam","Korba","Kota","Kozhikode","Kurnool","Latur","Lucknow","Ludhiana","Madurai","Mathura","Mau","Meerut","Mirzapur","Muzaffarnagar","Muzaffarpur","Mysore","Nagpur","Nanded","Nashik","Nellore","New Delhi","Nizamabad","Pali","Panipat","Parbhani","Patiala","Patna","Pondicherry","Pune","Purnia","Raichur","Raipur","Rajkot","Rampur","Ranchi","Ratlam","Rewa","Rohtak","Sagar","Saharanpur","Salem","Sambalpur","Satara","Satna","Shahjahanpur","Sikar","Siliguri","Singrauli","Solapur","Sonipat","Srinagar","Surat","Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tumkur","Udaipur","Ujjain","Vadodara","Varanasi","Visakhapatnam","Warangal"]
    hit_data={}
    df4.head(100)
    # global ans2
    def api12():
        X = df4
        y = df4y
        X_train = X
        y_train = y
        x_test = X
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(x_test)
        ans2=[]
        for i in y_pred:
            ans2.append(i)
        return ans2
    return api22(api12())

def moveon14():
    # names_of_cities=["Agra","Ahmedabad","Aizawl","Ajmer","Akola","Aligarh","Allahabad","Alwar","Amravati","Amritsar","Anantapur","Bareilly","Bathinda","Begusarai","Belgaum","Bellary","Bhagalpur","Bharatpur","Bhavnagar","Bhilwara","Bhopal","Bijapur","Bikaner","Bokaro","Bulandshahr","Chandigarh","Chandrapur","Chennai","Coimbatore","Cuttack","Darbhanga","Davanagere","Dehradun","Dewas","Dhanbad","Dhule","Durg","Erode","Etawah","Faridabad","Farrukhabad","Firozabad","Gaya","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Gwalior","Hyderabad","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jalna","Jammu","Jamnagar","Jhansi","Jodhpur","Junagadh","Kadapa","Karimnagar","Karnal","Katihar","Khammam","Kolhapur","Kolkata","Kollam","Korba","Kota","Kozhikode","Kurnool","Latur","Lucknow","Ludhiana","Madurai","Mathura","Mau","Meerut","Mirzapur","Muzaffarnagar","Muzaffarpur","Mysore","Nagpur","Nanded","Nashik","Nellore","New Delhi","Nizamabad","Pali","Panipat","Parbhani","Patiala","Patna","Pondicherry","Pune","Purnia","Raichur","Raipur","Rajkot","Rampur","Ranchi","Ratlam","Rewa","Rohtak","Sagar","Saharanpur","Salem","Sambalpur","Satara","Satna","Shahjahanpur","Sikar","Siliguri","Singrauli","Solapur","Sonipat","Srinagar","Surat","Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tumkur","Udaipur","Ujjain","Vadodara","Varanasi","Visakhapatnam","Warangal"]
    hit_data={}
    df4 = df_main_data.copy()
    df4y = df4["Y"]
    df4.head(100)
    global ans2
    ans2.clear()
    def api12():
        X = df4
        y = df4y
        X_train = X
        y_train = y
        x_test = X
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(x_test)
        ans2=[]
        for i in y_pred:
            ans2.append(i)
    api12()
    return ans2

ans7=[]
def moveon15():
    # names_of_cities=["Agra","Ahmedabad","Aizawl","Ajmer","Akola","Aligarh","Allahabad","Alwar","Amravati","Amritsar","Anantapur","Bareilly","Bathinda","Begusarai","Belgaum","Bellary","Bhagalpur","Bharatpur","Bhavnagar","Bhilwara","Bhopal","Bijapur","Bikaner","Bokaro","Bulandshahr","Chandigarh","Chandrapur","Chennai","Coimbatore","Cuttack","Darbhanga","Davanagere","Dehradun","Dewas","Dhanbad","Dhule","Durg","Erode","Etawah","Faridabad","Farrukhabad","Firozabad","Gaya","Ghaziabad","Gorakhpur","Gulbarga","Guntur","Gurgaon","Gwalior","Hyderabad","Indore","Jabalpur","Jaipur","Jalandhar","Jalgaon","Jalna","Jammu","Jamnagar","Jhansi","Jodhpur","Junagadh","Kadapa","Karimnagar","Karnal","Katihar","Khammam","Kolhapur","Kolkata","Kollam","Korba","Kota","Kozhikode","Kurnool","Latur","Lucknow","Ludhiana","Madurai","Mathura","Mau","Meerut","Mirzapur","Muzaffarnagar","Muzaffarpur","Mysore","Nagpur","Nanded","Nashik","Nellore","New Delhi","Nizamabad","Pali","Panipat","Parbhani","Patiala","Patna","Pondicherry","Pune","Purnia","Raichur","Raipur","Rajkot","Rampur","Ranchi","Ratlam","Rewa","Rohtak","Sagar","Saharanpur","Salem","Sambalpur","Satara","Satna","Shahjahanpur","Sikar","Siliguri","Singrauli","Solapur","Sonipat","Srinagar","Surat","Thane","Thanjavur","Thiruvananthapuram","Thrissur","Tiruchirappalli","Tirunelveli","Tumkur","Udaipur","Ujjain","Vadodara","Varanasi","Visakhapatnam","Warangal"]
    df5 = df_main_data
    df5y = df5["Y"]
    hit_data={}
    df5.head(100)
    global ans7
    def api12():
        global ans7
        X = df5
        y = df5y
        X_train = X
        y_train = y
        x_test = X
        lr = LinearRegression()
        lr.fit(X_train,y_train)
        y_pred = lr.predict(x_test)
        ans7=[]
        for i in y_pred:
            ans7.append(i)
    return ans7
    return api22(api12())
# moveon12()
    