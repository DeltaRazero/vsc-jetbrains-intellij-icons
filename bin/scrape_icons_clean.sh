#!/usr/bin/bash

__DIR__=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

SCRAPER="python \"$__DIR__/../scripts/icon_scraper/scraper.py\" \"$__DIR__/../resources/icons/jetbrains\""

eval $SCRAPER --clean
eval $SCRAPER # Call another time to check downloads 
