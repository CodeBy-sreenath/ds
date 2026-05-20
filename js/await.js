function delay()
{
    return new Promise(resolve=>{
        setTimeout(()=>{
            resolve("delayed for 2 seconds")
        },2000)
    })
}
async function run()
{
    console.log("start")
    let result=await delay()
    console.log(result)
    console.log("end")
}
run()