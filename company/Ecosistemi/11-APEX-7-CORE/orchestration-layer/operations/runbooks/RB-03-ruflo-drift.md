# RB-03 RuFlo schema drift or crash

1. Open the RuFlo breaker and disable its route.
2. Continue only eligible R0/R1 work through LocalRuntime.
3. Preserve schema hashes, stderr and source/runtime pins.
4. Re-run STATIC, SMOKE and CHAOS certification.
5. Never coerce an unknown schema or silently change provider.
