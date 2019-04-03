image = document.querySelector("#image");
prev = 0;
cur = 0;

function change_image() {
	while(cur == prev)
		cur = Math.floor(1+Math.random() * 12);
	prev = cur;
	console.log(`img/img_${cur}.png`);
	image.src = `img/img_${cur}.png`;
	//alert("Changed");
}