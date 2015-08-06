var util = require('util');


function Car(color) {
    this.drive = function() {
        return util.format('%s vrooom', this.color);
    };
    this.color = color;
}


function manufactureCar(color) {
    mixPaint(color);
    var newCar = new Car(color);
    recordCarManufacturedNetworkCall(newCar);
    return newCar;
}

function mixPaint(color) {
    console.log('mixing');
    return color;
}

/**
 * Makes a call over the network to DB, this should be MOCKED
 * @param car
 */
function recordCarManufacturedNetworkCall(car) {
    console.log('network call avoid calling in unittest');
    return car;
}


/////////////////////////////////////////////////////////////////////////

/**
 * Async processes all people from db
 * @param callback
 */
function processPeople() {
    var query = 'all';
    fetchDataFromDB(query, function(err, rows) {
        // process all the peoples in the DB
        for (var i=0; i < rows.length; i++) {
            rows.processed = true
        }
    });
}


/**
 * A fake DB call to illustrate function expression unittesting
 *
 * @param data
 * @param callback
 */
function fetchDataFromDB(query, callback) {
    // pretend DB call was made
    var err = null;
    var rows = [
        {name: 'gerald', age: 81}
    ];
    callback(err, rows);
}

module.exports = {
    processPeople: processPeople,
    manufactureCar: manufactureCar
};
