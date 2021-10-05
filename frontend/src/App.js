import React from 'react'
import { Route, Link, Switch,BrowserRouter} from 'react-router-dom'
import axios from 'axios'
import UsersList from './components/Users.js'
import ProjectsList from './components/Projects.js'
import ToDoList from './components/TODO.js'

const NotFound404 = ({ location }) => {
  return (
    <div>
        <h1>Страница по адресу '{location.pathname}' не найдена</h1>
    </div>
  )
}


class App extends React.Component{
    constructor(props){
        super(props)
        this.state={
            'tdusers':[],
            'projects':[],
            'todos':[]
        }
    }
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/tdusers/')
        .then(response => {
           const tdusers = response.data
               this.setState(
               {
                   'tdusers': tdusers
               }
           )
       }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
           const projects = response.data
               this.setState(
               {
                   'projects': Object.values(projects)[3]
               }
           )
       }).catch(error => console.log(error))
        axios.get('http://127.0.0.1:8000/api/todo/')
        .then(response => {
           const todos = response.data
               this.setState(
               {
                   'todos': Object.values(todos)[3]
               }
           )

       }).catch(error => console.log(error))
    }


    render(){
        return(
        <div>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li><Link to='/'> Users </Link></li>
                        <li><Link to='/projects'> Projects </Link></li>
                    </ul>
                </nav>
             <Switch>

            <Route exact path='/' component={() =>  <UsersList tdusers={this.state.tdusers}/>}  />
            <Route exact path='/projects' component={() =>  <ProjectsList projects={this.state.projects}/>}  />
            <Route exact path="/todo/:id">
                <ToDoList todos={this.state.todos} />
            </Route>
            <Route component={NotFound404} />
            </Switch>

            </BrowserRouter>

        </div>

        )
        }
}


export default App;
