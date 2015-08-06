var assert = require('chai').assert;
var example = require('./../libs/example.js');
var sinon = require('sinon');


describe('example.js', function() {
    describe('manufactureCar()', function() {
        it('should create a new car', function() {
            var blueCar = example.manufactureCar('blue');
            assert.equal(blueCar.color, 'blue');
            assert.equal(blueCar.drive(), 'blue vrooom');
        });
    });


    describe('export private method to allow unittest', function() {
        it('mixPaint() should be exported so we can test on it', function() {
            var paintColor = example.mixPaint('blue');
            assert.equal(paintColor, 'blue');
        });
    });


    describe('manufactureCar() mock network call', function() {
        it('should mock recordCarManufacturedNetworkCall inside manufactureCar so that no' +
               'network calls are made during unittest using DI', function() {

            // factor out into Network object and use dependency injection to
            // inject it into manufactureCar.
            // use a mock network object (sinon) in this test to assert that
            // network.recordCarManufacturedNetworkCall was called inside manufactureCar
            var mockNetwork = {
                recordCarManufacturedNetworkCall: sinon.spy()
            };
            var blueCar = example.manufactureCar('blue', mockNetwork);
            assert.equal(blueCar.color, 'blue');
            assert.equal(blueCar.drive(), 'blue vrooom');
            assert.isTrue(mockNetwork.recordCarManufacturedNetworkCall.called);
        });
    });


    describe('breakout fetchDataFromDB callback in processPeople and export it so it' +
            'can be unittested', function() {

        it('should add proccessed to all rows', function() {
            var rows = [
                {name: 'gerald', age: 81}
            ];
            var err = null;
            var processedRows = example.processPeopleFetchDataCallback(err, rows);
            assert.equal(processedRows.length, 1);
            assert.isTrue(processedRows[0].processed);
        });
    });


    describe('move fetchDataFromDB to a network object and inject it into processPeople', function() {
        it('should assert fetchDataFromDB was called with a query', function() {
            var mockNetwork = {
                fetchDataFromDB: sinon.spy()
            };
            example.processPeople(mockNetwork);
            assert.isTrue(mockNetwork.fetchDataFromDB.called);
            assert.equal(mockNetwork.fetchDataFromDB.getCall(0).args[0], 'all');
        })
    })
});