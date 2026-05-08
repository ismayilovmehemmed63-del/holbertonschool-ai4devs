function fetchUserData(userId) {
    let user = null;

    console.log("Fetching data for user: " + userId);

    // Xəta: setTimeout asinxron işləyir, dəyişən dərhal qayıdır (undefined)
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
    
    // Xəta: userData hələ 'null' olduğu üçün xüsusiyyətlərini oxuya bilməyəcək
    console.log("--- Dashboard ---");
    console.log("User: " + userData.name); 
    console.log("Role: " + userData.role);
}

displayDashboard(101);
