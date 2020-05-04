#include <iostream>

using namespace std;
/*
//function shou;d be top of main not below main
//with parameters
void hi1(string n)
    {
        cout<<"hello world "<<n<<"\n";
    }
//with out parameters
void hi()
    {
        cout<<"hello world "<<"\n";
    }
//with return
int sum(int a,int b)
{
    return(a+b);
}
*/

//cal by value and call by reference
/*
void hai(string n,int i)
    {
        cout<<"hello "<<n<<" ur age is "<<i<<"\n";
    }
void phai(string *n,int *i)
    {

        cout<<"hello "<<*n<<" ur age is "<<*i<<"\n";
    }
 */
 /*
 class Book
 {
     public:
        string n;
        int i;
        Book(string n,int i)
        {
            //this can be used when class variable(n,i) is same to member variable(n,i)
            this->n=n;
            this->i=i;
            //better to use different name in member variables
            //n=a;
            //i=b;
        }
        void say()
        {
            cout<<"hello world";
        }

 };


 */


 //encapsulation calss
 /*
 class B
 {
    private:
        string n;
        int i;
    public:
        B(string n,int i)
        {
            setn(n);
            seti(i);
        }
        void setn(string n)
        {
            this->n=n;
        }
        void seti(int i)
        {
            this->i=i;
        }
        string getn()
        {
            return n;
        }
        int geti()
        {
            return i;
        }

 };**/

 //inheritance
 class A
 {
     public:
     void s(){
     cout<<"can do sum \n";}
      void m()
     {
         cout<<"can do minus \n";
     }
     void d()//over riding
     {
         cout<<"can do /\n";
     }
     void add(int a,int b){
     cout<<a+b<<"\n";}
     void add(int a,int b,int c){
     cout<<a+b+c<<"\n";}
 };
 class B : public A
 {
     public:
     void di()
     {
         cout<<"can do div \n";
     }
      void ml()
     {
         cout<<"can do multpily \n";
     }
     void d()//overriding
     {
         cout<<"can do %\n";
     }
 };
int main()
{
    //tp print
    /*
    cout << "Hello world!" << endl;
    //or
    cout<<"hello world\n";
    cout <<"gopi";
    */
    //vsrisbles
    /*
    string name="gopi";
    int age=5;
    double cpga=9.8;
    bool ismale=true;
    char grade='a';
    cout<<"u name is "<<name<<"\n";
    cout<<"ur age is "<<age<<"\n";
    cout<<name<<" how are u? \n";
    cout<<"u cpga is " <<cpga<<"\n";
    cout<<"u are male "<<ismale<<"\n";
    cout<<"u grade is "<<grade<<"\n";
    */

    //string functions
    /*

    string s="hello";
    cout<<s[0]<<"\n";//to get indexed value
    cout<<s.length()<<"\n";//find length
    cout<<s.find("e",0)<<"\n";//to find whether char is present are not
    cout<<s.find("ello",0)<<"\n";//to find where word is present are not
    cout<<s.substr(0,3);
    */

    //math functions see in book refer it
    //pow,sqrt,fmin,fmax,ceil,floor,round

    //getting user input
    /*
    string a;//int can take only int values but str takes num and str
    cin>>a;
    cout<<"valu is "<<a;
    //another method getline for string
    string s;
    getline(cin,s);
    cout<<s;
    //for cahr take only first char of str / number as 1234 o/p 1 fro asdef o/p a
    char a;
    cin>>a;
    cout<<a;
    */

    //array
    /*
    int a[]={1,2,3};
    a[0]=0;
    cout<<a[0];
    */

    //functions
    /*hi();
    hi1("gopi");
    cout<<sum(2,3);
    */

    //if else else if
    /*
    int i=5;
    if(i==3)
        cout<< "its 3";
    else if(i==4)
        cout<<"its 4";
    else if(i==5)
       cout<<"it 5";
    else
        cout<<"un knoen";
        */
    //switch
    /*
    int i;
    cin>>i;
    switch(i)
    {
        case 1:
            cout<<"mon";
            break;
        case 2:
            cout<<"tue";
            break;
        case 3:
            cout<<"wed";
            break;
        case 4:
            cout<<"thu";
            break;
        case 5:
            cout<<"fri";
            break;
        case 6:
            cout<<"sat";
            break;
        case 7:
            cout<<"sun";
            break;
        default:
            cout<<"give correct no";


    }
    */

    //loop
    //while
    /*
    int i=0;
    while(i<5)
    {
        cout<<i<<"\n";
        i++;
    }
    */
    //do-while
    /*
    int i=7;
    do
    {
        cout<<i<<"\n";
        i++;
    }while(i<5);
    */
    //for loop
    /*
    for(int i=0;i<5;i++)
        cout<<"i is "<<i<<"\n";
        */
    //loop through array
    /*
    int a[]={1,2,3,4,5,6,3,2,2,2,2,2};
    for(int i=0;i<sizeof(a)/sizeof(a[0]);i++)
        cout<<a[i]<<"\n";
    //cout<<sizeof(a)/sizeof(a[0]);//to know the size of a
    */

    //2d arrays
    /*
    int a[4][2]={{1,2},{3,4},{5,6},{7,8}};
    cout<<sizeof(a)/sizeof(a[0]);
    */

    //read 2d array
    /*
    int m,n;
    cin>>m;
    cin>>n;
    int a[m][n];
    for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                cin>>a[i][j];}}
    for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                cout<<a[i][j]<<"\n";}}
                */
    //pointers
    /*
    int i=5,*j;
    cout<<i<<"\n";
    cout<<&i<<"\n";
    j=&i;
    cout<<j<<"\n";
    cout<<*j<<"\n";
    */

    //call by valure call by refernce
    /*
    int i=3;
    string a="gopi";
    hai(a,i);
    phai(&a,&i);
    */


    //classes and objr=ects
    /*
    Book b;
    b.n="gopi";
    b.i=9;
    Book b1;
    b1.n="gopajay";
    b1.i=92;
    cout<<b.n<<"\t"<<b.i<<"\n";
    cout<<b1.n<<"\t"<<b1.i<<"\n";
    */

    //constructor
    /*
    Book b("gopi",1);
    Book b1("basd",2);
    cout<<b.n<<"\t"<<b.i<<"\n";
    cout<<b1.n<<"\t"<<b1.i<<"\n";
    b.say();//object functions
    b1.say();
    */

    //encapsulation calss
    /*
    B b("abc",23);
    B b1("def",25);
    cout<<b.geti()<<"\t"<<b.getn()<<"\n";
    cout<<b1.geti()<<"\t"<<b1.getn()<<"\n";
    b.seti(1);
    b.setn("asdgoip");
    b1.seti(5);
    b1.setn("ajay goip");
    cout<<b.geti()<<"\t"<<b.getn()<<"\n";
    cout<<b1.geti()<<"\t"<<b1.getn()<<"\n";*/

    //inheritance
    /*
    A a;
    a.s();
    a.m();
    a.d();//overriding
    B b;
    b.s();
    b.m();
    b.d();//overriding
    b.ml();
    b.di();
    b.add(1,2);
    a.add(1,2,3);
    */
    //overloading

    //try catch exceptions
    /*
    int a,b;
    cin>>a;
    cin>>b;
    try
    {
        if(b==0)
        {
            throw b;
        }
        int c=a/b;
        cout<<c;
    }
    catch(...)
    {
        cout<<"Error raiesd diviede by zero";

    }
    */
    //cout<<1/0;




    //my own learning c++
    /*//operators
    int i=2;
    //cout<<5+4<<"\n"<<5-4<<"\n"<<5/4<<"\n"<<5%4<<"\n"<<5/4.0<<"\n";
    //cout<<i++<<"\n"<<i--<<"\n"<<++i<<"\n"<<--i;
    cout<< i*3*2*1<<"\n";//<<i-=5<<"\n"<<i*=5<<"\n"<<i/=5<<"\n"<<;*/



    return 0;
}
