function largest(arr)
{
   let lar=arr[0]
    for(let i=0;i<arr.length;i++)
    {
        if (arr[i]>lar)
        {
            lar=arr[i]
        }
    }
    return lar


}
console.log(largest([1,6,7,9,0]))
