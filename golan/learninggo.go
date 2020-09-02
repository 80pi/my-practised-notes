package main

import (
	"fmt"
)

type person struct { //just like declaring a node
	fname string
	lname string
	age   int
}
type ee struct {
	person
	eid int
}

/*//inheritance

type Comic struct {
	cid int
}
type Marvel struct {
	Comic
}
type dc struct {
	Comic
}*/

func main() {
	//fmt.Println("Hello, World")

	//var i = 23 //we can asssign variables like these
	/*
	   or we can assign like
	   i:=23 or
	   var i int =23 or
	   var i=23
	   these are the 3 types we can assign values to a variable in go*/
	/*fmt.Println("the value of i is ", i)
		  fmt.Printf("the value of i is %v and type is %T \n", i, i)//%T is used to know the type of variable for printf \n need to be put on the stmt or else it print next to it
		//we can also use this reflect.TypeOf(variable name)
		i := 90.36
	fmt.Println(reflect.TypeOf(i))
		  fmt.Print("dddd\n")
		i := "ggg"
	   fmt.Print("myname is as", i)*/

	//To scan Variables
	/*var i,j,k string
	   fmt.Scanln(&k)
			fmt.Scanf("%s", &j)
		   fmt.Scan(&i)
	*/ //order must be like this orelse we will get erroe

	//if else
	/*
			i := 25
			if i%2 == 0 {
				fmt.Println("even")
			} else {
				fmt.Println("odd")
	      }*/

	//switch
	/*
		var i int
		fmt.Scanln(&i)
		switch i {
		case 1:
			fmt.Println("one")
		case 2:
			fmt.Println("two")
		default:
			fmt.Println("Enter in range")
	   }*/

	//for loop
	/*for j := 1; j < 3; j++ {
	      fmt.Println(j)
	   }
	   //nesteed
		for a := 1; a < 6; a++ {
			for j := 1; j < 3; j++ {
				fmt.Println(a * j)
			}
	   }
	*/
	//for in while passsion
	/*
			i := 0
			for i < 6 {
				fmt.Println(i)
				i += 1
		   }
	*/

	//for in range passion
	/*a := []int{1, 2, 3, 4, 5, 6}
	for i, j := range a {
		fmt.Printf("%d->%d\n", i, j)
	}*/

	//goto
	/*
			var i int
		loop:
			fmt.Println("enter age")
			fmt.Scanln(&i)
			if i > 6 {
				fmt.Println("eligi")
			} else {
				goto loop
		   }*/

	//break and continue
	/*
				for i := 0; i < 11; i++ {
					if i == 5 {
						continue
					}
					if i == 9 {
						break
					}
					fmt.Println(i)
		      }
	*/

	//type casting

	//converting int to float
	/*
			i := 10
			s1 := strconv.FormatInt(int64(i), 10)
			s2 := strconv.Itoa(i)
			fmt.Println(float64(i))
			fmt.Println(s1, s2)
		   fmt.Printf("%T, %T\n", s1, s2)
	*/

	//converting flaot to int
	/*i := 12.3
		fmt.Println(int(i)) //float to int
		s1 := strconv.Itoa(int(i))
		fmt.Println(s1)
		fmt.Printf("%T\n", s1)
		s := fmt.Sprintf("%f", i)
	   fmt.Printf("%T", s)
	*/

	//string to int
	/*
			s := "10"
			fmt.Printf("%T", s)
			i, _ := strconv.ParseInt(s, 0, 64)
			fmt.Println(i)
		   fmt.Printf("%T", i)
	*/

	//functions with para
	/*
		s := test("1", "2")
	   fmt.Println(s)*/

	//function without para and return
	//tt()

	//closure function just like lambda
	/*i := 10
		ss := func() int {
			i *= i
			return i
		}
		fmt.Println(ss())
		fmt.Println(ss())
	   fmt.Println(ss())
	*/

	//array for one dimentional
	/*var i [3]int
	for a := 0; a < 3; a++ { //reading
		fmt.Scanln(&i[a])
	}
	for a := 0; a < 3; a++ { //printing
		fmt.Println(i[a])
	}
	//direct method to print a array
	fmt.Println(i)*/

	//for 2d
	/*var i [3][3]int
	for k := 0; k < 3; k++ {
		for a := 0; a < 3; a++ {
			fmt.Scanln(&i[k][a])
		}
	} //reading
	fmt.Println("-----------")
	for k := 0; k < 3; k++ {
		for a := 0; a < 3; a++ {
			fmt.Println(i[k][a])
		} //printing
	}
	fmt.Println(i)//used to print directly a array
	*/

	/*//array making using make function
	k := make([]int, 10)
	k1 := make([]int,  10)
	fmt.Println(k1)
	fmt.Println(k)*/

	//slicing
	//i := [5]int{1, 2, 3, 4, 5}
	/*var k []int = i[0:3]//sliced and assigned
		for a := 0; a < 3; a++ {
			fmt.Println(k[a])
	   }*/
	/*fmt.Println(i)
	i[1] = 90  //updating
	k := i[2:] //upper bound
	j := i[:4] //lower bound
	fmt.Println(i, len(i))
	fmt.Println(k)
	fmt.Println(j)*/

	//command line argumenats
	/*
		for i := 0; i < len(os.Args); i++ {
			fmt.Println(os.Args[i])
		}
		fmt.Println(os.Args)*/

	//string functions
	//s := "Hello World"
	/*k := "k"
	a := 'p'
	fmt.Println(int(a)) //below these 3 methods ca n be used to get ascii values
	fmt.Println(int('p'))
	fmt.Println(rune(a)) //thses 2 methods only tells us only singlel int
	fmt.Println(rune('p'))
	fmt.Println(k[0]) //but this method is used to tell the ascii value of a particular int valu only
	*/
	/*fmt.Println(s)
	fmt.Println(reflect.TypeOf(s)) //to know type
	fmt.Println(len(s))            //to know lenght
	fmt.Println(rune(s[1]))        //to get asci value of string based on index value
	//by the above we get ascii valuue of e
	fmt.Println(strings.ToUpper(s)) //to convert string to upper case
	fmt.Println(strings.ToLower(s)) //convert string to loewer*/
	//fmt.Println(strings.HasSuffix(s, "d"))  //tells that given string is present in the last
	//fmt.Println(strings.HasPrefix(s, "He")) //tells that gieve string is present in the first position sare not
	/*var a = []string{"q", "w", "e", "r", "t"}
	fmt.Println(strings.Join(a, "+")) //used to join a array to string like python*/
	//fmt.Println(strings.Repeat(s, 4))//used to print our string n number of times
	//fmt.Println(strings.Contains(s, "ol"))//tells that given string or a alphabet is present in the strng or not
	//fmt.Println(strings.Index(s, "ll"))//tells the index of first letter in the given strign
	//fmt.Println(strings.Count(s, "l"))//tells no of occurance of given alphabet in the string
	//fmt.Println(strings.Replace(s, "l", "L", 2)) //replace given aplhabet with the given one for given n no of time
	//fmt.Println(strings.ReplaceAll(s, "l", "q"))//it will replace all the alphabet in the givens string
	//k := "hi this is spliitng function"
	//var ss []string = strings.Split(k, " ")
	//fmt.Println(ss, s)
	//fmt.Printf("%v", ss) //used to print array by printf
	//fmt.Println(strings.Split("this is direct function one", " "))
	//fmt.Println(strings.Compare("gopi", "gopi"))//if both string are equal it print 0 if str1 is greater than str2 the 1 is print if viceversa -1 is printed
	//fmt.Println(strings.TrimSpace("     asd asda        "))//used to remove extra spaces in the first and at last
	//fmt.Println(strings.ContainsAny(s, "o&e"))//used to search more than one alphabet or a aphabet in a gropup of alphabet
	//fmt.Println(s)
	//fmt.Println(strings.ContainsAny(s, "a|e|i|o"))

	//pointer
	//i := 25
	/*var k *int
	k = &i
	fmt.Println(i, &i, k, *k)
	fmt.Println(&i)
	fmt.Println(k)
	fmt.Println(*k)*/
	/*fmt.Println(i)
	poitt(&i) //pointer function
	fmt.Println(i)*/

	/*//struct
	//giving data as
	p := person{age: 23, fname: "gopi", lname: "ajay"} //like this we can given values to struct variable randomly wiht thise names or
	//any method we can follow this o nr are above one//p := person{"gopi", "ajay", 22}//here order need to follow bzc names are mention like above
	fmt.Println(p)
	fmt.Println(p.fname, p.lname, p.age)
	p.details()                                          //calling struct function
	e := ee{person: person{"abc", "aja", 65}, eid: 1002} //here we are giving other values to person struct
	e.details()   */ //calling one struct on other

	/*//inheritacne
	c := Comic{123}
	m := Marvel{Comic{456}}
	d := dc{Comic{789}}
	fmt.Println(c, m, d)*/

	//map
	/*x := map[string]int{"a": 1, "b": 2, "c": 3} //creating
	//fmt.Println(x)//printing
	//fmt.Println(x["a"], x["b"], x["c"]) //printing just by reterving the values
	x["d"] = 4     //inserting
	x["a"] = 123   //updating
	delete(x, "d") //deleting
	fmt.Println(x)*/

	//sorting
	/*a := []int{9, 1, 8, 2, 3}
	b := []string{"as", "qw", "fg", "lk"}
	c := []float64{12.34, 12.22, 12.09}
	sort.Ints(a)
	sort.Strings(b)
	sort.Float64s(c)
	fmt.Println(a, b, c)
	sort.Sort(sort.Reverse(sort.IntSlice(a)))//sort in decsendin order
	sort.Sort(sort.Reverse(sort.StringSlice(b)))
	sort.Sort(sort.Reverse(sort.Float64Slice(c)))
	fmt.Println(a, b, c)*/

	//random numbers
	/*rand.Seed(time.Now().Unix())//with out this we cant generate random number only one number is generated commonly with out this for n number of executing
	//with the help of the above line we get diff number for each execution of our code
	fmt.Println(rand.Intn(10), rand.Float64())*/

	//deferto function
	/*defer p1()
	p2()*/

	//panic
	/*for i := 0; i < 5; i++ {
		if i == 3 {
			panic("its 3")
		}
	}*/
	//rr()//used to knoe recovery

	//encoding and decoding
	/*s := "gopivenkataajay"
	en := b64.StdEncoding.EncodeToString([]byte(s)) //for encoding
	de, _ := b64.StdEncoding.DecodeString(en)
	fmt.Println(s)
	fmt.Println(en)
	fmt.Println(de)
	fmt.Println(string(de))*/

} //main func bracket

//recover
func rr() {
	defer func() {
		if r := recover(); r != nil {
			fmt.Println("panic is cleaned\nprogram will stop because of panic \nbut error is=", r)
		}
	}()
	for i := 0; i < 5; i++ {
		if i == 3 {
			panic("its 3")
		}
		fmt.Println(i)
	}
}

//defer funtion exaples
func p1() {
	fmt.Println("p1 is called")
}
func p2() {
	fmt.Println("p2 is called")
}

//struct function
func (pp person) details() {
	fmt.Println("name is as ", pp.fname)
	fmt.Println("name is as ", pp.lname)
	fmt.Println("name is as ", pp.age)
	fmt.Println("name is as ", pp)
}

//struct function calling one struct  on other struct
func (eea ee) details() {
	fmt.Println("name is as ", eea)
	fmt.Println("name is as ", eea.fname)
	fmt.Println("name is as ", eea.lname)
	fmt.Println("name is as ", eea.age)
	fmt.Println("name is as ", eea.eid)

}

//function with pointer
func poitt(q *int) {
	*q = 900
}

//functions with para
func test(i, j string) string {
	return i + " " + j
}

//function without para and return
func tt() {
	fmt.Println("hgesa")
}
