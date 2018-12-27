let header_funct = function () {
	let header = document.getElementById('header');
	header.setAttribute('style', 'height: 50px; background: #0086b3; display: flex;');
	let nameLink = document.createElement('h1');
	nameLink.setAttribute('style', 'align-self: center;');
	nameLink.textContent="Branchback";
	nameLink.setAttribute('href','index.html');
	nameLink.setAttribute('id','name');
	header.appendChild(nameLink);
};
header_funct();
