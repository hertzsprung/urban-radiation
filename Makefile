PDFLATEX := pdflatex
TEXCOUNT := texcount
GNUPLOT := gnuplot

GRAPHS := toa-model.tex toa-model-verification.tex

.PHONY: all wc

all: radiation.pdf

wc:
	$(TEXCOUNT) radiation.tex

radiation.pdf: radiation.tex $(GRAPHS)
	$(PDFLATEX) $<
	$(PDFLATEX) $<

$(GRAPHS): radiation.plt radiation.py
	./radiation.py 51 > radiation.dat
	$(GNUPLOT) -e "load '$<'"
