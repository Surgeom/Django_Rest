import React from 'react'
import { Route, Link, Switch,BrowserRouter} from 'react-router-dom'
import axios from 'axios'
import UsersList from './components/Users.js'
import ProjectsList from './components/Projects.js'
import ToDoList from './components/TODO.js'
import LoginForm from './components/LoginForm.js'

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
            'todos':[],
            'token':null
        }
    }

    getToken(login,password){
        axios.post('http://127.0.0.1:8000/api-token-auth/',{"username":login,"password":password})
        .then(response =>{
                localStorage.setItem('token',response.data.token)
                console.log(localStorage)
                this.setState({
                    'token': response.data.token
                },this.loadData)

            }
        ).catch(error=>alert("Wrong password")
        )

    }

    logout(){
        localStorage.setItem('token','')
                this.setState({
                    'token': ''
                },this.loadData)
    }



    isAuthenticated(){
        return !!this.state.token
    }

    getHeaders(){
        if(this.isAuthenticated()){
            return {"Authorization" : "Token " + this.state.token}
        }
        return{}
    }

    loadData(){
                const headers=this.getHeaders()
        axios.get('http://127.0.0.1:8000/api/tdusers/',{headers})
        .then(response => {
           const tdusers = response.data
               this.setState(
               {
                   'tdusers': tdusers
               }
           )
       }).catch(error => console.log(error),  this.setState(
               {
                   'tdusers': []
               }
           ))
        axios.get('http://127.0.0.1:8000/api/projects/',{headers})
        .then(response => {
           const projects = response.data
               this.setState(
               {
                   'projects': Object.values(projects)[3]
               }
           )
       }).catch(error => console.log(error),this.setState(
               {
                   'projects': []
               }
           ))
        axios.get('http://127.0.0.1:8000/api/todo/',{headers})
        .then(response => {
           const todos = response.data
               this.setState(
               {
                   'todos': Object.values(todos)[3]
               }
           )

       }).catch(error => console.log(error),
                this.setState(
               {
                   'todos': []
               }
           ))

    }

    componentDidMount(){
        const token = localStorage.getItem('token')
        this.setState({
            'token':token
        },this.loadData)

    }


    render(){
        return(
        <div>
            <BrowserRouter>
                <nav>
                    <ul>
                        <li><Link to='/'> Users </Link></li>
                        <li><Link to='/projects'> Projects </Link></li>
                        <li>
                            { this.isAuthenticated() ?
                                <button onClick={()=>this.logout()}>Logout</button>
                                :
                                <Link to='/login'> Login </Link>

                             }
                        </li>
                    </ul>
                </nav>
             <Switch>

            <Route exact path='/' component={() =>  <UsersList tdusers={this.state.tdusers}/>}  />
            <Route exact path='/login' component={() =>  <LoginForm getToken={(login ,password) => this.getToken(login,password)} />} />
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
