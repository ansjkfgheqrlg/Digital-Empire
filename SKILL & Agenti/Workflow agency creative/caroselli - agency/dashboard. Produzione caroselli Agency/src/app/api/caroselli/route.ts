import { NextRequest, NextResponse } from "next/server";
import path from "path";
import fs from "fs";

const PROJECT_DIR = path.resolve(process.cwd(), "..");
const CAROSELLI_DIR = path.join(PROJECT_DIR, "output_caroselli");

export async function GET(req: NextRequest) {
  const { searchParams } = new URL(req.url);
  const folder = searchParams.get("folder");
  const file = searchParams.get("file");

  // Se sono forniti folder e file, restituisce l'immagine come stream binario
  if (folder && file) {
    try {
      const sanitizedFolder = path.basename(folder);
      const sanitizedFile = path.basename(file);
      
      const imagePath = path.join(CAROSELLI_DIR, sanitizedFolder, sanitizedFile);

      if (!fs.existsSync(imagePath)) {
        return new NextResponse("Immagine non trovata", { status: 404 });
      }

      const fileBuffer = fs.readFileSync(imagePath);
      return new NextResponse(fileBuffer, {
        headers: {
          "Content-Type": "image/png",
          "Cache-Control": "public, max-age=31536000, immutable",
        },
      });
    } catch (error: any) {
      return new NextResponse(`Errore: ${error.message}`, { status: 500 });
    }
  }

  // Altrimenti, elenca tutti i caroselli e le relative slide
  try {
    if (!fs.existsSync(CAROSELLI_DIR)) {
      return NextResponse.json({ caroselli: [] });
    }

    const items = fs.readdirSync(CAROSELLI_DIR);
    const caroselliList = [];

    for (const item of items) {
      const itemPath = path.join(CAROSELLI_DIR, item);
      const stat = fs.statSync(itemPath);

      if (stat.isDirectory()) {
        const files = fs.readdirSync(itemPath);
        const pngSlides = files
          .filter((f) => f.toLowerCase().endsWith(".png"))
          .sort((a, b) => {
            // Ordina numericamente le slide (es. slide_1, slide_2...)
            const numA = parseInt(a.replace(/\D/g, "")) || 0;
            const numB = parseInt(b.replace(/\D/g, "")) || 0;
            return numA - numB;
          });

        caroselliList.push({
          folderName: item,
          slides: pngSlides,
          createdAt: stat.mtime,
        });
      }
    }

    // Ordina i caroselli per data di ultima modifica (dal più recente)
    caroselliList.sort((a, b) => b.createdAt.getTime() - a.createdAt.getTime());

    return NextResponse.json({ caroselli: caroselliList });
  } catch (error: any) {
    return NextResponse.json({ error: error.message }, { status: 500 });
  }
}
