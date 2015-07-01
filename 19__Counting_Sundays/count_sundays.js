(function countSundays () {

    var count = 0,
        startYear = 1901,
        years = 100;

        for (var m = 0; m < 12*years; m++) {

            first = new Date(startYear, m, 1);
            if (first.getDay() === 0) {
                count++;
            }

        }

    console.log(count);

})();
