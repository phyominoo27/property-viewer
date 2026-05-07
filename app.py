import streamlit as st
import pandas as pd
import pypdf

st.set_page_config(
    page_title ="Myanmar Property Viewer",
    page_icon="🏠",
    layout="wide"
)

st.title("🏡 Myanmar Property Data Viewer")
st.write(
    "Upload property CSV files, filter listings, view summary stats, "
    "and extract text from property PDF doucments."
)

st.sidebar.header("App Menu")

mode = st.sidebar.selectbox(
    "Choose tool",
    ["CSV Property Viewer", "PDF Reader"]
)

if mode == "CSV Property Viewer":
    st.header("📊 CSV Property Viewer")

    uploaded_csv = st.file_uploader(
        "Upload property CSV",
        type=["csv"]      
    )

    if uploaded_csv is not None:
        df = pd.read_csv(uploaded_csv)
        st.success("CSV uploaded successfully!")
    else:
        st.warning("No CSV uploaded. Using sample property data.")
        df = pd.read_csv("sample_properties.csv")

    st.subheader("Original Property Data")
    st.dataframe(df, use_container_width=True)

    st.sidebar.subheader("CSV Filters")

    if "location" in df.columns:
        locations = ["ALL"] + sorted(df["location"].dropna().unique().tolist())

        selected_location = st.sidebar.selectbox(
            "Filter by location",
            locations
        )

        if selected_location != "ALL":
            filtered_df = df[df["location"] == selected_location]
        else:
            filtered_df = df
    else:
        st.warning("No 'location' column found. showing all data.")
        filtered_df = df
    
    st.subheader("Filtered Results")
    st.dataframe(filtered_df, use_container_width=True )

    st.subheader("Summary Stats")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Properties", len(filtered_df))
    
    if "price_mmk" in df.columns and len(filtered_df) > 0:
        with col2:
            avg_price = filtered_df["price_mmk"].mean()
            st.metric("Average Price", f"{avg_price:,.0f} MMK")

        with col3:
            max_price = filtered_df["price_mmk"].max()
            st.metric("Highest Price", f"{max_price:,.0f} MMK")
    else:
        st.warning("No 'price_mmk' column found or no properties to show price metrics.")

    st.subheader("What This Tool Does")
    st.write(
        "This tool helps real estate agents quickly inspect property  spreadsheets., "
        "filter by location, and understand basic price information."
    )

elif mode == "PDF Reader":
    st.header("📄 PDF Reader")

    uploaded_pdf = st.file_uploader(
        "Upload property PDF",
        type=["pdf"]
    )

    if uploaded_pdf is not None:
        try:
            reader = pypdf.PdfReader(uploaded_pdf)
            text = ""

            for page_number, page in enumerate(reader.pages, start=1):
                page_text = page.extract_text()
                if page_text:     
                    text += f"\n\n--- Page {page_number} ---\n"
                    text += page_text

                if text.strip():
                    st.success("PDF text extracted successfully.") 

                    st.subheader("Extracted Text Preview")
                    st.write(text[:10000])

                    st.download_button(
                        label="Download Extracted Text",
                        data = text,
                        file_name="extracted_property_text.txt",
                        mime="text/plain"
                    )
                else:
                    st.warning("No text could be extracted from the PDF.")
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    else:
        st.info("Upload a PDF file to extract text.")