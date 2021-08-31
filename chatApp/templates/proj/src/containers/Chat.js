import React from "react";
import { connect } from "react-redux";
import WebSocketInstance from "../websocket";
import Hoc from "../hoc/hoc";
import Profile from "./Profile";
import groupUser from './../assets/groupUser.png'
import singleUser from './../assets/singleUser.png'
import axios from "axios";

class Chat extends React.Component {
  state = {
    message: "",
    value:''
  };

  initialiseChat() {
    this.waitForSocketConnection(() => {
      // WebSocketInstance.addCallbacks(
      //   this.props.setMessages.bind(this),
      //   this.props.addMessage.bind(this)
      // );
      WebSocketInstance.fetchMessages(
        this.props.username,
        this.props.match.params.chatID
      );
    });
    WebSocketInstance.connect(this.props.match.params.chatID);
  }

  constructor(props) {
    super(props);
    this.initialiseChat();
  }

  waitForSocketConnection(callback) {
    const component = this;
    setTimeout(function() {
      if (WebSocketInstance.state() === 1) {
        console.log("Connection is made");
        callback();
        return;
      } else {
        console.log("wait for connection...");
        component.waitForSocketConnection(callback);
      }
    }, 100);
  }

  messageChangeHandler = event => {
    this.setState({ message: event.target.value});
  };

  sendMessageHandler = e => {
    e.preventDefault();
    const messageObject = {
      from: this.props.username,
      content: this.state.message,
      chatId: this.props.match.params.chatID
    };
    WebSocketInstance.newChatMessage(messageObject);
    this.setState({ message: "" });
  };

  renderTimestamp = timestamp => {
    let prefix = "";
    const timeDiff = Math.round(
      (new Date().getTime() - new Date(timestamp).getTime()) / 60000
    );
    if (timeDiff < 1) {
      // less than one minute ago
      prefix = "just now...";
    } else if (timeDiff < 60 && timeDiff > 1) {
      // less than sixty minutes ago
      prefix = `${timeDiff} minutes ago`;
    } else if (timeDiff < 24 * 60 && timeDiff > 60) {
      // less than 24 hours ago
      prefix = `${Math.round(timeDiff / 60)} hours ago`;
    } else if (timeDiff < 31 * 24 * 60 && timeDiff > 24 * 60) {
      // less than 7 days ago
      prefix = `${Math.round(timeDiff / (60 * 24))} days ago`;
    } else {

    }
    return prefix;
  };

  getUserName = (name) => {
    var index = name.lastIndexOf('@')
    name = name.substr(0, index) + '    @' + name.substr(index + 1);
  
    return name
  }
  renderMessages = messages => {
    const currentUser = this.props.username;
    return messages.map((message, i, arr) => (
      <li
        key={message.id}
        style={{ marginBottom: arr.length - 1 === i ? "300px" : "15px" }}
        className={message.author === currentUser ? "sent" : "replies"}
      >
        <p>
        {this.getUserName(message.content)}
          <br />
          <small>{this.renderTimestamp(message.timestamp)}</small>
        </p>
      </li>
    ));
  };

  scrollToBottom = () => {
    this.messagesEnd.scrollIntoView({ behavior: "smooth" });
  };

  componentDidMount() {
    this.scrollToBottom();
  }

  componentDidUpdate() {
    this.scrollToBottom();
  }

  componentWillReceiveProps(newProps) {
    if (this.props.match.params.chatID !== newProps.match.params.chatID) {
      WebSocketInstance.disconnect();
      this.waitForSocketConnection(() => {
        WebSocketInstance.fetchMessages(
          this.props.username,
          newProps.match.params.chatID
        );
      }); 
      WebSocketInstance.connect(newProps.match.params.chatID);
    }
  }

  replaceAll=(string, search, replace)=> {
    return string.split(search).join(replace);
  }

  getImageURL = (name) => {
    var url=''
    var token = localStorage.getItem('token')
    axios.defaults.headers = {
      "Content-Type": "application/json",
      Authorization: `Token ${token}`
    };
    axios
      .get(`http://127.0.0.1:8000/chat/profile/${name}`)
      .then(res => res.data)
      .then(res => {

        this.setState({value:res[0].photo_url})
        // url = res[0].photo_url
      })
      .catch() 
 
      return this.state.value
    
  }



  getImage = () =>
  {   
    var itemNO = this.props.match.params.chatID.split('_').length
    var name = this.props.match.params.chatID
    name = this.replaceAll(name, '_', ' ')
    var username = localStorage.getItem('username')
    if (username !== null & username !== undefined)
    {
      username = localStorage.getItem('username').charAt(0).toUpperCase() + username.slice(1)  
    }
    if (itemNO <= 2)
    {
      name = name.replace(username, '')
      name = this.replaceAll(name,' ', '')
      name = name.toLowerCase()
      name=this.getImageURL(name) 
    }
    else {
      name=groupUser
    }
    if (name === undefined)
    {
      name = singleUser  
    }
    
    return name
  }



  render() {
    const messages = this.state.messages;
    return (

      <Hoc>
        <Profile id={this.props.match.params.chatID} />
         {/* {console.log(this.message)} */}
        <div className="messages">
          <ul id="chat-log">
            {this.props.messages && this.renderMessages(this.props.messages)}
            <div
              style={{ float: "left", clear: "both" }}
              ref={el => {
                this.messagesEnd = el;
              }}
            />
          </ul>
        </div>
        <div className="message-input">
          <form onSubmit={this.sendMessageHandler}>
            <div className="wrap">
              <input
                onChange={this.messageChangeHandler}
                value={this.state.message}
                required
                id="chat-message-input"
                type="text"
                placeholder="Write your message..."
              />
               {/* <i className="fa fa-paperclip attachment" aria-hidden="true" /> */}
              <button style={{width:'90px',paddingTop:'20px'}} id="chat-message-submit" className="submit">
                <i className="fa fa-paper-plane" aria-hidden="true" />
              </button>
            </div>
          </form>
        </div>
      </Hoc>
    );
  }
}

const mapStateToProps = state => {
  return {
    username: state.auth.username,
    messages: state.message.messages,

  };
};

export default connect(mapStateToProps)(Chat);
