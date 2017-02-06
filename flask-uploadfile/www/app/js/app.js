var routerApp = angular.module('routerApp', ['ui.router', 'ui.bootstrap', 'lr.upload']);

routerApp.$inject = ['AppController'];

// ------ router -------------
routerApp.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/login');
    $stateProvider
        .state('home', {
            url: '/home',
            templateUrl: 'app/pages/home.html',
            controller: 'AppController as vm'
        })
        .state('login', {
            url: '/login',
            templateUrl: 'app/pages/login.html',
            controller: 'LoginController as vm'
        })
        .state('about', {
            // we'll get to this in a bit
        });
});

//-------- login controller --------------
routerApp.controller('LoginController', function($scope, $http, $rootScope, $state) {
    var vm = this;
    
    vm.username = '';
    vm.password = '';
    vm.message = '';

    vm.login = function(){
        if(vm.username=='admin' && vm.password=='123'){
            $rootScope.loggedUser = vm.username;
            $state.go('home');
        }else{
            vm.message = "greska";
        }
    }

});
