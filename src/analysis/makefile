# Makefile
# requires GNUMake32
# Installation instructions: http://tilburgsciencehub.com/setup


analyze: ../../gen/analysis/output/analysis.html

../../gen/analysis/output/analysis.html: analysis.ipynb ../../gen/data-preparation/output/dataset.csv
	jupyter nbconvert --output-dir='../../gen/analysis/output/' --to html --TemplateExporter.exclude_input=True analysis.ipynb

wipe:
	python wipe.py