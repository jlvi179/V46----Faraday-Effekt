all: build/v46.pdf

build/v46.pdf: build/ndotiert1.pdf build/ndotiert2.pdf build/hochrein.pdf build/BFeld.pdf v46.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build v46.tex
	lualatex  --output-directory=build v46.tex
	biber build/v46.bcf
	lualatex  --output-directory=build v46.tex

build/BFeld.pdf: BFeld.txt BFeld.py | build
	python BFeld.py

build/ndotiert1.pdf: Messungen1.txt ndotiert1.py | build
	python ndotiert1.py

build/ndotiert2.pdf: Messungen2.txt ndotiert2.py | build
	python ndotiert2.py

build/hochrein.pdf: Messungen3.txt hochrein.py | build
	python hochrein.py

build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
