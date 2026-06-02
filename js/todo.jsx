import { useState } from "react";

function App()
{
    const[todos,setTodos]=useState([])
    const[input,setInput]=useState("")
    function addTodo()
    {
        if(input.trim()==="")
        {
            return
        }
        setTodos([...todos,input])
        setInput("")
    }
    function deleteTodo(index){
        const updateTodo=todos.filter((_,i)=>i!=index)
        setTodos(updateTodo)
    }
    return(
        <div>
            <h1>ToDo App</h1>
            <input type="text" placeholder="enter todo" value={input} onChange={(e)=>setInput(e.target.value)} />
            <button onClick={addTodo} >Add</button>
            <ul>
                {
                    todos.map((todo,index)=>(
                        <li key={index}>{todo}
                        <button onClick={()=>deleteTodo(index)}>Delete</button>
                        
                        </li>
                    ))
                }
            </ul>
        </div>
    )
}
