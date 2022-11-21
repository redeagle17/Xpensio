from fastapi import FastAPI
from demo import findstring
# from category import cat
# from firebase import solve
from firebase import create_collection
app = FastAPI()

li = ["Dear SBI User, your A/c X4954-debited by Rs50.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs55.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs60.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI",
"Dear SBI User, your A/c X4954-debited by Rs65.0 on 19Nov22 transfer to Dunzo Digital Ref No 232316221258. If not done by u, fwd this SMS to 9223008333/Call 1800111109 or 09449112211 to block UPI -SBI"]

@app.get('/status')
async def status():
    findstring(li)

# @app.get('/status/category')
# async def statuscategory():
#     x = cat()
#     return x

# @app.get('/firebase')
# async def solutionfetch():
#     create_collection(x)
    # return x