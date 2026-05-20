async function greet()
{
    return "Hello"
}
greet().then((message)=>console.log(message))
//is same as theat of
function greet()
{
    return Promise.resolve("Hello")
}
greet().then((message)=>console.log(message))