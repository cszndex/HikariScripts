document.addEventListener('DOMContentLoaded', function () {
  const textContainer = document.getElementById('textContainer');
  const icon = document.getElementById('navbar-icon');
  const texts = textContainer.getElementsByClassName('text');
  const pasteButton = document.getElementById("pasteButton")
  const inputFluxus = document.getElementById("fluxus_url")
  const tryExample = document.getElementById("tryExample")
  const copyScript = document.getElementById("copyScript")
  let index = 2;
  let isX = false;
  
  function switchText() {
    const currentText = texts[index];
    const nextIndex = (index + 1) % texts.length;
    const nextText = texts[nextIndex];

    currentText.style.opacity = 0;
    nextText.style.opacity = 1;

    index = nextIndex;
  }
  switchText();
  
  setInterval(switchText, 3000);
  
  tryExample.addEventListener("click", function() {
    inputFluxus.value = "https://fluxteam.net/android/checkpoint/start.php?HWID=d565bbeb55bf3b3761926ba962826ef4905cc06b6bd698eccce37ab0980523bd8308121031bf0729081485b4ffee7d19"
    var instance = mdtoast('Click "Generate Fluxus Key" Button to proceed.', {
        interaction: true,
        duration: 5,
        actionText: 'CLOSE',
        action: function(){
          this.hide(); 
        },
        init: true
    });
    instance.show();
  });
  
  pasteButton.addEventListener("click", function() {
    navigator.clipboard.readText().then(
      cliptext => (inputFluxus.value = cliptext),
      err => console.log(err)
    );
  });
  
  copyScript.addEventListener("click", function() {
    navigator.clipboard.writeText("loadstring(game:HttpGet('http://hikari-eosin.vercel.app/hikari'))()");
    var instance = mdtoast('Script copied to clipboard.', {
        interaction: true,
        duration: 5,
        actionText: 'CLOSE',
        action: function(){
          this.hide(); 
        },
        init: true
    });
    instance.show();
  });
  
  icon.addEventListener('click', () => {
    icon.style.transform = 'scale(0)';
    setTimeout(() => {
      if (isX) {
        icon.classList.remove('bx-x');
        icon.classList.add('bx-menu');
      } else {
        icon.classList.remove('bx-menu');
        icon.classList.add('bx-x');
      }
      setTimeout(() => {
        icon.style.transform = 'scale(1)';
      }, 0);
      isX = !isX;
    }, 180);
  });
  
});