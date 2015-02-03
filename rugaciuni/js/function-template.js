// JavaScript Document
// functie template pentru a lua informatiile din json-ul ce corespunde fiecarei rugaciuni in parte


function getData(jsonURL, containerID){
	/*
	 * iau ca parametru url-ul json-ului si id-ul containerului unde trebuie plasat, si sot informatia
	*/ 
	var aici = $(containerID);
	$.getJSON( jsonURL, function( data ) {
		var aux = data.results[0].paragrafe;
		if(!(aux instanceof Array) ){
			aici.append($(aux).addClass('paragrafe-text'));
		}
		else {
			for(var i = 0; i < aux.length; i++){
				aici.append($(aux[i]).addClass('paragrafe-text'));
			}
		}
 	 });
}