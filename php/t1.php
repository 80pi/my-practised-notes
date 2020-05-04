<?php

// to print an thing
// echo "my age is gopi";

// to print multiple lines
// echo "hello world <br>";
// echo "my age is gopi";

// variable asign
// $name="gopi";// dollar is a must before variable name
// $age=23;//int
// $height=5.6;//float
// echo "hello world name is $name <br>";
// echo "my age is $age and height is $height";


// string methods
// $s="hello world";
// echo strtoupper($s);//to uppercase
// echo "<br>";// to print on next line
// echo strtolower($s);//to print lower case
// echo str_word_count($s);//lenght of string
// echo strrev($s)//reverse
// echo strpos($s,"world");
// echo str_replace("world","gopi",$s);//replace the first old word with new word in $s
// echo ord("a")//return asci value
// echo chr(97);//asci value to string
// print_r(str_split($s));//this print_r is only printiing the array if we use echo here it is only printing the array just see
// echo $s;//below three are same
// Echo $s;
// ECHO $s;
// echo strcmp($s,"hello world");//compare our string with second string
// echo strcasecmp($s,"Hello world");//se\ame as above but it neglects case sentivity
// echo strchr("Hello world!","or");//if the given is there in our string it print from there to last else it return false
// echo wordwrap($s,2,"<br>",true);//to break the string into n number of given parts
// echo substr_count("Hello world. The world is nice","world");//coutn the number of "world" in the string and return the count in return
// echo substr_replace($s,"world",2); 


// arrays
// $a=array(1,2.908,3,4,"gopi",true,false);//to create a array  "array" keyword must be there a array contains all the data type on it as a container
// sort($a);//to sort a array when all dara types are present srting is done based on ascii values sort on asccecndiing
// $a=array(1,2,2,3,4,5);
// array_push($a,9,4,19,12.36);//push elements like python
// array_pop($a);//pop the last value
// echo(array_sum($a));//sum of array if char is present sum is return works for in,float also string while sum str is neglected and return sum
// echo (array_product($a));//product of array if char is present '0' is return works for in,float
// rsort($a);//sort descending
// print_r($a);//to print whole array
// $aa=range(0, 5);//to create a array of given range
// print_r(array_slice($a,1,3));//second is starting index from our selscted list and third one is no of digits it need to print here
// print_r($a);


// associate arrsy judt like dictionary in python as
// $aa=array("gopi"=>"a+","bhae"=>"a","as"=>"b+");
// echo $aa["gopi"];


// function with no para meters
// function sh(){
// 	echo "hello wolrd";
// }
// sh();

// function with para meters
// function sh($a,$b){
// 	echo "hello $a <br>";
// 	echo "your age is $b";
// }
// sh("gopi",22); 

// function with para meters and return
// function sh($a,$b){
// 	return $a+$b;
// 	}
// echo sh(20,22);

// if else  and else if
// $a=1;
// if($a==3){
// 	echo "yes";
// }
// elseif ($a==1) {
// 	echo "yaa";
// }
// else{
// 	echo "no";
// }

// switch
// $a=23;
// switch ($a) {
// 	case 25:
// 		echo "good";
// 		break;
// 	case 24:
// 		echo "well";
// 		break;
// 	case 23:
// 		echo "nice";
// 		break;
	
// 	default:
// 		echo "enter correct nu";
// 		break;
// }


// while loop
// $i=0;
// while ($i<7) {
// 	echo "$i <br>";
// 	$i++;
// }


// do while loop
// $i=7;
// do{
// 	echo "$i <br>";
// 	$i++;
// }while ($i<7);


// for loop
// for($i=0;$i<7;$i++){
// 	echo "$i <br>";
// }


// class
// class Book{
// 	var $tt;
// 	var $aa;
// 	var $bp;
// }
// $b=new Book;
// $b->tt="abc";
// $b->aa="def";
// $b->bp=123;

// $b1=new Book;
// $b1->tt="hpo";
// $b1->aa="xuc";
// $b1->bp=569;

// echo $b->aa."<br>";
// echo $b1->bp;

// // constructor
// class Book{
// 	var $tt;
// 	var $aa;
// 	var $bp;

// 	function __construct($a,$b,$c){
// 		$this->tt=$a;//this and below are do the same thing as $objectname->classvariablename=value; here this means that particular instabe of class means the particular object to assign value only to that instanve variable only
// 		$this->aa=$b;
// 		$this->bp=$c;
// 	}
// }
// $b=new Book("abx","def",123);
// $b->tt="abc";//ad ,iddle aslo we can change the value by doing like this

// $b1=new Book("qwe","ert",456);

// echo $b->tt."<br>";
// echo $b1->bp;


// 

// getters and setters
// class Book{
// 	private $name;
// 	private $age;

	// function __construct($a,$b){
	// 	$this->setName($a);
	// 	$this->setAge($b);
	// 	//or
	// 	//$this->name=$a;
	// 	//$this->age=$b;

		
// 	}
// 	function sayhel(){
// 		echo "hello $aa<br>";
// 	}
// 	function setName($a){
// 		$this->name=$a;
// 	}
// 	function setAge($b){
// 		$this->age=$b;
// 	}
// 	function getName(){
// 		return $this->name;
// 	}
// 	function getAge(){
// 		return $this->age;
// 	}
// }
// $b=new Book("a",1);
// //ad ,iddle aslo we can change the value by doing like this

// $b1=new Book("b",2);
// $b->setName("gopi");
// $b1->setName("gopi1");
// $b->setAge(1);
// $b1->setAge(2);
// echo $b->getName()."<br>";
// echo $b->getAge()."<br>";
// echo $b1->getName()."<br>";
// echo $b1->getAge()."<br>"


// //inhertance
class a{
	function s(){
	echo "hi sum";}
	function m(){
	echo "hi min";}
	function d(){
	echo "can /";}
}
class b extends a{
	function di(){
	echo "hi di";}
	function mu(){
	echo "hi mun";}
	function d(){
	echo "can %";}
}
$a1= new a();
$a1->s();
echo "<br>";
$a1->m();
echo "<br>";
$a1->d();//this metho dis s called overriding
echo "<br>";
$b1=new b();
$b1->s();
echo "<br>";
$b1->m();
echo "<br>";
$b1->d();
echo "<br>";//also this is tooo
$b1->di();
echo "<br>";
$b1->mu();
echo "<br>";

?>

