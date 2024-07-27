using HtmlAgilityPack;
using ChileTrabajos.Models;
using System.Globalization;

namespace ChileTrabajos.Engine
{
    public class DocGear
    {
        public List<JobItem> ListJobs(string srtHtml)
        {
            List<JobItem> jobsWithLinks = AddLinks(srtHtml);
            List<JobItem> jobsWithDates = AddDate(jobsWithLinks,srtHtml);

            for (int i = 0; i < jobsWithLinks.Count; i++)
            {
                jobsWithLinks[i].CalendarDate = jobsWithDates[i].CalendarDate;
            }

            return jobsWithLinks;
        }

        public List<JobItem> AddLinks(string srtHtml)
        {
            HtmlDocument doc = new HtmlDocument();;
            doc.LoadHtml(srtHtml);
            HtmlNodeCollection jobItems = doc.DocumentNode.SelectNodes("//div[contains(@class, 'job-item')]");
            List<JobItem> jobList = new List<JobItem>();

            foreach (var jobItem in jobItems)
            {
                string link = jobItem.SelectSingleNode(".//a").GetAttributeValue("href", string.Empty);
                jobList.Add(new JobItem { UrlLink = link });
            }

            return jobList;
        }

        public List<JobItem> AddDate(List<JobItem> jobList, string srtHtml)
        {
            HtmlDocument doc = new HtmlDocument();
            doc.LoadHtml(srtHtml);
            HtmlNodeCollection jobItems = doc.DocumentNode.SelectNodes("//div[contains(@class, 'job-item')]//h3[2]");
            List<string> dates = new List<string>();

            foreach (var jobItem in jobItems)
            {
                string text = jobItem.SelectSingleNode(".//a").InnerText;
                dates.Add(text.Trim().Replace("  "," "));
            }
            
            for(int i = 0; i < jobList.Count ;i++){
                jobList[i].CalendarDate = DateTime.ParseExact(dates[i],"d 'de' MMMM 'de' yyyy",new CultureInfo("es-ES"));;    
            }
            return jobList;
        }
    }
}