using System;
namespace Practice
{
    class Program
    {
        static void Main(string[] args)
        {
            //used to print on the screen
            //Console.WriteLine("Hello World!");
            //or
            //Console.Write("hello");//used to print but on same line it does go to next line like write line

            /*used to take input from users and also used to make console visible after debugging stop we change the option like 
            Tools>Options>debugging>Automically close clonsle after exection>select it and click ok*/
            //Console.ReadLine();

            //data types
            //int a = 5;
            //string b = "gopi";
            //char c='A';
            //double d = 3.4;
            //long e = 234;
            //bool istr = true;//or false with out quotations
            //float f = 12.45f;
            //Console.WriteLine("your id is " + a);
            //Console.WriteLine("your name is " + b);
            //Console.WriteLine("your grade is " + c);
            //Console.WriteLine("your cgpa is " + d);
            //Console.WriteLine("your phone is " + e);
            //Console.WriteLine("your male is " + istr);
            //Console.WriteLine("your scpa is " + f);

            //print on next line
            //Console.WriteLine("hwll\ngopi");
            //Console.WriteLine("hwll\'gopi\'");

            //Some string methods
            //string s = "hello world";
            //Console.WriteLine(s.Length);
            //Console.WriteLine(s.ToLower()+" "+s.ToUpper());
            //Console.WriteLine(s.Contains('e'));
            //Console.WriteLine(s.Contains("world"));//search both char and str
            //Console.WriteLine(s[0]);
            //Console.WriteLine(s.IndexOf('w'));
            //Console.WriteLine(s.IndexOf("world"));
            //Console.WriteLine(s.Substring(3));
            //Console.WriteLine(s.Substring(3,5));
            //Console.WriteLine(s.Substring(s.IndexOf("world")));

            //number methods
            //int a = 5,b=4;
            //Console.WriteLine(a+b);
            //Console.WriteLine(a - b);
            //Console.WriteLine(a / b);
            //Console.WriteLine(a * b);
            //Console.WriteLine(a % b);
            //Console.WriteLine(5/2.0);//to get decimal values
            //here bodmis rule is applied here


            //to read input from user
            //int a = Convert.ToInt32(Console.ReadLine());//string ot int
            //double d = Convert.ToDouble(Console.ReadLine());//string to double
            //int a1 = 5;
            //double d1 = a1;//int to double
            //int a2 = (int)d1;//double to int
            //int a3 = Convert.ToInt32(d1);//or this is second method to convert but str to int (int) is not possilbel here
            /*type casting bzc readline take input as strin gto change string 
            to int is done by type casting*/
            //Console.WriteLine(a+" "+d+" "+a2+" "+a3);

            //Arrays
            //int[] a = {1,2,3,3,4,5,6 };
            //Console.WriteLine(a[2]);
            //a[2] = 455;
            //Console.WriteLine(a[2]);
            //to read and display array
            /*string[] s = new string[5];
            for(int i = 0; i < 5; i++)//for loop
            {
                s[i] = Console.ReadLine();
            }
            /*for (int i = 0; i < 5; i++)
            {
                Console.WriteLine(s[i]);
            }*/
            /*Array.Reverse(s);
            foreach (string i in s)//foreach loop
            {
                Console.WriteLine(i);
            }*/

            //while loop
            //int i = 0;
            //while (i < 5)
            //{
            //    Console.WriteLine(i);
            //    i++;
            //}

            //do while loop 
            //int i = 6;//at here it works for n time upto satify the given conditon 
            //do//it exectud for one time if condition is wrong
            //{
            //    Console.WriteLine(i);
            //    i++;
            //} while (i < 4);

            // if else else if
            /*int i = 5;
            if (i == 3)
            {
                Console.WriteLine("ypur 3");
            }
            else if (i == 4)
            {
                Console.WriteLine("ur 4");
            }
            else
            {
                Console.WriteLine("finally");
            }*/

            //cst concation question
            /*int i = 5;
            Console.WriteLine(56+"25"+" "+" "+"20"+"30"+" "+"36"+52);
            Console.WriteLine(20 + 30);*///if 20+30in the above line means that str concation only occurs here

            //method 
            /*static void hh()
            {
                Console.WriteLine("hai gopi");
            }
            hh();
            */

            //method with parameters and return type
            /*static string hh(string a)//here our return type is string bzc it is returning string
            {//return type is sspecified bsed on its returning type data type
                return("hai"+a);
            }
            Console.WriteLine(hh("gopi"));*/



            //2d array
            //int[,] a = { { 1, 2 }, { 3, 4 }, { 5, 6 } };//2d array manuually
            //Console.WriteLine(a[0, 1]);
            //2d array by vlaues input by users
            /*int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            int[,] a1= new int[a, b];
            for (int i = 0; i < a; i++)
            {
                for(int j = 0; j < b; j++)
                {
                    int c= Convert.ToInt32(Console.ReadLine());
                    a1[i, j] = c;
                }
            }
            for (int i = 0; i < a; i++)
            {
                for (int j = 0; j < b; j++)
                {
                    Console.WriteLine(a1[i,j]);
                }
            }*/

            //try and catch
            /*try
            {
                int a = Convert.ToInt32(Console.ReadLine());
                int b = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine(a / b);
            }
            catch(Exception e)
            {
                Console.WriteLine(e.Message);
            }
            */

            /* //classes on other class vreate with name book with out parametrs
             Book b = new Book();//creating object
             b.n = "gopi";
             b.i = 2;
             Book b1 = new Book();
             b1.n = "gopi1";
             b1.i = 22;

             Console.WriteLine(b.n + " " + b.i);
             Console.WriteLine(b1.n + " " + b1.i);*/

            //classes on other class vreate with name book with parametrs for constructor
            /* Book b = new Book("gopi",1);//creating object
             b.i = 2;//we can seoeratly change values
             Book b1 = new Book("ajay",3);
             b1.i = 22;
             Book bb = new Book();
             bb.n = "asd";
             bb.i = 234;

             Console.WriteLine(b.n + " " + b.i);
             Console.WriteLine(b1.n + " " + b1.i);
             Console.WriteLine(bb.n + " " + bb.i);*/

            //object methods with return tyoe
            /*Book b = new Book("gopi", 1);
            Console.WriteLine(b.h());*/

            //encaplusation getters and setter we can not acces  directly
            /*
            Book b = new Book("gopi", 1);
            Book b1 = new Book("gopi1", 11);
            Console.WriteLine(b.nn);
            Console.WriteLine(b.ii);
            Console.WriteLine(b1.nn);
            Console.WriteLine(b1.ii);
            b.nn = "ajay";
            b.ii = 234;
            b1.nn = "gopiajay";
            b1.ii = 123234;
            Console.WriteLine(b.nn);
            Console.WriteLine(b.ii);
            Console.WriteLine(b1.nn);
            Console.WriteLine(b1.ii);
            //we cannnot directly change the value we can change value only with get and sret function only 
            //with function name only we can change value only
            */
            //static AND WITH OUT STATIC
            /*
            Book b=new Book();
            Book b1=new Book();
            */

            //static method
            //Book.say();

            //static class

            //Book.say();
            //Book.ss();

            //inheritance
            /*
            Parent1 p1 = new Parent1();
            Parent2 p2 = new Parent2();
            p1.d();//method overriding
            p1.div();
            p1.mul();
            Console.WriteLine("second obj");
            p2.d();//method overriding
            p2.add();
            p2.min();
            p2.div();
            p2.mul();
            p2.a(1, 2);//method overrodoing
            p2.a(1, 2, 3);//method overriding
            */



            //Console.ReadLine();
        }
    }
}
