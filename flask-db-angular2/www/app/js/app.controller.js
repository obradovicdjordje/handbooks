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
            var req = {
                method: 'GET',
                url: '/api/users',
                headers: {'auth-token': $rootScope.token}
            }
            $http(req).then(function(resp){
                vm.users = resp.data;
            }, function(err){
                vm.message = err;
            });
        }

        vm.createUser = function(){
            var req = {
                method: 'POST',
                url: '/api/users',
                headers: {'auth-token': $rootScope.token},
                data: {'username':vm.username, 'password':vm.password}
            }
            $http(req).then(function(resp){
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
