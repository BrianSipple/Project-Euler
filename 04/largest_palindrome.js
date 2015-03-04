/**
*  A palindromic number reads the same both ways.
*  The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
*
*  Find the largest palindrome made from the product of two 3-digit numbers.
*/

function isPalindrome (n) {

    var reversed = parseInt(n.toString().split('').reverse().join(''));

    return reversed === n;
}


function findLargestPalindromeOfProducts(digits) {

    var maxNumber = '';
    var minNumber = Math.pow(10, digits-1);

    var product;
    var maxFound = 0;
    var factorsFound;

    for (var i = 0; i < digits; i++) {
        maxNumber += '9';
    }

    // We have maximums and a minumum that bound the search
    maxNumber = Number(maxNumber);

    for (var x = minNumber; x < maxNumber; x++) {
        for (var y = minNumber; y < maxNumber; y++) {
            product = x * y;
            if (isPalindrome(product)) {
                if (product > maxFound) {
                    maxFound = product;
                    factorsFound = [x, y];
                }
            }
        }
    }

    console.log(factorsFound);
    return maxFound;

}

console.log(findLargestPalindromeOfProducts(3));
