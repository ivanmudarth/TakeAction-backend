async function getResult(url) {
	let results = await axios.get(`/api/recommendation?url=${url}`).catch((error) => {
		console.log('url function bad');
	});
	return results['data']['charity_url'];
}

function displayCharityUrl(urls) {
	const url_body = document.getElementById('charity-links');
	url_body.innerHTML = '';
	urls.forEach((url) => {
		const h3Node = document.createElement('h3');
		h3Node.innerText = url;
		url_body.appendChild(h3Node);
	});
}

document.getElementById('btn').addEventListener('click', async function() {
	let url = document.getElementById('text-input').value;

	charity_url = await getResult(url);
	displayCharityUrl(charity_url);
	console.log(charity_url);
});
