using System;
using System.Collections.Generic;
using System.Text;

namespace Practice
{
    class Parent2 : Parent1
    {
        public void add()
        {
            Console.WriteLine("can add");
        }
        public void min()
        {
            Console.WriteLine("can minus");
        }
        public void d()
        {
            Console.WriteLine("can %");
        }
        //method overloading
        public void a(int a,int b)
        {
            Console.WriteLine(a + b);
        }
        public void a(int a, int b,int c)
        {
            Console.WriteLine(a + b+c);
        }
}
}
