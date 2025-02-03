const res = []

for (let i = 0; i < 100000000; i++) {
    const x = Math.random();
    let numOfTries = 0;

    for (let j = 0; j < 100; j++) {
        const y = Math.random();
        if (y > x) {
            numOfTries = j
            break
        }
    }

    res.push(numOfTries - 1);
}

const sum = res.reduce((acc, val) => acc + val, 0);
console.log(`A fair entrace fee for the game is: ${sum / res.length} after 100000000 experiments`)
