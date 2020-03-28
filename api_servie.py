import json
import time
import datetime
import sys
import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np

class api_servie:
    def data_json(self,res):
        llist=[]
        out_dict={"Date of Arrival":1,"Port of Origin ":1,"Street":1,"Tehsil":1}
        for row in res:
            out_dict={"Date of Arrival":1,"Port of Origin ":1,"Street":1,"Tehsil":1}
            ad,origin,street,taluk = row
            out_dict["Date of Arrival"]=ad
            out_dict["Port of Origin"]=origin
            out_dict["Street"]=street
            out_dict["Tehsil"]=taluk
            llist.append(out_dict)
        headers=["Date of Arrival","Port of Origin","Street","Tehsil"]
        return {'data':llist,'headers':headers}

            
    def get_data(self,pin):
        engine=create_engine('sqlite:///'+'Data.db')
        df = pd.read_csv(r'Hassan.csv')
        df.to_sql('base',con=engine, if_exists='replace')
        # print(df)
        # pin='573201'
        res=engine.execute("select [Date of Arrival],[Port of Origin of journey],[Street/ Village],[Tehsil] from base where [PIN]=?;",pin)
        # for i in res:
        #     print(i)
        return self.data_json(res)
    
    def get_pins(self):
        out_dict={}
        engine=create_engine('sqlite:///'+'Data.db')
        res=engine.execute("select distinct[PIN] from base;")
        pin_list=[]
        for i in res:
            pin_list.append(i[0])
        out_dict['data']=pin_list
        pin_list=[]
        pin_list.append(out_dict)
        return pin_list

    def plotter(self):
        engine=create_engine('sqlite:///'+'Data.db')
        res=engine.execute("select [PIN],count([PIN]) from base group by [PIN];")
        pins=[]
        pincount=[]
        for i in res:
            pins.append(i[0])
            pincount.append(i[1])
        # fig1, ax1 = plt.subplots()
        # ax1.pie(pins, explode=pincount, 
        # shadow=True, startangle=90)
        # ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # plt.show()
        index = np.arange(len(pins))
        plt.bar(index, pincount)
        plt.xlabel('PIN', fontsize=9)
        plt.ylabel('Quarantined number', fontsize=9)
        plt.xticks(index, pins, fontsize=8, rotation=30)
        plt.title('Quarantine List Hassan')
        plt.show()


if __name__ == "__main__":
    obj = api_servie()
    obj.plotter()