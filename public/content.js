chrome.runtime.onMessage.addListener((request) => {
  if (request.type === "takeAction") {
    const modal = document.createElement("dialog");
    modal.id = "myDivIdAct";
    modal.style.position = "fixed";
    modal.style.margin = "0px";
    modal.style.padding = "0px";
    modal.style.left = "0px";
    modal.style.transition = "bottom 1.2s";
    modal.style.zIndex = "2147483647";
    modal.style.width = "100%";
    modal.style.height = "16vh";
    modal.style.opacity = "0.9";
    modal.style.backgroundColor = "#83a9c9";
    modal.innerHTML = `<iframe id="takeAction"style="height:100%; width:100%"></iframe><link href="https://fonts.googleapis.com/css?family=Roboto:300&display=swap" rel="stylesheet"/>
    <div-z style="position:absolute; top:6vh; right:18px; ">  
        <h6-z id="unique" style="cursor:pointer; transition: color 0.3s; font-family: 'Roboto', sans-serif; font-size: 30px; padding:0px; margin:0px; color:#ffffff;" onmouseout="this.style.color='#ffffff'" onmouseover="this.style.color='#ff6464'">x</h6-z>
    </div-z>`;
    document.body.appendChild(modal);
    const dialog = document.querySelector("dialog");
    dialog.showModal();

    const iframe = document.getElementById("takeAction");
    //error
    iframe.src = chrome.extension.getURL("index.html");
    iframe.frameBorder = 0;

    modal.querySelector("h6-z").addEventListener("click", () => {
      modal.remove();
    });
  }
});

/*
<iframe id="actNow"style="height:100%; width:100%"></iframe><link href="https://fonts.googleapis.com/css?family=Roboto:300&display=swap" rel="stylesheet"/>
            <div-z style="position:absolute; top:6vh; right:18px; ">  
                <h6-z id="unique" style="cursor:pointer; transition: color 0.3s; font-family: 'Roboto', sans-serif; font-size: 30px; padding:0px; margin:0px; color:#ffffff;" onmouseout="this.style.color='#ffffff'" onmouseover="this.style.color='#ff6464'">x</h6-z>
            </div-z>

<iframe id="actNow" style="height:100%"></iframe>
<div style="position:absolute; top:0px; left:5px;">  
    <button>x</button>
</div>
*/
