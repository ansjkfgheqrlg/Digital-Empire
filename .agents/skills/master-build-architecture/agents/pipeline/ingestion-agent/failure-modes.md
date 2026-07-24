# Ingestion Failure Modes

| Failure | Symptom | Prevention | Detection | Recovery |
|---------|---------|------------|-----------|----------|
| Lost provenance | Atoms without source tags | Mandatory tagging in every step | KG later | Re-ingest with tags |
| Summary (shorter output) | Output < input | P03 + length_check | length_check | Re-process with expansion mandate |