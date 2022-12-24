from fastapi import FastAPI
from demo import findstring
from category import cat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from firebase import solve
from firebase import create_collection
from prediction import arima_prediction
import pandas as pd
db=firestore.client()
app = FastAPI()

li = ["Dear SBI User, your A/c X4954-debited by Rs50.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs55.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs60.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs65.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs650.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs1000.0 on 19Nov22 transfer to easemytrip Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs6550.0 on 19Nov22 transfer to zomato Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"]

@app.get('/signup')
async def status():
    db.collection("Email").document("Message List").collection("List").document('List').set({'list':li})
    findstring(li)
    x=cat("Email")
    return x

@app.get('/login')
async def login():
    old=db.collection("Email").document("Message List").collection("List").get()
    new_list=(list(set(li) - set(old)))
    db.collection("Email").document("Message List").collection("List").document('List').set({'list':li})
    findstring(new_list)
    x=cat("Email")
    return x

@app.get('/predict')
async def predict():
    # trans=db.collection("Email").document("Transactions").collection("Transaction").get()
    # date=[]
    # amount=[]
    # for price in trans:
    #     d=list(price.to_dict().values())
    #     date.append(d[1])
    #     amount.append(d[2])
    # x=arima_prediction(date,amount)
    # df=pd.read_csv('Electric_Production.csv')
    return arima_prediction()
    # return x