import time, os
from playsound3 import playsound

from Modules.Engine import Caller, DocGear
from Modules.Models import JobItem
from datetime import datetime

currentDate = datetime.now()
links = ["https://www.chiletrabajos.cl/encuentra-un-empleo?2=programador+c%23&13=&fecha=&categoria=&8=&14=&inclusion=&f=2"]

n = len(links)
i = n
_sound = "./Assets/sound.wav"
fileTXT = "./CurrentJobs.txt"

myDir = os.path.dirname(fileTXT)

# Crea los directorios si no existen
if not os.path.exists(myDir): os.makedirs(myDir)

while i > 0:
    for link in links:
        doc = Caller.get_dom(link)
        jobList = DocGear.list_jobs(doc)
        for job in jobList:
            if (job.calendar_date == currentDate):
                #"a" añade texto
                with open(fileTXT, "a") as txt: txt.write(f"Job \n\tlink => {job.url_link}\n\tFecha => {job.calendar_date}\n\n")
                playsound(_sound)
    i = i-1
    if(i == 0):
        i = n
        time.sleep(8*60)#8min