@echo off
title ActiveRehab TransCare - Daily GMB Auto-Publishing Engine

echo ============================================================
echo   ActiveRehab TransCare - Daily GMB Auto-Publishing Engine
echo ============================================================

REM 1. Run the Python state machine to select today's post and get the image prompt
python gmb_manager.py

REM 2. Read the prompt out to show what image we need to generate
echo.
echo [System] Current campaign selected successfully.
echo [System] Check 'current_gmb_text.txt' for today's copy.
echo.

echo ============================================================
echo   READY FOR AUTONOMOUS UPLOAD & GEOTAGGING
echo ============================================================
