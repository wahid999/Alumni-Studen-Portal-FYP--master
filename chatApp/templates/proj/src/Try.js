import React, { Component } from 'react'
import { createStore} from "redux";




  


export class Try extends Component {

    reducer = (state = {}, action) => {
        
        if (action.type === 'IMAGE')
        {
            state=action.data
            return state
        }
        
        return state
    }
    componentWillMount = () => {
     
        var store = createStore(this.reducer)
        this.getImage(store)

    }
  getImage = (store) => {
    var username = localStorage.getItem('username')
    var url=''
    fetch(`http://localhost:8000/chat/profile/${username}`)
      .then(res => res.json())
      .then(res => url=(res[0].photo_url))
    store.dispatch({type:'IMAGE',data:url})
    console.log(store.getState())
  }

    render() {
        return (
            <div>
                
            </div>
        )
    }
}

export default Try