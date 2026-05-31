function sayHello(){
    return new Promise((resolve)=>{
        setTimeout(()=>{
            console.log("after 3 seconds")
            resolve("completed")
        },3000)
    })
}
async function hello(){
    console.log("hai")
    let result=await sayHello()
    console.log(result)
    console.log("sreenath")
}
hello()