# Preparation materials for Discrete Mathematics tutorial

V jednotlivých LaTeX přípravách jsou u problémů poznámky z výuky. Jsou vždy ve formátu `%NOTE: poznamka k uloze ze cviceni`

Google sheets with [activity](https://docs.google.com/spreadsheets/d/170DkIgitdei39mTJSbe60sLbXrxTak9fchzrkC5yohM/edit?gid=913631362#gid=913631362)

## Using the printer at KAM

More information about printingat KAM [here](https://kam.mff.cuni.cz/net/printing.html)

1. Copy pdf file to KAM account folder: `cat <path_to_file> | ssh hartmaj@kam.mff.cuni.cz "cat > output.pdf"`
2. SSH to KAM: `ssh hartmaj@kam.mff.cuni.cz`
3. (OPTIONAL) If printing two A5 pages on single A4 first duplicate a page to create a two page pdf: `gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=combined.pdf -dBATCH input_file.pdf input_file.pdf`
4. Print the document: `lp -o number-up=2 -o fit-to-page -n 2 combined.pdf`

Default printer can be set using: `lpoptions -d <printer_name>`