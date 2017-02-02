(function () {
    'use strict';

    angular.module('routerApp').controller('AppController', AppController);

    AppController.$inject = ['$rootScope', '$scope', '$state', '$http'];
    function AppController($rootScope, $scope, $state, $http) {
        var vm = this;
        vm.username = $rootScope.loggedUser;
        vm.password = '';

        vm.message = '';
        vm.users = [];

        vm.getUsers = function(){
            $http.get('/api/users').then(function(resp){
                vm.users = resp.data.result;
            }, function(err){
                vm.message = err;
            });
        }

        vm.createUser = function(){
            var data = {'username':vm.username, 'password':vm.password}
            $http.post('/api/users', data).then(function(resp){
                vm.users = resp.data.result;
                vm.getUsers();
            }, function(err){
                vm.message = err;
            });
        }


        vm.logout = function(){
            $rootScope.loggedUser = null;
            $state.go('login');
        }

        vm.getUsers();
    }
})();
