function isAnagram(s,t)
{
    if(s.length!=t.length)
    {
        return false
    }
    let seen={}
    for(let ch of s)
    {
        if(seen[ch])
        {
            seen[ch]++
        }
        else
        {
            seen[ch]=1

        }
    }
    for(let ch of t)
    {
        if(!ch in seen)
        {
            return false
        }
        seen[ch]--
    }
    if(seen[ch]<0)
    {
        return false
    }
    return true
}

console.log(isAnagram("anagram", "nagaram"))
console.log(isAnagram("rat", "car"))         