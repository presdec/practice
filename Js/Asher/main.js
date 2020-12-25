const arr1 = [
    ["name", "id", "age", "weight", "Cool"],
    ["Susan", "3", "20", "120", true],
    ["John", "1", "21", "150", true],
    ["Bob", "2", "23", "90", false],
    ["Ben", "4", "20", "100", true],

];

const arr2 = [
    ["name", "id", "height"],
    ["Bob", "3", "50"],
    ["John", "1", "45"],
    ["Ben", "2", "43"],
    ["Susan", "4", "48"],

];

const arr3 = [
    ["name", "id", "parent"],
    ["Bob", "3", "yes"],
    ["John", "1", "yes"]

];

let tempA = [];
// read array of arrays line by line and parse the data
for (index = 1; index < arr1.length; index++) {
    rows = arr1[index];
    let columns = arr1[0];
    let result =  rows.reduce(function(result, field, index) {
        result[columns[index]] = field;
        return result;
    }, {})
    tempA.push(result);
}

let tempB = [];
// read array of arrays line by line and parse the data
for (index = 1; index < arr2.length; index++) {
    rows = arr2[index];
    let columns = arr2[0];
    let result =  rows.reduce(function(result, field, index) {
        result[columns[index]] = field;
        return result;
    }, {})
    tempB.push(result);
}

let tempC = [];
// read array of arrays line by line and parse the data
for (index = 1; index < arr3.length; index++) {
    rows = arr3[index];
    let columns = arr3[0];
    let result =  rows.reduce(function(result, field, index) {
        result[columns[index]] = field;
        return result;
    }, {})
    tempC.push(result);
}

// make an array of objects in unique key pairs from 2 arrays
function fillObject(from, to) {
    for (let key in from) {
        if (from.hasOwnProperty(key)) {
            if (Object.prototype.toString.call(from[key]) === '[object Object]') {
                if (!to.hasOwnProperty(key)) {
                    to[key] = {};
                }
                fillObject(from[key], to[key]);
            }
            else if (!to.hasOwnProperty(key)) {
                to[key] = from[key];
            }
        }
    }
}

fillObject(tempA, tempB);
fillObject(tempB, tempC);

// get the list of all keys
let allkeys = []
tempC.forEach((objInArr) => {
    allkeys = allkeys.concat(Object.keys(objInArr))
})

// check all tempC entries for missing keys, add null value
tempC.forEach((objInArr, i) => {
    allkeys.forEach((key) => {
        if (objInArr[key] === undefined) {
            // the generic value, in this case 0
            tempC[i][key] = null
        }
    })
})

/*

At this point SOLVED, the arrays are merged and missing values are null
only problems are three:

1. its in key pairs objects in array, not array of arrays with header arrays
2. the keys aren't in order, ie parent appears last in ben but third in bob
3. the objects aren't in the right 'name' order. Ie Susan first
*/

console.log*(JSON.stringify(tempC));


//Solution problem 3, sorting the names so that it matches arr1.
//sorts the .object by property given, in reverse ,to match original array
dynamic_sort = function(property) {
    let sort_order = -1;
    if(property[0] === "-") {
        sort_order = 1;
        property = property.substr(1, property.length - 1);
    }
    return function (a,b) {
        let result = (a[property] < b[property]) ? -1 : (a[property] > b[property]) ? 1 : 0;
        return result * sort_order;
    }
}

tempC.sort(dynamic_sort("name"));


//Solution problem 2, sorting the properties so that it matches arr1.
let _ = require('underscore');
var arr = tempC;
let order = Object.keys(tempC[0]);
var sorted = _.sortBy(arr, function(obj){ 
    return _.indexOf(order, obj.key);
});

console.log(sorted);

// no idea why this isn't working, particularly since standalone it works..
// maybe i'm importing the underscore library wrong?
// https://jsfiddle.net/feb70gn9/


//Solution problem 1. Revert back to an array of arrays
let output = sorted.map(function(obj) {
    return Object.keys(obj).map(function(key) {
        return obj[key];
        });
});

output.unshift((Object.keys(sorted[0])));
console.log(JSON.stringify(output));