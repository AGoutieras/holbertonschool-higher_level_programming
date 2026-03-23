const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  const my_list = document.querySelector('.my_list');
  my_list.appendChild(li);
});
