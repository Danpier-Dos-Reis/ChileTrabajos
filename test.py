from datetime import datetime

from Modules.Engine import DAL

if __name__ == "__main__":
    #Insert
    DAL.addRecord(datetime.now(),"holaholachabacano.peru")

    #show records
    records = DAL.getRecords()
    for r in records:
        print(r)

    #delete record