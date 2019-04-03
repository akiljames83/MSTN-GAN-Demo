image = document.querySelector("#image");
prev = 0;
cur = 0;

const sleep = (milliseconds) => {
  return new Promise(resolve => setTimeout(resolve, milliseconds))
}

async function change_image() {
	image.src = 'img/load_1.gif';

	time = Math.floor(Math.random()*1500);
	await sleep(1300);

	while(cur == prev)
		cur = Math.floor(1+Math.random() * 12);

	prev = cur;
	console.log(`img/img_${cur}.png`);
	image.src = `img/img_${cur}.png`;
	
}