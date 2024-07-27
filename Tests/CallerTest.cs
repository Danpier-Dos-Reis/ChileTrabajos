using ChileTrabajos.Engine;

namespace ChileTrabajos.Tests
{
    public class CallerTest
    {
        public void Caller_GetDom_StringTest(string url){
            //arrange
            Caller caller = new Caller();
            
            //act
            string result = caller.GetDom(url);
            
            //assert
            if(!string.IsNullOrEmpty(result)){Console.WriteLine("Si obtenemos el dom");}
            else {Console.WriteLine("No obtenemos el dom");}
        }
    }
}