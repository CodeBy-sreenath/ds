function greet(name,callback)
{
    console.log(name + " hai ")
    callback()
}
function sayGoodby()
{
    console.log("good by")
}
greet("sreenath",sayGoodby)