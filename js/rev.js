function reverse(s)
{
    let str=""
    for(let ch of s)
    {
        str=ch+str
    }
    return str
}
console.log(reverse("sreenath"))