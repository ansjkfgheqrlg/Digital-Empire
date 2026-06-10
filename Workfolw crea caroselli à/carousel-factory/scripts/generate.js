const fs = require('fs-extra');
const path = require('path');
const { renderCarousel } = require('./render');

async function main() {
  // Leggi il JSON del carosello (generato da Claude)
  const inputFile = process.argv[2];
  
  if (!inputFile) {
    console.log('Uso: node generate.js <file-carousel.json>');
    console.log('Es:  node generate.js ./input.json');
    process.exit(1);
  }
  
  const carouselData = await fs.readJson(inputFile);
  
  console.log(`🎨 Brand: ${carouselData.brand}`);
  console.log(`📝 Titolo: ${carouselData.titolo}`);
  console.log(`📊 Slide: ${carouselData.slides.length}`);
  console.log('');
  
  await renderCarousel(carouselData);
}

main().catch(console.error);
