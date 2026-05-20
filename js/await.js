function delay(){
    return new Promise(resolve=>{
        setTimeout(()=>{
            resolve("finished after three seconds")
        },3000)
    })
}
async function run()
{
    console.log("start")
    let resukt=await delay()
    console.log(resukt)
    console.log("end")
}
run()