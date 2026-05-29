 let arr=[1,2,3,4]
let result=arr.map(function(num){
    return num*2
    
})
let evenNumbers=arr.filter(function(num){
    return num%2===0
})
console.log(result)
console.log(evenNumbers)