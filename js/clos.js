function outer()
{
    count=0
    function inner()
    {
        count++
        return count
    }
    return inner
}
const counter=outer()
console.log(counter())
console.log(counter())