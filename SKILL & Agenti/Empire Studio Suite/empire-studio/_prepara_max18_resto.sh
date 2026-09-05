set -u
ids="140FuW7b9pk RnNSRF4s9nk JTn5pqm9ecM O2IDhISyy8Y DI5aWJiFAt8 NmoOZVTrTXA"
n=3
for id in $ids; do
  n=$((n+1))
  run=$(printf "max18-v%02d-%s" "$n" "$id")
  echo "=============================================="
  echo ">>> $run  ($id)"
  if [ -f "runs/$run/scenes.md" ]; then echo "GIA' PRONTO, salto"; continue; fi
  python scripts/yt_ingest.py --input "https://www.youtube.com/watch?v=$id" --run "$run" 2>&1 | tail -5
  python scripts/frame_extractor.py --run "$run" --interval 6 --height 720 2>&1 | tail -4
  python scripts/scene_detector.py --run "$run" --interval 6 --threshold 3.0 2>&1 | tail -4
  echo "<<< $run fatto: frame=$(ls runs/$run/frames 2>/dev/null | wc -l) scene=$(grep -c '^| [0-9]' runs/$run/scenes.md 2>/dev/null || echo 0)"
done
echo "=== PREPARAZIONE FINITA ==="
