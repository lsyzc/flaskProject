 window.onload = function() {
     var imgCenter = document.getElementById("imgCenter")
     var img1 = document.getElementById("img1")
     var img2 = document.getElementById("img2")
     var img3 = document.getElementById("img3")
     var img4 = document.getElementById("img4")



     img1.onclick = function() {
         //  console.log(this.src);
         imgCenter.style.backgroundImage = 'url(' + this.src + ')';
     }

     img2.onclick = function() {
         //  console.log(this.src);
         imgCenter.style.backgroundImage = 'url(' + this.src + ')';
     }
     img3.onclick = function() {
         //  console.log(this.src);
         imgCenter.style.backgroundImage = 'url(' + this.src + ')';
     }
     img4.onclick = function() {
         //  console.log(this.src);
         imgCenter.style.backgroundImage = 'url(' + this.src + ')';
     }




 }