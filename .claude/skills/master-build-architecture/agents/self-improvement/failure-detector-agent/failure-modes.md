# Failure-Detector Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| False negatives | Missed real failures | Multiple passes + all sources | SI self-review | Add more patterns |
| False positives | Over-alarming | Calibrated thresholds | triage review | Tune patterns.