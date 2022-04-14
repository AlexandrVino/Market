window.onload = () => {
    let rateForm = document.getElementById('rate_form');
    let item_info = document.getElementById('item_info');
    let button = document.getElementById('set_rate')
    let close_button = document.getElementById('close_button')

    rateForm.hidden = true

    button.onclick = () => {
        rateForm.hidden = !rateForm.hidden;
        item_info.hidden = !rateForm.hidden;
    }

    close_button.onclick = () => {
        rateForm.hidden = true;
        item_info.hidden = false;
    }
}