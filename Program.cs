using ChileTrabajos.Engine;
using ChileTrabajos.Models;
using ChileTrabajos.Tests;

namespace ChileTrabajos
{
    class Program
    {
        static void Main(string[] args)
        {
            //Intances
            Caller caller = new Caller();
            DocGear docGear = new DocGear();

            DateTime current = DateTime.Now;
            string[] links = {
                "https://www.chiletrabajos.cl/encuentra-un-empleo?2=programador+c%23&13=&fecha=&categoria=&8=&14=&inclusion=&f=2"
                };
            int n = links.Length;
            int i = n;
            
            

            //Init Infinite loop
            while (i > 0)
            {
                foreach (string link in links)
                {
                    string doc = caller.GetDom(link);
                    List<JobItem> jobList = docGear.ListJobs(doc);

                    //Por cada trabajo validará la fecha e inmediatamente sonará un pito si se publicó un trabajo hoy mismo
                    foreach (var job in jobList)
                    {
                        if (DateTime.Now == job.CalendarDate)
                        {
                            //Hereeeeeee: Falta guardar en un log el Job
                            Console.Beep(800,2000); //Hz,Mili Segundos
                        }
                    }
                }
                i--;
                if (i == 0)
                {
                    Thread.Sleep(5 * 60000);//1min = 60.000milis
                    i = n;
                }
            }
            
            // #region Tests
            // CallerTest callerTest = new CallerTest();
            // callerTest.Caller_GetDom_StringTest(links[0]);
            // #endregion
        }
    }
}