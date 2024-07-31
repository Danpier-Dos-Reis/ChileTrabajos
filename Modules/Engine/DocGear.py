import locale
from datetime import datetime
from bs4 import BeautifulSoup

from ..Models.JobItem import JobItem

# Configurar el locale a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')  # Esto puede variar según tu sistema operativo

def list_jobs(srt_html):
    """
    return List[JobItem]
    """    
    jobs_with_links = add_links(srt_html)
    jobs_with_dates = add_date(jobs_with_links, srt_html)
    for i in range(len(jobs_with_links)):
        jobs_with_links[i].calendar_date = jobs_with_dates[i].calendar_date
    return jobs_with_links

def add_links(srt_html):
    soup = BeautifulSoup(srt_html, 'html.parser')
    job_items = soup.select('div.job-item')
    job_list = []
    for job_item in job_items:
        link = job_item.select_one('a')['href']
        job_list.append(JobItem(link))
    return job_list

def add_date(job_list, srt_html):
    soup = BeautifulSoup(srt_html, 'html.parser')
    job_items = soup.select('div.job-item h3:nth-of-type(2)')
    dates = []
    for job_item in job_items:
        text = job_item.select_one('a').text
        dates.append(text.strip().replace('  ', ' '))
    for i in range(len(job_list)):
        job_list[i].calendar_date = datetime.strptime(dates[i], "%d de %B de %Y")
    return job_list
