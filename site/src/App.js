import React, { Component } from 'react';
// import logo from './logo.svg';
import './App.css';
import axios from 'axios'

// 拦截request,设置全局请求为ajax请求
axios.interceptors.request.use((config) => {
  config.headers['X-Requested-With'] = 'XMLHttpRequest';
  let regex = /.*csrftoken=([^;.]*).*$/; // 用于从cookie中匹配 csrftoken值
  config.headers['X-CSRFToken'] = document.cookie.match(regex) === null ? null : document.cookie.match(regex)[1];
  return config
});

axios.defaults.withCredentials=true;
axios.defaults.headers.post['Content-Type']='application/json';
// const server = 'http://127.0.01:8080';//这个要写在etc/settings里

//https://blog.csdn.net/div_ma/article/details/80436727  react-router-dom
class App extends Component {
  constructor(props){
    super(props);
    this.state={
      name:"",
      age:0
    }

    this.change=this.change.bind(this);
    this.write=this.write.bind(this);
    this.read=this.read.bind(this);
  }

  change(key,e){
    this.setState(
        {
            [key]:e.target.value
        }
    );
  }

  async write(){
    let data={...this.state};
    console.log(data);
    // let res=await axios.post(`${server}/write/`,data);
    let res=await axios.post(`/person/`,data);
    // let res=await axios.post(`/person`,data);

    console.log(res);
  }

  async read(){
    // let params={
    //   name:'a'
    // }
    // let res=await axios.get(`${server}/read/`,{params});
    // let res=await axios.get(`${server}/person`);
    let res=await axios.get(`/person/`);

    console.log(res);
  }

  render() {
    return (
      <div className="App">
        <input onChange={(e)=>(this.change('name',e))}/>
        <br />
        <input onChange={(e)=>(this.change('age',e))} />
        <br />
        <button onClick={this.write}>write</button>
        <button onClick={this.read}>read</button>
      </div>
    );
  }
}

export default App;
