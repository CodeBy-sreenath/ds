function greet(name,callback)
{
    console.log("hello",name)
    callback()

}
function sayHello()
{
    console.log("good morning")
}
greet("srrenath",sayHello)