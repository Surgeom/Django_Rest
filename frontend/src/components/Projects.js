import React from 'react'
import {Link} from 'react-router-dom'


const ProjectItem = ({project})=>{
    return (
        <tr>
            <td>{project.proj_name}</td>
            <td>{project.repo_url}</td>
            <td>{Object.values(project.td_users).map(id=>id.username).join()}</td>
            <td><Link to={`todo/${project.id}`}>TODO</Link></td>
        </tr>
    )
}

const ProjectsList =({projects})=>{
    return (
        <table>
            <th>Proj_name</th>
            <th>Repo_url</th>
            <th>Td_users</th>
            <th>Todos</th>
            {projects.map((proj)=><ProjectItem project={proj}/>)}
        </table>
    )
}

export default  ProjectsList