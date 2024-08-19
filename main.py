import time, os
from playsound3 import playsound

from Modules.Engine import Caller, DocGear, DAL
from Modules.Models import JobItem
from datetime import datetime

currentDate = datetime.now()
links = ["https://www.chiletrabajos.cl/encuentra-un-empleo?action=search&order_by=&ord=&within=25&2=desarrollador+web&filterSearch=Buscar",#desarrollador web
         "https://www.chiletrabajos.cl/encuentra-un-empleo?2=analista+programador&13=&fecha=&categoria=&8=&14=&inclusion=&f=2",#analista programador
         "https://www.chiletrabajos.cl/encuentra-un-empleo?2=desarrollador+full+stack&13=&fecha=&categoria=&8=&14=&inclusion=&f=2", #desarrollador full stack
         "https://www.chiletrabajos.cl/encuentra-un-empleo?2=desarrollador+front+end&13=&fecha=&categoria=&8=&14=&inclusion=&f=2#google_vignette"#desarrollador front end
         ]

_sound = "./Assets/sound.wav"
fileTXT = "./CurrentJobs.txt"
jobRecords = DAL.getRecords()

myDir = os.path.dirname(fileTXT)

# Crea los directorios si no existen
if not os.path.exists(myDir): os.makedirs(myDir)

#Borrar registros antiguos
if __name__ == "__main__" and len(jobRecords) > 0:
    DAL.deleteRecord(currentDate.date())
    

n = len(links)
i = 0
while i <= n:
    link = links[i]
    doc = Caller.get_dom(link)
    jobList = DocGear.list_jobs(doc)
    
    #Añadir nuevos registros
    for job in jobList:
        if (job.calendar_date.date() == currentDate.date()):
            if str(job.url_link) == "https://www.chiletrabajos.cl/trabajo/analista-programador-en-practica-3441342":
                pico = "lkhsdfskdfns"
        if len(jobRecords) > 0:
            #Validamos que no exista ese link en los records
            if not any(l[2] == str(job.url_link) for l in jobRecords):
                #Añadir a la db
                if (job.calendar_date.date() == currentDate.date()):
                    DAL.addRecord(job.calendar_date,job.url_link)
                    playsound(_sound)
                    jobRecords = DAL.getRecords()
        else:
            #Si no hay registros entonces solo debemos validar la fecha
            if (job.calendar_date.date() == currentDate.date()):
                DAL.addRecord(job.calendar_date,job.url_link)
                playsound(_sound)
                jobRecords = DAL.getRecords()

    i = i+1
    if(i == n):
        i = 0
        print(f"{datetime.now()} - server sleeping...")
        time.sleep(8*60)#8min
