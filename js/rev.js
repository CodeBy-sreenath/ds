function reverseString(s)
{
    let str=""
    for(let i=s.length-1;i>=0;i--)
    {
        str+=s[i]
    }
    return str
}
console.log(reverseString("sreenath"))