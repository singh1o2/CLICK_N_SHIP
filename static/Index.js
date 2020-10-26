Products = document.querySelectorAll('.card');
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
