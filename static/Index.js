/*Products = document.querySelectorAll('.card');
class Product{
  PID;
  ProductName;
  ProductDescription;
  setI(i)
  {
    this.PID=i;
  }
}

ActualProducts = [] ;
localStorageProducts = [] ;
index =0;
for(i=0;i<Products.length;i++)
{
    ActualProducts[i] =new Product();
    ActualProducts[i].setI(Products[i].querySelector('.id').textContent);
    Button = Products[i].querySelector('button');
    ActualProducts[i].ProductName = Products[i].querySelector('.card-title').textContent;
    ActualProducts[i].ProductDescription =  Products[i].querySelector('.card-text').textContent;
    ActualProducts[i].ProductImage = Products[i].querySelector('img').src;
    Button.addEventListener('click',function()
    {
        localStorageProducts[index] = new Product();
        x = parseInt(this.parentElement.querySelector('.id').textContent)-1;//retrieve product id from DOM
        localStorageProducts[index]=ActualProducts[x];
        localStorage.ProductStoredTemp = JSON.stringify(localStorageProducts);
        index++;
    });
}
**/

//

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
$("body").bind("ajaxSend", function(elm, xhr, s){
   if (s.type == "POST") {
      xhr.setRequestHeader('X-CSRF-Token', csrf_token);
   }
})

Products = document.querySelectorAll('.card');
for(i=0;i<Products.length;i++)
{
    Button = Products[i].querySelector('button');
    $(Button).click(function(e)
    {
      productName = this.parentElement.querySelector('.card-title').textContent;
      console.log(productName);
      e.preventDefault();
      $.ajax({
        headers: { "X-CSRFToken": csrf_token },
        type:'POST',
        csrfmiddlewaretoken: '{{ csrf_token }}',
        url:'../addToCart/',
        data: JSON.stringify(productName),
        datatype:'json'
      });
    });
}
