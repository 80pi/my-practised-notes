using System;
using System.Collections.Generic;
using System.Text;

namespace Practice
{
    class Parent1
    {
        public void div()
        {
            Console.WriteLine("can div");
        }
        public void mul()
        {
            Console.WriteLine("can multiply");
        }
        public virtual void d()
        {
            Console.WriteLine("can /");
        }
    }
}
