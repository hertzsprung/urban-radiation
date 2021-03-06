urban-radiation
===============

To start playing quickly, `./presentation.sh`

To run the models
- `./one_year_toa.py <latitude>` to generate one year of TOA insolation data
- `./model_obs_merge.py <met_mast_csv> <cl31_csv> <latitude>` to run the SW and LW models over combined Met mast and CL31 observation data

To compile the report you will need:
- A LaTeX installation including pdflatex, biblatex with biber, siunitx
- Gnuplot
- Python 3
- pygments (for minted syntax highlighting)

Optionally, you will need
- R with [Metrics](https://github.com/benhamner/Metrics/tree/master/R) library (if you want to compute statistics)
- texcount (if you want a word count)
- ghostscript and epspdf if you want to generate presentation plots
