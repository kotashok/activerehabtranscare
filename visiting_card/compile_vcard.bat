@echo off
title ActiveRehab vCard PDF Compiler
echo ===================================================
echo ActiveRehab TransCare Business Card PDF Compiler
echo Card Size: 3.5in x 2in (Standard Business Card)
echo ===================================================
echo.
echo Launching Node.js to generate vcard.pdf...
echo.
node generate_vcard_pdf.js
echo.
echo ===================================================
echo Compilation complete!
echo Print-ready vcard.pdf saved to this folder.
echo ===================================================
echo.
pause
