import React from "react";
import ReactDOM from "react-dom";
import { createStore, compose, applyMiddleware, combineReducers } from "redux";
import { Provider } from "react-redux";
import thunk from "redux-thunk";
import "antd/dist/antd.css";
import authReducer from "./store/reducers/auth";
import navReducer from "./store/reducers/nav";
import messageReducer from "./store/reducers/message";
import App from "./App";
import './assets/style.css'
import '@fortawesome/fontawesome-free/css/all.min.css';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

function configureStore() {
  const rootReducer = combineReducers({
    auth: authReducer,
    nav: navReducer,
    message: messageReducer
  });

  const store = createStore(
    rootReducer,
    composeEnhancers(applyMiddleware(thunk))
  );


  return store;
}

const store = configureStore();

const app = (
  <Provider store={store}>
    <App />
  </Provider>
);


ReactDOM.render(app, document.getElementById("root"));
