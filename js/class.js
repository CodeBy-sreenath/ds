class Student
{
    constructor(name,age)
    {
        this.name=name
        this.age=age
    }
    display()
    {
        console.log(this.name,this.age)
    }
}
const s1=new Student("sreenath",21)
s1.display()