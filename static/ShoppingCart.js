/*if(localStorage != null)
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
}*/


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrf_token = getCookie('csrftoken');


Products = document.querySelectorAll('.card');
Price =0;
for(i=0;i<Products.length;i++)
{
    Button = Products[i].querySelector('button');
    productDescription= Products[i].querySelector('.card-text').textContent;
    Price+=parseInt(productDescription);
    console.log(Price);
    Button.addEventListener('click',function()
    {
      this.parentElement.parentElement.style.display = 'none';
      Price-=parseInt(this.parentElement.querySelector('.card-text').textContent);
      document.querySelector('#Amount .card-text').textContent = "TOTAL AMOUNT    :    "+Price;
      $.ajax({
        headers: { "X-CSRFToken": csrf_token },
        type:'POST',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url:'../deletefromCart/',
        data: JSON.stringify(this.parentElement.querySelector('.card-title').textContent),
        datatype:'json'
      });
    });
  }
document.querySelector('#Amount .card-text').textContent = "TOTAL AMOUNT    :    "+Price;
