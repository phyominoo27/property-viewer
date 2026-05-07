# Myanmar Property Data Viewer

A Streamlit app for real estate agents to view property CSV data and extract text from property PDF documents.

## Problem

Real estate agents often receive property information in spreadsheets, brochures, and PDF documents. Manually reading and organizing this information takes time.

This tool helps agents quickly inspect property data, filter listings by location, view simple price stats, and extract readable text from property PDFs.

## Features

- Upload property CSV files
- View property data as a table
- Filter listings by location
- Show total property count
- Show average property price
- Show highest property price
- Upload property PDF documents
- Extract readable PDF text
- Download extracted text as `.txt`

## Tech Stack

- Python
- Streamlit
- Pandas
- pypdf

## How to Run Locally
bash
pip install -r requirements.txt
streamlit run app.py


## CSV Format

The app works best with CSV files using these columns:

csv
type,location,bedrooms,bathrooms,sqft,price_mmk

Example:

csv
Apartment,Yangon,2,1,850,180000000
House,Mandalay,3,2,1600,250000000
Condo,Yangon,1,1,600,120000000 (1/3)


## PDF Reader Notes

The PDF reader works with text-based PDFs.

It may not work well with scanned image-only PDFs. Those will require OCR in a future version.

## Demo

Live app: ADD_STREAMLIT_LINK_HERE

## Screenshots

Add screenshot here after deployment.

## Future Improvements

- Add Burmese search
- Add price range filter
- Add messy Facebook property post parser
- Add AI-generated Burmese and English property descriptions
- Add OCR for scanned PDFs
- Add property Q&A using MiniMax

## Demo

Live app: https://property-viewer-e9ask5a3etvyjlknyisfcr.streamlit.app/
