const form = document.getElementById("validatorForm");

const ipVersion = document.getElementById("ipVersion");
const ipAddress = document.getElementById("ipAddress");

const modal = document.getElementById("resultModal");
const closeModalButton = document.getElementById("closeModal");
const modalButton = document.getElementById("modalButton");

const resultIcon = document.getElementById("resultIcon");
const resultTitle = document.getElementById("resultTitle");
const resultMessage = document.getElementById("resultMessage");


// Change placeholder when IP version changes
ipVersion.addEventListener("change", () => {
    if (ipVersion.value === "4") {
        ipAddress.placeholder = "192.168.1.1";
    } else {
        ipAddress.placeholder = "2001:db8::1";
    }
});

// Submit IP address to Python
form.addEventListener("submit", async (event) => {

    event.preventDefault();
    const version = ipVersion.value;
    const ip = ipAddress.value.trim();
    if (ip === "") {
        showModal(
            false,
            "Invalid Input",
            "Please enter an IP address."
        );
        return;
    }

    try {
        const response = await fetch("/validate", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                version: version,
                ip: ip
            })
        });

        const data = await response.json();

        showModal(
            data.valid,
            data.valid
                ? `Valid IPv${version} Address`
                : `Invalid IPv${version} Address`,
            data.message
        );

    } catch (error) {

        showModal(
            false,
            "Connection Error",
            "Unable to connect to the Python server."
        );
        console.error(error);
    }
});


// Show modal
function showModal(success, title, message) {
    resultIcon.className = "result-icon";
    if (success) {

        resultIcon.classList.add("success");
        resultIcon.textContent = "✓";

    } else {

        resultIcon.classList.add("error");
        resultIcon.textContent = "×";

    }
    resultTitle.textContent = title;
    
    resultMessage.textContent = message;
    modal.classList.add("active");
}


// Close modal
function closeModal() {
    modal.classList.remove("active");
}


// Close buttons
closeModalButton.addEventListener(
    "click",
    closeModal
);

modalButton.addEventListener(
    "click",
    closeModal
);


// Close when clicking outside modal
modal.addEventListener("click", (event) => {
    if (event.target === modal) {
        closeModal();
    }
});


// Close with Escape key
document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
        closeModal();
    }
});
