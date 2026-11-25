from pyscript import document, when

CLUB_MEMBERS = [
    "bong bong marcos",
    "ethan de leon",
    "spider man",
    "jose rizal",
    "ibbara",
]

@when("click", "#enter_btn")
def candidate_checker(event):
    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()
    candidate = f"{f_name} {l_name}".strip()

    is_member = candidate.lower() in CLUB_MEMBERS
    if is_member:
        document.getElementById("result").innerHTML = (
            f"Congratulations! {candidate}, you are now part of the club."
        )
    else:
        document.getElementById("result").innerHTML = (
            f"Sorry {candidate}, your name is not on the list."
        )
