import React from 'react'
import { useParams } from 'react-router-dom'


const ToDoItem = ({todo})=>{
    return (
        <tr>
            <td>{todo.todo_text}</td>
            <td>{todo.todo_project.proj_name}</td>
            <td>{todo.created}</td>
            <td>{todo.td_user.username}</td>
        </tr>
    )
}

const ToDoList =({todos})=>{
     let { id } = useParams();
     if (todos.length !==0){
     let filtered_items = todos.filter((todos) => todos.todo_project.id === +id)
     return (
        <table>
            <th>Text</th>
            <th>TODO_project</th>
            <th>Created</th>
            <th>User</th>
            {filtered_items.map((tod)=><ToDoItem todo={tod}/>)}
        </table>
    )}
    else{
    return(
    <table>
            <th>Text</th>
            <th>TODO_project</th>
            <th>Created</th>
            <th>User</th>
        </table>)
}}

export default  ToDoList