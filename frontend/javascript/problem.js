let displayProblem = function (newTitle, newDescription) {
	let content = document.getElementById('content');
	let container = document.createElement('div');
	let title = document.createElement('h2');
	title.textContent = newTitle;
	let description = document.createElement('p');
	description.textContent = newDescription;
	let inputBox = document.createElement('input');
	let submitButton = document.createElement('button');
	submitButton.setAttribute('type','button');
	submitButton.textContent = "Submit";
	container.appendChild(title);
	container.appendChild(description);
	container.appendChild(inputBox);
	container.appendChild(submitButton);
	content.appendChild(container);
}
displayProblem("Test Title", "This is the problem");
displayProblem("Test Title 2", "This is the problem 2");
