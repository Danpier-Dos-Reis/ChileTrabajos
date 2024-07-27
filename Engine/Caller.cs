namespace ChileTrabajos.Engine
{
    public class Caller
    {
        public string GetDom(string url)
        {
            using (HttpClient client = new HttpClient())
            {
                return client.GetStringAsync(url).Result;
            }
        }
    }
}