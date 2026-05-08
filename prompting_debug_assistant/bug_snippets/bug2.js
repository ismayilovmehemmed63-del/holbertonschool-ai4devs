function fetchUserData() {
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                name: "John",
                role: "Developer"
            });
        }, 2000);
    });
}

async function displayDashboard() {
    const user = await fetchUserData();

    console.log("Dashboard");
    console.log("User:", user.name);
    console.log("Role:", user.role);
}

displayDashboard();
