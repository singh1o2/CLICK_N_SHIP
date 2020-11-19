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

addToCart = document.querySelector('#addToCart');
$(addToCart).click(function(e)
{
  productName = document.querySelector('.product-title').textContent;
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
