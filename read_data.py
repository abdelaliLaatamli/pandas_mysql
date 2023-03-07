
from sqlalchemy import create_engine
# import pymysql
import pandas as pd

 

sqlEngine       =  create_engine('mysql+pymysql://vagrantDb:Password123#9!@192.168.33.10:3306/test', pool_recycle=3600)

dbConnection    = sqlEngine.connect()

frame           = pd.read_sql("select * from test.UserVitals", dbConnection);

 

pd.set_option('display.expand_frame_repr', False)

print(frame)

 

dbConnection.close()