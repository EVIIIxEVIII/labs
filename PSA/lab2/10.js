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

console.log(`Jora Petrovici would spend ${brokeManRider(365)} lei in an year`);
console.log(`Normal person would spend ${normieManRider(365)} lei in an year`);
