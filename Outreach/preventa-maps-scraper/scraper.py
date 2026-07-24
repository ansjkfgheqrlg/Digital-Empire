#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Owner: 01-AGENCY · Controllore: A2-QA · Origine: FORGE
Governo: MANDATO Art.8 + ADR-003 + ADR-008

Wrapper script for Preventa Maps Scraper.
Delegates to the modular implementation inside 02-AUTOMAZIONI-E-SCRIPTS/run.py.
"""
from __future__ import annotations

import os
import sys

# Aggiunge 02-AUTOMAZIONI-E-SCRIPTS al path per caricare i moduli estratti
SCRIPTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "02-AUTOMAZIONI-E-SCRIPTS")
sys.path.append(SCRIPTS_DIR)

import run

if __name__ == "__main__":
    run.main()
