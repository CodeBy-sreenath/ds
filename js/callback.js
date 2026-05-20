function greet(name,callback)
{
    console.log("Hello" +name)
    callback()
}
function sayHello()
{
    console.log("good by")
}
greet("sreenath",sayHello)