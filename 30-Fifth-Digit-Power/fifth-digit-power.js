/**
Surprisingly there are only three numbers that can be written
as the sum of fourth powers of their digits:

1634 = 1 ^ 4 + 6 ^ 4 + 3 ^ 4 + 4 ^ 4
8208 = 8 ^ 4 + 2 ^ 4 + 0 ^ 4 + 8 ^ 4
9474 = 9 ^ 4 + 4 ^ 4 + 7 ^ 4 + 4 ^ 4
As 1 = 1 ^ 4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be
written as the sum of fifth powers of their digits.
*/

function sum (nums) {
    let res = 0;
    for (n of nums) {
        res += n;
    }
    return res;
}

function sumOfDigitPowers (n, power) {

    let res = 0,
    digits = n.toString().split('');

    for (d of digits) {
        res+= Math.pow(d, power);
    }

    return res;
}

function findNumsMatchingSumOfDigitPowers(power) {

    let matches = [],
    rangeMin = 10,  // Any single digit to a power is not a sum of digit powers
    rangeMax = (Math.pow(9, power)) * (power - 1);  // The number of digits for the sum must have the same number of digits as a candidate, see the table below:

    for (let i = rangeMin; i < rangeMax; i++) {

        if (sumOfDigitPowers(i, power) === i) {
            matches.push(i);
        }
    }
    console.log('Matches computed for sum of digits to the power of ' + power + ':');
    console.log(matches);

    return matches;
}

export function runner() {

    let matches;

    matches = findNumsMatchingSumOfDigitPowers(4);
    console.log('Sum of matches: ' + sum(matches));

    matches = findNumsMatchingSumOfDigitPowers(5);
    console.log('Sum of matches: ' + sum(matches));

};
