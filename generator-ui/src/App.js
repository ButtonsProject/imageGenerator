import React from "react";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import {Header} from "./components/Header";
import {PostForm} from "./components/PostForm";
import {ResultForm} from "./components/ResultForm";


const App = () => {
    return (
        <>
            <Header/>
            <Router>
                <Switch>
                    <Route exact path="/" component={PostForm}/>
                    <Route path="/result" component={ResultForm}/>
                </Switch>
            </Router>
        </>
    )
}

export default App;