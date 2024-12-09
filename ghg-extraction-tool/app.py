import streamlit as st
import pandas as pd
import pdfplumber
import docx
import io
import re
from typing import Tuple, Dict, Optional
import tempfile
import os

# Set page configuration
st.set_page_config(
    page_title="Sustainability Report Document Parser",
    layout="wide"
)

class DocumentParser:
    def __init__(self):
        self.supported_extensions = ['.pdf', '.docx']
    
    def extract_text_from_pdf(self, file) -> str:
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text
    
    def extract_text_from_docx(self, file) -> str:
        doc = docx.Document(file)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        return '\n'.join(text)
    
    def extract_emissions_data(self, text: str) -> Dict[str, Tuple[float, str, str]]:
        # Initialize results dictionary
        results = {
            'scope1': (0, 'tCO2e', 'Not found'),
            'scope2': (0, 'tCO2e', 'Not found'),
            'scope3': (0, 'tCO2e', 'Not found')
        }
        
        # Simple pattern matching (this could be enhanced with more sophisticated NLP)
        patterns = {
            'scope1': r'Scope 1.*?(\d+[\d,.]*)\s*(tCO2e|mtCO2e|CO2e)',
            'scope2': r'Scope 2.*?(\d+[\d,.]*)\s*(tCO2e|mtCO2e|CO2e)',
            'scope3': r'Scope 3.*?(\d+[\d,.]*)\s*(tCO2e|mtCO2e|CO2e)'
        }
        
        for scope, pattern in patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                value = float(match.group(1).replace(',', ''))
                unit = match.group(2)
                context = text[max(0, match.start() - 50):match.end() + 50]
                results[scope] = (value, unit, context)
                break
                
        return results

class SustainabilityApp:
    def __init__(self):
        self.parser = DocumentParser()
        
    def calculate_monetized_emissions(self, total_emissions: float, unit: str) -> float:
        # Convert to tons if in million tons
        if unit.lower().startswith('m'):
            total_emissions *= 1_000_000
        
        # Calculate monetized value ($236 per ton)
        monetized = total_emissions * 236
        
        # Convert to billions and round to 2 decimal places
        return round(monetized / 1_000_000_000, 2)
    
    def run(self):
        st.title("Sustainability Report Document Parsing Tool")
        
        st.write("""
        This tool extracts greenhouse gas emission sustainability data from textual sustainability reports. 
        The tool supports upload as DOCX or PDF formats. Other formats are not supported at this time.
        """)
        
        with st.expander("Detailed Using Instructions"):
            st.write("""
            1. Upload your sustainability report by dragging and dropping it into the app.
            2. The program analyzes the document for GHG reporting data across Scopes 1, 2, and 3.
            3. Outputs include detected parameters, their values, details about where they were found in the text, and CSV-formatted data for further analysis.
            """)
        
        st.warning("""
        Disclaimer: This app was both AI-generated and utilizes AI. Therefore, the accuracy of the calculations 
        cannot be guaranteed, and it's recommended that you verify the calculations.
        """)
        
        uploaded_file = st.file_uploader(
            "Upload your sustainability report (PDF or DOCX)",
            type=['pdf', 'docx']
        )
        
        if uploaded_file is not None:
            # Create temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
                tmp_file_path = tmp_file.name
            
            try:
                # Extract text based on file type
                if uploaded_file.name.endswith('.pdf'):
                    text = self.parser.extract_text_from_pdf(tmp_file_path)
                else:
                    text = self.parser.extract_text_from_docx(tmp_file_path)
                
                # Extract emissions data
                emissions_data = self.parser.extract_emissions_data(text)
                
                # Display results
                st.subheader("Parsed Data")
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.write("**Scope 1 Emissions**")
                    st.write(f"Value: {emissions_data['scope1'][0]:,}")
                    st.write(f"Unit: {emissions_data['scope1'][1]}")
                    st.write("Context:", emissions_data['scope1'][2])
                
                with col2:
                    st.write("**Scope 2 Emissions**")
                    st.write(f"Value: {emissions_data['scope2'][0]:,}")
                    st.write(f"Unit: {emissions_data['scope2'][1]}")
                    st.write("Context:", emissions_data['scope2'][2])
                
                with col3:
                    st.write("**Scope 3 Emissions**")
                    st.write(f"Value: {emissions_data['scope3'][0]:,}")
                    st.write(f"Unit: {emissions_data['scope3'][1]}")
                    st.write("Context:", emissions_data['scope3'][2])
                
                # Calculate total emissions
                total_emissions = sum(data[0] for data in emissions_data.values())
                st.subheader("Total All Scopes GHG Emissions")
                st.write(f"{total_emissions:,} {emissions_data['scope1'][1]}")
                
                # Calculate monetized emissions
                monetized = self.calculate_monetized_emissions(total_emissions, emissions_data['scope1'][1])
                st.subheader("Monetized GHG Emissions")
                st.write(f"${monetized:,} billion")
                
                # Create CSV data
                st.subheader("CSV Data")
                df = pd.DataFrame({
                    'Scope': ['Scope 1', 'Scope 2', 'Scope 3', 'Total'],
                    'Emissions': [
                        emissions_data['scope1'][0],
                        emissions_data['scope2'][0],
                        emissions_data['scope3'][0],
                        total_emissions
                    ],
                    'Unit': [
                        emissions_data['scope1'][1],
                        emissions_data['scope2'][1],
                        emissions_data['scope3'][1],
                        emissions_data['scope1'][1]
                    ],
                    'Monetized_Value_Billion_USD': [
                        self.calculate_monetized_emissions(emissions_data['scope1'][0], emissions_data['scope1'][1]),
                        self.calculate_monetized_emissions(emissions_data['scope2'][0], emissions_data['scope2'][1]),
                        self.calculate_monetized_emissions(emissions_data['scope3'][0], emissions_data['scope3'][1]),
                        monetized
                    ]
                })
                
                st.dataframe(df)
                
                # Download button for CSV
                csv = df.to_csv(index=False)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name="emissions_data.csv",
                    mime="text/csv"
                )
                
            except Exception as e:
                st.error(f"An error occurred while processing the file: {str(e)}")
            
            finally:
                # Clean up temporary file
                os.unlink(tmp_file_path)
        
        # Clear Data button
        if st.button("Clear Data"):
            if st.button("Are you sure? This will clear all data."):
                st.experimental_rerun()

if __name__ == "__main__":
    app = SustainabilityApp()
    app.run()