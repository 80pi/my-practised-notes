// to display msg
// document.write("hello world");

//for pop up
// window.alert("hai");

// to write html in javascript
// document.write("<h2>hello world</h2>")

//to print one after other
// document.write("hello world"+"<br>");
// document.write("hai"+"<br>"+"hello"+"<br>"+"gopi");

//to draw line between paras
// document.write("hai")
// document.write("<hr>")
// document.write("gopi")

//variables
// var a=5,b='a',c="gopi",d='ajay',e="w",f=3.4
// document.write("you age is "+a)
// document.write("<br>")
// document.write(b)
// document.write("<br>")
// document.write(c)
// document.write("<br>")
// document.write(d)
// document.write("<br>")
// document.write(e)
// document.write("<br>")
// document.write(f)
// document.write("<br>")

//type cating
// document.write(100+Number("234")+"<br>")
// document.write(100+parseInt("123")+"<br>")
// document.write(100+parseFloat("123.6")+"<br>")

// string methods
// var n="gopi venkata ajay",n1='ajay'
// var str = "Hello world, welcome to the universe.";
// document.write(n.length+"<br>")//length
// document.write(n.charAt(0)+"<br>")//charter at
// document.write(n.indexOf("o")+"<br>")//index of
// document.write(n.indexOf("opi")+"<br>")
// document.write(n.substring(1)+"<br>")//substirng with out range
// document.write(n.substring(1,3)+"<br>")//substr with range
// document.write(n.concat(n1)+"<br>")//concate
// document.write(str.includes("world")+"<br>")//true/false
// document.write(n.repeat(2)+"<br>")//repeats
// var s=str.replace('world','gopi')//replacing
// document.write(s+"<br>")
// document.write(n.search('pi')+"<br>")
// document.write(n.slice(-4,-1)+"<br>")
// var a=n.split("a");
// document.write(a+"<br>")
// document.write(n.toUpperCase()+"<br>")
// var k="ASdf"
// document.write(k.toLowerCase()+"<br>")
// document.write(k.toUpperCase()+"<br>")
// var q=23
// document.write("15"+q.toString()+"<br>")


//to copy paste
//document.write("");

//numbers
// document.write((3+2)+"<br>"+(3-2)+"<br>"+3*2+"<br>"+30/2.0+"<br>")
// var a=100
// document.write((a++)+"<br>"+(a--)+"<br>"+(++a)+"<br>"+(--a)+"<br>");
// document.write(Math.sqrt(36)+"<br>");
// document.write(Math.pow(2,3)+"<br>");
// document.write(Math.round(2.3)+"<br>");

//to take user inputs
// var n=window.prompt("enter u name: ")
// alert('u name is '+n);

// functions
// function add(a,b){
// 	return a+b;
// }
// function h(n)
// {
// 	document.write("hello "+n)
// }

// document.write(add(5,4));
// var n=window.prompt("enter u name: ")
// h(n)

//arrays
// var a=[9,8,8,7,4,61,2,3,4,5]
//to print array
// for (var i = 0; i < a.length; i++) {
// 	document.write(a[i]+"<br>");
// }
// or we can directly print it by
// document.write(a);

// to sort
// a.sort()

//to reversr
// a.reverse();

//to find length
// document.write(a.length);

//to update
// a[0]=1234

//to add elements
// a.push("gopi")

//to pop last elemnt
// a.pop()

//to remove first element
// a.shift()

// to  add at first
// a.unshift(567)

//to join a array with special symbol
// document.write(a.join(" "));

//to map
// var a=[1,2,3,4]
// var s=a.map(Math.sqrt)//round
// document.write(s)

// // to fill array with one elemet
// var a=[1,3,4,5]
// a.fill(0,)
// document.write(a)

// to fill array with one elemet with range
// var a=[1,3,4,5]
// a.fill(0,1,3)
// document.write(a)

//function sto give color with help of id
// var s=document.getElementById('ss')
// ss.style="color:red;background-color:black"

//if,else,elseif
// var n=window.prompt("enter a number")
// if(n==3)
// {
// 	alert("hhh")
// }
// else if(n==4)
// {
// 	document.write("klj")
// }
// else if(n==5)
// {
// 	document.write("kiu")
// }
// else{
// 	document.write("error")
// }

//switch
// var n=window.prompt("enter u grade: ")
// switch(n)
// {
// 	case 'a':
// 		document.write("Excellent");
// 		break;
// 	case 'a--':
// 		document.write("Nice");
// 		break;
// 	case 'b':
// 		document.write("Good");
// 		break;
// 	case 'bb':
// 		document.write("pass");
// 		break;
// 	case 'c':
// 		document.write("Fail");
// 		break;
// 	default:
// 		document.write("enter correct grade");
// 		break;

// }

//while
// var i=0
// while(i<5){
// document.write(i+"<br>")
// i++}

// //for lop
// for (var i = 0; i < 10; i++) {
// 	document.write(i+"<br>")
// }

//do while
// i=7
// do
// {
// 	document.write(i)
// 	i++
// }while(i<6)

//try catch finally throw
// try
// {
// 	// var x=y+9
// 	throw "u had not defined x"//if throw is defined we need to place it correctly
// }
// catch(err)
// {
// 	document.write(err+"<br>")

// }
// finally
// {
// 	document.write("i will print it")
// }

// class and objrcts
// class Book
// {
// 	constructor(ti,au)
// 	{
// 		this.ti=ti
// 		this.au=au
// 	}
// 	rea()
// 	{
// 		document.write("u r reading "+this.ti+" written by "+this.au)
// 	}
// }

// var b1=new Book("abc","gopi")
// var b2=new Book("aaa","ddd")
// document.write(b1.ti+"<br>")
// document.write(b2.ti+"<br>")
// b1.rea();
// document.write("<br>")
// b1.ti="kln"
// document.write(b1.ti+"<br>")//value updating
// b2.rea();


// //encapusaltion
// class Book
// {
// 	constructor()
// 	{
// 		var ti
// 		var au
// 	}
// 	setti(ti)
// 	{
// 		document.write("setting"+"<br>")
// 		this.ti=ti
// 	}
// 	getti()
// 	{
// 		document.write("getting"+"<br>")
// 		return this.ti
// 	}
// 	setau(au)
// 	{
// 		document.write("setting"+"<br>")
// 		this.au=au
// 	}
// 	getau()
// 	{
// 		document.write("getting"+"<br>")
// 		return this.au
// 	}
// 	rea()
// 	{
// 		document.write("u r reading "+this.ti+" written by "+this.au)
// 	}
// }

// var b1=new Book()
// b1.setti("gopi")
// var s=b1.getti()
// document.write(s+"<br>")
// b1.setau("gopilop")
// var s1=b1.getau()
// document.write(s1+"<br>")
// b1.rea();

//inheritance
// class Ac
// {
// 	canro(){
// 		document.write("can rotate")
// 	}
// 	cansw(){
// 		document.write("can swing")
// 	}
// 	temp()
// 	{
// 		document.write("temp can inc or dec")
// 	}
// }
// class co extends Ac
// {
// 	col()
// 	{
// 		document.write("cost is less")
// 	}
// 	fan()
// 	{
// 		document.write("has fans inside")
// 	}
// 	temp()
// 	{
// 		document.write("has fiber in it temp can be inc or dec")
// 	}
// }
// var a1=new Ac()
// a1.canro();
// document.write("<br>")
// a1.cansw();
// document.write("<br>")
// a1.temp();//overriding
// document.write("<br>")
// var a2=new co()

// a2.canro();//inheritance
// document.write("<br>")
// a2.cansw();//inhetiytanve
// document.write("<br>")
// a2.col();
// document.write("<br>")
// a2.fan();
// document.write("<br>")
// a2.temp();//overriding
// document.write("<br>")

// super inhertance by constructor
class A
{
	constructor(a,b)
	{
		this.a=a
		this.b=b
	}
	pp()
	{
		document.write("ur name is "+this.a+" ur age "+this.b)
	}

}
class b extends A
{
	constructor(a,b,c){
		super(a,b)
		this.c=c
	}
	pap()
	{
		document.write("ur name is "+this.a+" ur age "+this.b+" ur country is "+this.c)
	}

}

var a=new A("gopi",12)
a.pp()
document.write("<br>")
var b1=new b("ajay",56,"gut")
b1.pap()
