function message()
{
    return new Promise((resolve)=>{
        setTimeout(()=>{
            resolve("Hello")
        },2000)
    })
}
async function showMessage()
{
    console.log("Srenath")
    let result=await message()
    console.log(result)
}
showMessage()