function calculateTotal(items) {
    let total = 0;
    for (let i = 0; i < items.length; i++) {
        total += items[i].price;
    }
    return total;
}

function findUser(users, id) {
    for (let i = 0; i < users.length; i++) {
        if (users[i].id === id) {
            return users[i];
        }
    }
    return null;
}

const items = [
    { name: "Apple", price: 1.5 },
    { name: "Banana", price: 0.75 },
    { name: "Cherry", price: 2.0 }
];

console.log(calculateTotal(items));
