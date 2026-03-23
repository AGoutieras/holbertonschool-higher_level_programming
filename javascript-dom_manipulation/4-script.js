const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  const myList = document.querySelector('.my_list');
  myList.appendChild(li);
});
