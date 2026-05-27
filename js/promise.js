const promise=new Promise((resolve,reject)=>{
    resolve("success")
})
promise.then(data=>console.log(data))