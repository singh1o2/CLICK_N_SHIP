if(localStorage != null)
{
    var Products =JSON.parse(localStorage.ProductStoredTemp);
    Node = document.querySelector('.card-group');
    Price = 0;
    NoOfProducts =0;
    for(i = 0;i<Products.length;i++)
    {
      console.log(Products[i].ProductName);
      clone = Node.cloneNode(true);
      clone.querySelector('.card-title').textContent = Products[i].ProductName;
      clone.querySelector('.card-text').textContent = Products[i].ProductDescription;
      Price+=parseInt(Products[i].ProductDescription.substring(1)); //exclude dollar sign
      clone.querySelector('img').src = Products[i].ProductImage;
      document.body.appendChild(clone);
      clone.style.display = 'flex';
      NoOfProducts++;
      clone.querySelector('button').addEventListener('click',function()
      {
          this.parentElement.parentElement.style.display = 'none';
          Price-=parseInt(this.parentElement.querySelector('.card-text').textContent.substring(1));
          this.parentElement.querySelector('.card-text').textContent = '0';
          this.parentElement.querySelector('.card-title').textContent = '';
          NoOfProducts--;
          displayText(NoOfProducts); //if cart empty
          document.querySelector('#Amount .card-text').textContent = "TOTAL AMOUNT    :    "+Price;//update Price
      });
    }
    Node.style.display = 'none'
    document.querySelector('#Amount .card-text').textContent = "TOTAL AMOUNT    :    "+Price;
}
function displayText(NoOfProducts)
{
  if(NoOfProducts==0)
  {
     document.querySelector('h1').style.display = 'flex';
  }
}
