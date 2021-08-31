import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import Hoc from "../hoc/hoc";
import { createStore } from 'redux'
import './../assets/style.css'
import * as messageActions from "./../store/actions/message";
import groupUser from './../assets/groupUser.png'
import singleUser from './../assets/singleUser.png'
import axios from "axios";

class Profile extends React.Component {
  picFlag=''
  replaceAll=(string, search, replace)=> {
    return string.split(search).join(replace);
  }


    
  state = {
    loc: '',
    value: '',
    picFlag:''
  }

  getUserName = () => {

    var itemNO = this.props.id.split('_').length
    var name = this.props.id
    name = this.replaceAll(name,'_',' ')
    var username = localStorage.getItem('username')
    if (username !== null & username !== undefined)
    {
      username = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
    }
    
      name = name.replace(username, '')
      var temp = this.replaceAll(name, ' ', '')
    
      if (itemNO > 2)
      {
        name += ' [Group]'
        name='~You '+name
    }
     
      return name
  }
 

  getImage = () =>
  {   
    var url=''
    var itemNO = this.props.id.split('_').length
    if (itemNO > 2) {
      return groupUser
    }

    var name = this.props.id
    name = this.replaceAll(name, '_', ' ')
    var username = localStorage.getItem('username')
    if (username !== null & username !== undefined)
    {
      username = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
    }
    name = name.replace(username, '')
    name = this.replaceAll(name,' ', '')
    name = name.toLowerCase()
    url = localStorage.getItem(name)
    
    if (url === undefined || url==='false'||url ===null )
    {
      
      return singleUser  
    }
    console.log(url)
    return url
  }



  render() {
    if (this.props.token === null) {
      return <Redirect to="/" />;
    }

    return (
      <div className="contact-profile" >
        
        {this.props.username !== null ? (
          <Hoc>
            
            <img
              style={{marginLeft:'20px'}} 
              src={this.getImage()}
            />
            {this.state.loc}
              <p>{this.getUserName()}</p>
  
          </Hoc>
        ) : null}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    token: state.auth.token,
    username: state.auth.username,
    chats: state.message.chats,
    
  };
};

const mapDispatchToProps = dispatch => {
  return {
    getUserChats: (username, token) =>
      dispatch(messageActions.getUserChats(username, token)),
    getChats: () => {
      
      // return window.location.pathname
    }
    
  };
};


export default connect(mapStateToProps)(Profile);
