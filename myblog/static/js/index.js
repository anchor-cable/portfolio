const dassimen = document.getElementById('dassimen');
const dassimen_low = document.getElementById('modal-overlay');

//ON
dassimen.addEventListener('mouseover', () => {
    　　dassimen_low.style.display = 'flex';
    }, false);
    
//OUT
dassimen.addEventListener('mouseleave', () => {
    　　dassimen_low.style.display = 'none';
}, false);