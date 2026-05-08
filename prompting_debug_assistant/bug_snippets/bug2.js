function fetchUserData(userId) {
    let user = null;
    console.log("Fetching data for user: " + userId);
    setTimeout(() => {
        console.log("Data received from server...");
        user = {
            id: userId,
            name: "Admin",
            role: "Developer"
        };
    }, 2000);

    return user; 
}
function displayDashboard(userId) {
    const userData = fetchUserData(userId);

    console.log("--- Dashboard ---");
    console.log("User: " + userData.name); 
    console.log("Role: " + userData.role);
}

displayDashboard(101);
