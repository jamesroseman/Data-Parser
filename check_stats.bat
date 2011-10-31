@echo off
FOR /F %%A in (input.txt) DO (
	curl -o temp.html www.tuftsalumni.org/%%A 
	FOR /F "tokens=1,2 delims=:" %%B in ('FINDSTR /I /R "<H1>Travel-Learn Program</H1>" temp.html') DO (
	ECHO %%A >> output.txt
  )
)
start csvParser.py
exit