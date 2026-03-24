document.addEventListener('DOMContentLoaded', function () {
  const translate = document.querySelector('#btn_translate');

  translate.addEventListener('click', function () {
    const langCode = document.querySelector('#language_code').value;
    fetch('https://hellosalut.stefanbohacek.com/?lang=' + langCode)
      .then(response => response.json())
      .then(data => {
        const hello = document.querySelector('#hello');
        hello.textContent = data.hello;
      });
  }
  );
});
