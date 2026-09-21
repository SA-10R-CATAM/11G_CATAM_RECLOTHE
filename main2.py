
from pyscript import window, document


def check_agreement(event):
    checkbox = document.getElementById("agreeCheckbox")
    accept_button = document.getElementById("acceptButton")

    if checkbox.checked:
        accept_button.disabled = False
    else:
        accept_button.disabled = True


def accept_terms(event):

    checkbox = document.getElementById("agreeCheckbox")

    if checkbox.checked:

        window.location.href = "terms_condition.html"

