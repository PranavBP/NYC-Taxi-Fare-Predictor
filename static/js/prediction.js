window.onload = function () {
    const hourDropDown = document.getElementById("hour");
    const dayDropDown = document.getElementById("day");
    const dateDropDown =  document.getElementById("date");
    const monthDropDown = document.getElementById("month")
    const rateCodeDropdown = document.getElementById("rate_code")
    const passengerDropdown = document.getElementById("passenger")
    const paymentTypeDropdown = document.getElementById("payment_type")
    let weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let months = ["Null", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    let rateCodes = ["Null","Standard Rate", "John F. Kennedy International Airport", "Newark", "Nassau or Westchester", "Negotiated fare", "Group ride"]
    let pTypes = ["Null", "Credit Card", "Cash", "No Charge", "Dispute"]

    for (let i = 0; i < 24; i++) {
        const el = document.createElement("option");
        let txt = ""
        if (i === 0) {
            txt = "12 Am to 12:59 Am";
        } else if (i < 12) {
            txt = String(i) + " Am to " + String(i) + ":59 Am";
        } else if (i === 12) {
            txt = "12 Pm to 12:59 Pm";
        } else {
            txt = String(i - 12) + " Pm to " + String(i - 12) + ":59 Pm";
        }
        el.textContent = txt;
        el.value = String(i);
        hourDropDown.appendChild(el);
    }

    for (let i = 0; i < weekdays.length; i++) {
        const opt = weekdays[i];
        const el = document.createElement("option");
        el.textContent = opt;
        el.value = String(i);
        dayDropDown.appendChild(el);
    }

    for (let i = 1; i < 32; i++) {
        const element = document.createElement("option");
        element.textContent = i;
        element.value = String(i);
        dateDropDown.appendChild(element);
    }

    for (let i = 1; i < months.length; i++) {
        const option = months[i];
        const element = document.createElement("option");
        element.textContent = option;
        element.value = String(i);
        monthDropDown.appendChild(element);
    }

    for (let i = 1; i < rateCodes.length; i++) {
        const option = rateCodes[i];
        const element = document.createElement("option");
        element.textContent = option;
        element.value = String(i);
        rateCodeDropdown.appendChild(element);
    }

    for (let i = 1; i < 7; i++) {
        const element = document.createElement("option");
        element.textContent = i;
        element.value = String(i);
        passengerDropdown.appendChild(element);
    }

    for (let i = 1; i < pTypes.length; i++) {
        const option = pTypes[i];
        const element = document.createElement("option");
        element.textContent = option;
        element.value = String(i);
        paymentTypeDropdown.appendChild(element);
    } 

};