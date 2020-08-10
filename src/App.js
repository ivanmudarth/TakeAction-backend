import "./App.css";
import React, { Component } from "react";
import "./App.css";
import icon from "./takeAction.png";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      organization: "Learn More About Mental Health",
      message:
        "Irresponsible reporting detected: the way suicide is portrayed by the media can have harmful effects on those suffering with mental health issues. Mental health should not be treated as less important than physical health. Learn about the misunderstood aspects of mental illness that are often exacerbated by the internet.",
      link: "https://www.camh.ca/en/health-info/mental-health-101",
      takeActionLink: "https://ymhc.ngo/donate/",
    };
  }
  componentDidMount() {
    /*
    console.log("hello");
    var searchUrl = "";

    // eslint-disable no-undef 
    chrome.tabs.getSelected(null, function (tab) {
      myFunction(tab.url);
    });

    function myFunction(tablink) {
      console.log("inside myFunction");
      searchUrl =
        "http://6f521fbf2526.ngrok.io/api/recommendation?url=" + tablink;
    }

    console.log("outside " + searchUrl);

    fetch(searchUrl)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        this.setState({ link });
      });
      */
  }

  render() {
    return (
      <div className="modalBody">
        <div className="row">
          <div className="left">
            <a href={this.state.takeActionLink} target="_blank">
              <img className="icon" src={icon} />
            </a>
          </div>
          ;
          <div className="right">
            <p className="titleText">
              <b>Take Action -&nbsp;</b>
              <a className="titleLink" href={this.state.link} target="_blank">
                {this.state.organization}
              </a>
            </p>
            <p className="genText">
              <b>Irresponsible reporting detected:</b> the way suicide is
              portrayed by the media can have harmful effects on those suffering
              with mental health issues. Mental health should not be treated as
              less important than physical health. Learn about the misunderstood
              aspects of mental illness that are often exacerbated by the
              internet.
            </p>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
