buttons = document.querySelectorAll('.dropbtn');

for (var i = 0; i <buttons.length; i++) {
      console.log(buttons);
      buttons[i].addEventListener('click',function()
      {
         card = this.nextSibling.nextSibling;
         if( card.style.display == 'flex')
         {
            console.log(card);
            card.style.display = 'none';
         }
        else
        {
            console.log(card.style.display);
            card.style.display = 'flex';
        }
         document.querySelector('body').style.height = '100%';
      });
}
