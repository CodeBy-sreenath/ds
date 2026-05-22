function greet(name,callback)
{
    console.log("Hello," +name)
    callback()

}
function sayHello()
{
    console.log("welcome to the js world")
}
greet("Sreenath",sayHello)