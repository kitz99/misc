var myNameSpace = angular.module('myApp', []);

myNameSpace.controller('MyController', 
	function MyController($scope){
		// modelul
		$scope.author = {
		'name' : 'Ionel Popescu',
		'title' : 'Staff author',
		'company' : 'Wala wala'
		}
});
