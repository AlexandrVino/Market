window.onload = () => {
    let rateForm = document.getElementById('rate_form');
    let item_image = document.getElementById('item_image');
    let button = document.getElementById('set_rate')
    let close_button = document.getElementById('close_button')

    rateForm.hidden = true

    button.onclick = () => {
        rateForm.hidden = !rateForm.hidden;
        item_image.hidden = !rateForm.hidden;
    }

    close_button.onclick = () => {
        rateForm.hidden = true;
        item_image.hidden = false;
    }
}