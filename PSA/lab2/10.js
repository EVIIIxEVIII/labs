const offencesMap = new Map([
    [0, 50],
    [1, 200],
]);

const brokeManRider = (days) =>  {
    let moneySpent = 0;
    let offenceNum = 0;

    for (let i = 0; i < days * 2; i++) {
        const isHairyMuscular = Math.random() < 0.02;
        if (isHairyMuscular) { moneySpent += 6; continue; }

        const isCaught = Math.random() < 0.05;
        if (isCaught)  {
            moneySpent += offencesMap.get(offenceNum) || 300;
            offenceNum++;
        }
    }

    return moneySpent / days;
}

const normieManRider = (days) => {
    return days * 2 * 6;
}

const res = []
for (let i = 0; i < 10000; i++) {
    res.push(brokeManRider(365))
}
const sum = res.reduce((acc, val) => acc + val, 0);

console.log(`Jora Petrovici would spend ${sum/10000} lei in an year on average, after ${10000} experiments`);
console.log(`Normal person would spend ${normieManRider(365)} lei in an year`);
