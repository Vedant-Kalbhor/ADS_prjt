
document.addEventListener('DOMContentLoaded', function() {
    let next = document.querySelector('.next');
    let prev = document.querySelector('.prev');
    
    if (next && prev) {
        next.addEventListener('click', function() {
            let items = document.querySelectorAll('.item');
            document.querySelector('.slide').appendChild(items[0]);
        });

        prev.addEventListener('click', function() {
            let items = document.querySelectorAll('.item');
            document.querySelector('.slide').prepend(items[items.length - 1]);
        });
    } else {
        console.error('Next or previous buttons not found in the DOM');
    }
});
