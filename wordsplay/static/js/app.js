/**
 * Created by vitaliy on 14.06.16.
 */

function create_game() {
    value = document.getElementById("timeSelect").value;
    if (value == '') {
        value = 60
    }
    window.location = '/game/action?action=create&move_time=' + value;
}

var app = angular.module('MyApp', [
    'ui.router',
]).config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('((');
    $interpolateProvider.endSymbol('))');
});

app.config(function ($stateProvider, $urlRouterProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider

        .state('index', {

            url: "/",
            templateUrl: "/test",
            controller: "JobList"
        })

        .state('games', {

            url: "/game",
            templateUrl: "/game",
            controller: "GameController"
        })
});

app.controller("GameController", ['$scope', '$q',
    function ($scope, CbgenRestangular, $q) {


    }]);// end controller
