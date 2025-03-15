document.addEventListener("DOMContentLoaded", function () {
    console.log("Script loaded successfully!");

    // Handle form submission for login
    const loginForm = document.getElementById("loginForm");
    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const formData = {
                email: document.getElementById("email").value,
                password: document.getElementById("password").value
            };

            try {
                const response = await fetch("/api/login", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(formData)
                });

                const data = await response.json();
                if (response.ok) {
                    localStorage.setItem("token", data.token);
                    alert("Login successful!");
                    window.location.href = "/dashboard";
                } else {
                    alert("Error: " + data.message);
                }
            } catch (error) {
                console.error("Error logging in:", error);
            }
        });
    }

    // Fetch user appointments
    async function fetchAppointments() {
        try {
            const response = await fetch("/api/appointments", {
                headers: {
                    "Authorization": "Bearer " + localStorage.getItem("token")
                }
            });

            const data = await response.json();
            if (response.ok) {
                const appointmentsList = document.getElementById("appointmentsList");
                appointmentsList.innerHTML = "";
                data.appointments.forEach((appointment) => {
                    const listItem = document.createElement("li");
                    listItem.textContent = `Dr. ${appointment.doctor_name} - ${appointment.date} at ${appointment.time}`;
                    appointmentsList.appendChild(listItem);
                });
            } else {
                alert("Failed to fetch appointments: " + data.message);
            }
        } catch (error) {
            console.error("Error fetching appointments:", error);
        }
    }

    // Call fetchAppointments when the page loads
    if (document.getElementById("appointmentsList")) {
        fetchAppointments();
    }

    // Handle logout
    const logoutBtn = document.getElementById("logoutBtn");
    if (logoutBtn) {
        logoutBtn.addEventListener("click", function () {
            localStorage.removeItem("token");
            alert("Logged out successfully!");
            window.location.href = "/login";
        });
    }
});
