// script.js

function goToIndex() {
    window.location.href = "/";
}

function goToClientForm() {
    window.location.href = "/client_form";
}
// script.js

// Attach the saveClientData function to the "Save" button click event
document.addEventListener("DOMContentLoaded", function() {
    var saveButton = document.querySelector(".save-button");
    saveButton.addEventListener("click", saveClientData);
});


function clearForm() {
    var inputElements = document.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], textarea, select, input[type="checkbox"], input[type="radio"]');

    for (var i = 0; i < inputElements.length; i++) {
        var elementType = inputElements[i].type;

        if (elementType === 'checkbox' || elementType === 'radio') {
            inputElements[i].checked = false;
        } else {
            inputElements[i].value = '';
        }
    }
}

/*
function saveClientData(event) {
    event.preventDefault(); // Prevent the default form submission

    console.log("client_name:", document.getElementById("client_name").value);
    console.log("address:", document.getElementById("address").value);
    console.log("customer_type", document.getElementById("customer_type").value);
    console.log("purchase_contact", document.getElementById("purchase_contact").value);
    console.log("purchase_email", document.getElementById("purchase_email").value);
    console.log("purchase_mobile", document.getElementById("purchase_mobile").value);
    console.log("project_head", document.getElementById("project_head").value);
    console.log("project_email", document.getElementById("project_email").value);
    console.log("project_mobile", document.getElementById("project_mobile").value);
    console.log("design_contact", document.getElementById("design_contact").value);
    console.log("design_email", document.getElementById("design_email").value);
    console.log("design_mobile", document.getElementById("design_mobile").value);
    console.log("quality_contact", document.getElementById("quality_contact").value);
    console.log("account_contact", document.getElementById("account_contact").value);
    console.log("account_email", document.getElementById("account_email").value);
    console.log("account_mobile", document.getElementById("account_mobile").value);
    //console.log("customer_rating", document.getElementById("customer_rating").value);
    console.log("discount_details", document.getElementById("discount_details").value);
    console.log("overhead_details", document.getElementById("overhead_details").value);
    console.log("priority_details", document.getElementById("priority_details").value);
    console.log("total_offer_sent", document.getElementById("total_offer_sent").value);
    console.log("total_po_recovered", document.getElementById("total_po_recovered").value);
    console.log("total_business", document.getElementById("total_business").value);

}*/

function saveClientData(event) {
    event.preventDefault();
    var formData = {
        "client_name": document.getElementById("client_name").value,
        "address": document.getElementById("address").value,
        "customer_type": document.getElementById("customer_type").value,
        "purchase_contact": document.getElementById("purchase_contact").value,
        "purchase_email": document.getElementById("purchase_email").value,
        "purchase_mobile": document.getElementById("purchase_mobile").value,
        "project_head": document.getElementById("project_head").value,
        "project_email": document.getElementById("project_email").value,
        "project_mobile": document.getElementById("project_mobile").value,
        "design_contact": document.getElementById("design_contact").value,
        "design_email": document.getElementById("design_email").value,
        "design_mobile": document.getElementById("design_mobile").value,
        "quality_contact": document.getElementById("quality_contact").value,
        "quality_email": document.getElementById("quality_email").value,
        "quality_mobile": document.getElementById("quality_mobile").value,
        "account_contact": document.getElementById("account_contact").value,
        "account_email": document.getElementById("account_email").value,
        "account_mobile": document.getElementById("account_mobile").value,
        //"customer_rating": document.getElementById("customer_rating").value,
        "discount_details": document.getElementById("discount_details").value,
        "overhead_details": document.getElementById("overhead_details").value,
        "priority_details": document.getElementById("priority_details").value,
        "total_offer_sent": document.getElementById("total_offer_sent").value,
        "total_po_recovered": document.getElementById("total_po_recovered").value,
        "total_business": document.getElementById("total_business").value


        // ... Repeat this pattern for all form fields
    };

    // Collect the selected customer rating
   // var customerRatingRadios = document.getElementsByName("customer_rating");
    //var selectedCustomerRating = null;

    //for (var i = 0; i < customerRatingRadios.length; i++) {
     //if (customerRatingRadios[i].checked) {
       //     selectedCustomerRating = customerRatingRadios[i].value;
         //  break;
        //}
    //}

// Add the selected customer rating to the data object
//data["customer_rating"] = selectedCustomerRating;

    // ... (Your existing code)



     fetch("/save_client", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => {
        console.log("Data saved successfully:", data);

        const successMessage = document.getElementById("success_message");
        successMessage.style.display = "block";
        setTimeout(() => {
            successMessage.style.display = "none";
        }, 3000);

        const errorMessage = document.getElementById("error_message");
        errorMessage.style.display = "none";
    })
    .catch(error => {
        console.error("Error saving data:", error);

        const errorMessage = document.getElementById("error_message");
        errorMessage.style.display = "block";
        setTimeout(() => {
            errorMessage.style.display = "none";
        }, 3000);

        const successMessage = document.getElementById("success_message");
        successMessage.style.display = "none";
    });
}