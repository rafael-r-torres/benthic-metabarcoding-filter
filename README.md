# Benthic Metabarcoding Ecological Filter

This repository contains the standardized filtering logic used to process 16S, 18S, and COI metabarcoding data, specifically optimized for marine benthic ecology.

## 🔗 [Live Interactive Decision Tree](https://rafael-r-torres.github.io/benthic-metabarcoding-filter/)

## 📊 Methodology Flowchart
![Methodology Flowchart](Explicit_Methodology_Flowchart.png)

## 🛠 Filtering Logic Overview
The filter follows a strict 10-step sequence to remove contaminants and non-target taxa:

1.  **Statistical Confidence:** Removes low-quality hits (e-value > 0.01).
2.  **Taxonomic Integrity:** Discards sequences not matched in WoRMS or missing Kingdom data.
3.  **Kingdom Check:** Filters out non-Animalia (Bacteria, Fungi, Plantae, etc.).
4.  **Terrestrial Contaminants:** Removes Hexapoda and Arachnida (except marine Halacaridae).
5.  **Pelagic Exceptions:** Removes 16 specific planktonic genera and pelagic classes (e.g., Thaliacea).
6.  **Vertebrate Sweep:** Removes Chordata (except benthic Ascidiacea and Leptocardii).
7.  **Parasite Identification:** Flags Dicyemida and parasitic feeding modes.
8.  **Tardigrada Check:** Specific flag for Phylum Tardigrada.
9.  **Benthic Validation:** Confirms taxa with explicit 'benthos' or 'macrobenthos' tags.
10. **Benthic Proxy:** Keeps typically benthic phyla (Annelida, Mollusca, etc.) when ecology tags are missing.

## 💻 Technical Implementation
The filtering is implemented via a nested logic string used in Excel/LibreOffice and visualized via a Python-based Graphviz pipeline.
