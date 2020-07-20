var btn=document.getElementsByTagName('span');

window.onload=function() {
	for (i=0; i<btn.length; i++) (function(i) {return function() {
		btn[i].style.color="red"
	};})(i);


	}