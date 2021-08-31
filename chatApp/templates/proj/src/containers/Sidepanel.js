import axios from "axios";
import React from "react";
import { Spin, Icon } from "antd";
import { connect } from "react-redux";
import * as actions from "../store/actions/auth";
import * as navActions from "../store/actions/nav";
import * as messageActions from "../store/actions/message";
import Contact from "../components/Contact";
import './../assets/style.css'
import groupUser from './../assets/groupUser.png'
import singleUser from './../assets/singleUser.png'
const antIcon = <Icon type="loading" style={{ fontSize: 24 }} spin />;

class Sidepanel extends React.Component {
  picFlag = ''
  
  state = {
    loginForm: true,
    chat: {},
    value: '',
    picFlag:''
    
  };
 
  getImage = () => {
    var username = localStorage.getItem('username')

    var token=localStorage.getItem('token')
    axios.defaults.headers = {
    "Content-Type": "application/json",
    Authorization: `Token ${token}`
    };
    axios
      .get(`http://127.0.0.1:8000/chat/profile/${username}/`)
      .then(res => res.data)
      .then(res => {
        if(res.length!==0)
          this.setState({ value: (res[0].photo_url) })
        else{this.setState({value:singleUser})}
      })
   
  }

  waitForAuthDetails() {
    const component = this;
    setTimeout(function () {
      if (
        component.props.token !== null &&
        component.props.token !== undefined
      ) {
        component.props.getUserChats(
          component.props.username,
          component.props.token
        );
        return;
      } else {
        console.log("waiting for authentication details...");
        component.waitForAuthDetails();
      }
    }, 100);
  }

  componentDidMount() {
    this.waitForAuthDetails();
  }

  
  openAddChatPopup() {
    this.props.addChat();
  }

  changeForm = () => {
    this.setState({ loginForm: !this.state.loginForm });
  };

  authenticate = e => {
    e.preventDefault();
    if (this.state.loginForm) {
      this.props.login(e.target.username.value, e.target.password.value);
    } else {
      this.props.signup(
        e.target.username.value,
        e.target.email.value,
        e.target.password.value,
        e.target.password2.value
      );
    }
  };

  getUsername = () => {
    var getUser = localStorage.getItem('username')
    
    if (getUser !== undefined && getUser !== null) {
      var name = getUser.charAt(0).toUpperCase() + getUser.slice(1)
      return name
    }

  }

 
  render() {
    let activeChats = this.props.chats.map(c => {
      
      return (
          
          <Contact
            key={c.id}
            id={c.id}
            name={c.participants}
            status="busy"
            chatURL={`${c.memebers_name}`}
            />          
      );
    } );
    return (
      <div id="sidepanel">
        <div id="profile"  >
          <div className="wrap" >
            
            {
              localStorage.getItem('username') === null ?
                <p style={{ fontSize: '18px' }}>Enter Login info here</p> :
                <div>
                  
                <img
                  id="profile-img"
                  src={this.state.value}
                  className="online"
                  alt=""    
                  />
                {this.getImage()}
                </div>

            }
            
            <p style={{fontSize:'25px'}}>{this.getUsername()}</p>
            <i
              className="fa fa-chevron-down expand-button"
              aria-hidden="true"
            />
            <div id="status-options">
              <ul>
                <li id="status-online" className="active">
                  <span className="status-circle" /> <p>Online</p>
                </li>
                <li id="status-away">
                  <span className="status-circle" /> <p>Away</p>
                </li>
                <li id="status-busy">
                  <span className="status-circle" /> <p>Busy</p>
                </li>
                <li id="status-offline">
                  <span className="status-circle" /> <p>Offline</p>
                </li>
              </ul>
            </div>
            <div id="expanded">
              {this.props.loading ? (
                <Spin indicator={antIcon} />
              ) : this.props.isAuthenticated ? (
                  <button onClick={() => {
                      window.location.replace('/')
                    this.props.logout()
                  }} className="btnTry">
                  <span className='btnTry'>Logout</span>
                </button>
              ) : (
                <div style={{fontSize:'15px'}}>
                  <form method="POST" onSubmit={this.authenticate}>
                    {this.state.loginForm ? (
                      <div>
                        <input
                          name="username"
                          type="text"
                          placeholder="username"
                        />
                        <input
                          name="password"
                          type="password"
                          placeholder="password"
                        />
                      </div>
                    ) : (
                      <div>
                        <input
                          name="username"
                          type="text"
                          placeholder="username"
                        />
                        <input name="email" type="email" placeholder="email" />
                        <input
                          name="password"
                          type="password"
                          placeholder="password"
                        />
                        <input
                          name="password2"
                          type="password"
                          placeholder="password confirm"
                        />
                      </div>
                    )}

                        <button type="submit"  >Authenticate</button>
                  </form>

                </div>
                  )}
              
              {this.props.error!==null?<p style={{fontSize:'15px'}}>Wrong Username or Password..!</p>:<p></p>}
              <hr style={{marginTop:'90px',marginRight:'20px'}}/>
            </div>
            <div  style={{marginBottom:'200px'}} id="contacts">
            <ul >{activeChats}</ul>

       
              </div>
          </div>
        </div>
        
        
        {
          localStorage.getItem('username') === null ? <p></p> :
            <div >
              {/* <div  id="contacts">
                 <ul >{activeChats}</ul>
              </div> */}
            <div id="bottom-bar" style={{marginTop:'200px'}} >
              <button id="addChat" style={{width:'100%',fontSize:'15px'}} onClick={() => this.openAddChatPopup()}>
                <i className="fa fa-user-plus fa-fw" aria-hidden="true" />
                <span>Create chat</span>
              </button>
              
              </div>
              </div>
        }
        
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isAuthenticated: state.auth.token !== null,
    loading: state.auth.loading,
    token: state.auth.token,
    username: state.auth.username,
    chats: state.message.chats,
    error:state.auth.error
  };
};

const mapDispatchToProps = dispatch => {
  return {
    login: (userName, password) =>
      // dispatch(actions.authLogin(localStorage.getItem('name'), localStorage.getItem('password'))),
      dispatch(actions.authLogin(userName, password)),
    logout: () => dispatch(actions.logout()),
    signup: (username, email, password1, password2) =>
      dispatch(actions.authSignup(username, email, password1, password2)),
    addChat: () => dispatch(navActions.openAddChatPopup()),
    getUserChats: (username, token) =>
      dispatch(messageActions.getUserChats(username, token))
  };
};

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Sidepanel);
