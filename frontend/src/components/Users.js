import React from 'react'

const UserItem = ({tduser})=>{
    return (
        <tr>
            <td>{tduser.username}</td>
            <td>{tduser.first_name}</td>
            <td>{tduser.last_name}</td>
            <td>{tduser.email}</td>
        </tr>
    )
}

const UsersList =({tdusers})=>{
    return (
        <table>
            <th>Nickname</th>
            <th>First_name</th>
            <th>Last_name</th>
            <th>Email</th>
            {tdusers.map((user)=><UserItem tduser={user}/>)}
        </table>
    )
}

export default  UsersList