document.addEventListener('DOMContentLoaded', function () {
  const addItem = document.querySelector('#add_item');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', function () {
    const li = document.createElement('li');
    li.textContent = 'Item';
    myList.appendChild(li);
  });

  const removeItem = document.querySelector('#remove_item');

  removeItem.addEventListener('click', function () {
    myList.removeChild(myList.lastElementChild);
  });

  const clearList = document.querySelector('#clear_list');

  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
