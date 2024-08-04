import time, os
from playsound3 import playsound

from Modules.Engine import Caller, DocGear
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

myDir = os.path.dirname(fileTXT)

# Crea los directorios si no existen
if not os.path.exists(myDir): os.makedirs(myDir)

n = len(links)
i = 0
while i <= n:
    link = links[i]
    doc = Caller.get_dom(link)
    jobList = DocGear.list_jobs(doc)
    for job in jobList:
        #Test
        #print(f"JobDate=>{jobList[0].calendar_date.date()}\nCurrentDate=>{currentDate.date()}")
        if (job.calendar_date.date() == currentDate.date()):
            #"a" añade texto
            with open(fileTXT, "a") as txt: txt.write(f"Job \n\tlink => {job.url_link}\n\tFecha => {job.calendar_date}\n\n")
            playsound(_sound)
    i = i+1
    if(i == n):
        i = 0
        time.sleep(8*60)#8min