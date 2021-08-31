import { NavLink } from "react-router-dom";
import axios from "axios";
import React, { Component } from 'react'
import './../assets/style.css'
import groupUser from './../assets/groupUser.png'
import singleUser from './../assets/singleUser.png'
import 'font-awesome/css/font-awesome.min.css';
export class Contact extends Component {

  state = {
    
    chat: [],
    id:null,
    imgUrl: '',
    picFlag:''
    
    
  }   
  picFlag=''
  getImageURL = (name) => {
    try {
      var token=localStorage.getItem('token')
      axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
      };
      axios
        .get(`http://127.0.0.1:8000/chat/profile/${name}/`)
        .then(res => res.data)
        .then(res => {
          if (res.length !== 0)
            this.picFlag = res[0].photo_url
          else{this.picFlag='false'}
        })
        .catch(
            
          )  
      
      // let url = ''
      // var token=localStorage.getItem('token')
      // var token = 'Token ' + localStorage.getItem('token');
      // var value = fetch(`http://localhost:8000/chat/profile/${name}`)
      //   .then(res => res.json())
  
      //   .then(res => {
      //     if (res.length !== 0)
      //       this.picFlag = res[0].photo_url
      //     else{this.picFlag='false'}
      //   }
      // ).catch(
            
      // )  
    }
    catch{this.picFlag=singleUser}
    return this.picFlag
    
  }


  replaceAll=(string, search, replace)=> {
    return string.split(search).join(replace);
  }


  getImageDetail = () => {
    var username = localStorage.getItem('username')
    var tempName = this.props.chatURL
    var itemNO = this.props.chatURL.split('_').length
    tempName = this.replaceAll(tempName, '_', ' ')
    
    var Name = this.props.name
    var len = Name.length
    var url=''
    Name=Name.join(' ')
    Name = Name.replace(username, '')
    Name = this.replaceAll(Name, ' ', '')

    if (len === 1)
    {
      if (itemNO > 2)
      {
        return groupUser
      }
      return singleUser
    }
    
    if (itemNO > 2)
    {
      return groupUser
    }

    try {
      if (len <= 2 & username !== null & username !== undefined) {
        url = this.getImageURL(Name)
        localStorage.setItem(Name,url)      
      }


      if (url === undefined || url==='false'|| url ===null ) 
        {return singleUser}
    }
    catch{
      url=singleUser
    }
   
    return url

  }
 
  getName = () => {
    var username = localStorage.getItem('username')
    var tempName = this.props.chatURL
    var itemNO = this.props.chatURL.split('_').length
    tempName = this.replaceAll(tempName,'_',' ')
    if (username !== undefined && username !== null && username !== '')
      var tempUsername = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
    
    tempName = tempName.replace(tempUsername, '')
    if (tempName.length >= 10)
    {
      tempName = tempName.slice(0, 12)+'...'
      
      }
    if (itemNO > 2)
    {
      tempName += '[Group]'
      
    }
    
    // var username = localStorage.getItem('username')
    // var Name = this.props.name
    // var len = Name.length
    // Name = Name.map(item=> item.charAt(0).toUpperCase() + item.substr(1).toLowerCase())
    // var temp = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
    // Name = Name.join(' ')
    // Name = Name.replace(temp,'')
    
    // if (len > 2)
    // {
    //   Name+=' [Group]'
    // }
   
    return tempName
  }

  //http://127.0.0.1:8000/chat/chat/40/

  deleteChatRequest = (chatId) => {

      var token=localStorage.getItem('token')
      axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
      };
      axios
        .delete(`http://127.0.0.1:8000/chat/chat/${chatId}/`)
        .then(res => {
          window.location.replace('alumani')
          alert('chat has been removed')
        }).catch(console.log('Delettin failed'));
      window.location.replace('alumani')
    };
  
  deleteChat = (e) => {
    var Name = this.props.name
    var len = Name.length
    var chatId = this.props.id
    this.deleteChatRequest(chatId)

  }


  render() {
    return (
      <div className='wrapTry' style={{fontSize:'15px'}}>
        
      <NavLink  to={`/${this.props.chatURL}`} style={{ color: "#fff" }}>      
      <li   >
        {localStorage.getItem('token') !== null ?
              <div > 
            <img style={{
                      width: '50px',
                      borderRadius: "50%",
                      float: 'left',
                      marginRight: '0px'
                }}
                  src={this.getImageDetail()}
                />
                
                <div className="meta">
                  <p className="name" >   
                    {this.getName()}      
                  </p>
                </div>
               
                <button className='deleteBtn' onClick={this.deleteChat}> <i className="fas fa-trash-alt "></i></button>
            
        </div>
          :
    <p></p> 
        } 
</li>
        </NavLink>
        <br/>
</div>
    )
  }
}


export default Contact;
