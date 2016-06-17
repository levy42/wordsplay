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
     'restangular'
 ]);

 app.config(function ($stateProvider, $urlRouterProvider, RestangularProvider) {
     // For any unmatched url, send to /route1
     $urlRouterProvider.otherwise("/");
     $stateProvider
         .state('index', {

             url: "/",
             templateUrl: "/static/html/partials/_job_list.html",
             controller: "JobList"
         })

        .state('test', {

             url: "/test",
             templateUrl: "/templates/test.html",
             controller: "TestController"
         })
 });

 app.controller("TestController", ['$scope', 'Restangular', 'CbgenRestangular', '$q',
 function ($scope, Restangular, CbgenRestangular, $q) {


 }]);// end controller