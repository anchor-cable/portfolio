const dassimen = document.getElementById('dassimen');
const dassimen_low = document.getElementById('modal-overlay');

//ON
dassimen.addEventListener('mouseenter', () => {
    　　dassimen_low.style.visibility = 'visible';
    }, false);
    
//OUT
dassimen.addEventListener('mouseleave', () => {
    　　dassimen_low.style.visibility = 'hidden';
}, false);