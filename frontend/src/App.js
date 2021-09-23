import React from 'react'
import axios from 'axios'
import UsersList from './components/Users.js'

class App extends React.Component{
    constructor(props){
        super(props)
        this.state={
            'tdusers':[]
        }
    }
    componentDidMount(){
        axios.get('http://127.0.0.1:8000/api/tduser/')
        .then(response => {
           const tdusers = response.data
               this.setState(
               {
                   'tdusers': tdusers
               }
           )
       }).catch(error => console.log(error))

    }

    render(){
        return(
        <div>
            <div>Menu</div>
            <UsersList tdusers={this.state.tdusers}/>
            <div>Footer</div>
        </div>

        )
        }
}


export default App;
