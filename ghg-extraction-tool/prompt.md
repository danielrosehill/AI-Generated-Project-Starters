# Original prompt (spoken, voice to text)

**Note this prompt was recorded by dictation and an LLM optimized version of this prompt appears after it alongside the prompt which was used to generate that improved version**

Your task is to generate a web-based GUI which has the purpose of ingesting sustainability data reports provided by the user, and extracting several key target data points.

Generate an app that can be deployed on Streamlit. 

If you need to use API keys in order to make this work, please do so in a manner that is compliant with Streamlit standards for protecting secrets.

The functionality of the web UI should be as follows:

The user will encounter a screen with text inviting them to upload a sustainability report. 

You can expect that the report will be a PDF or .docx. Only accept these formats and if the user attempts to open upload data such as CSV or XLSX formats, respond with an error message that this tool only processes documents and data formats are not accepted.

The manner in which the user uploads the document should be a drag and drop interface.

Upon receiving the document, your task is to parse it and attempt to extract the following three pieces of information. 

Scope 1 emissions
Scope 2 emissions
Scope 3 emissions. 

Additionally, you should extract the following matching data points for each of these variables:

Scope 1 emissions units
Scope 2 emissions units
Scope 3 emissions units

You can expect that generally the reporting units will be the same across all three scopes, but occasionally you may encounter variance.
 
The first of these fields are numeric values and must be exported as valid numbers without any text characters. 

The second is the reporting unit in which the report is denominated. 

When parsing the document for these data points, be aware that you may encounter instances in which the same data point is provided in several tables. 

You may find data tables providing numbers on both a equity basis and an operating basis. If you encounter this in one of the reports you parse, choose the numbers from the operating basis table. 

Scope two emissions data may be reported on both a market basis and a location basis. If you encounter this variant in the data that you analyze, choose the location basis.

For scope 3 emissions, you may encounter more variability presentation. 

The figure you are looking for is the total scope 3 emissions. 

If you find that the scope three emissions are reported on a few different bases, the basis that you choose for your computations should be the total scope three emissions. 

If you are not sure about any of the scopes that you encounter in the report, you should note that in a Notes output which can be appended after the main body of your output. Additionally, you may find that not all of the three scopes are reported, or some scopes are reported in groups, for example, scope 1 and 2. If you find that a scope was not reported, simply note this value as 0. You can add in the notes section that the scope was not included in the report. If you find that scope one and scope 2 are not individually reported, report the total as the scope two emissions and leave scope 1 as 0. However, if you encounter this variant, you must note that this was the reporting method you encountered in the notes output. 

Your sole source of information for computing the information should be the PDF document that the user supplies. Do not attempt to enhance your output by using any external sources for the data. 

An example of a valid data point that you may encounter is 1204 million tons of carbon dioxide equivalents for scope 1.

In this case, the category is Scope 1, the unit is MTC02E, and the reporting units can be abbreviated MTCO2E.

After you parse the document for these data points, provide the output of that process in a text box which should populate beneath the drag-and-drop field. 

Within that text box, populate the following text:

- For scope 1, provide all the data points in fields, and beneath that, provide a description of where you found the data in the document. Provide both the page number and a quote.
  
Repeat this format for scope 1, 2 and 3.

The next section in your output after parsing the document should be all scopes reporting. This is a computed field which is calculated by adding together the total scope 1, 2 and three reporting. Use the same reporting unit. 

This figure should be labeled total all scopes GHG emissions. 

The next section in your output should be called monetized GHG emissions. Before providing the data, have a note that says this section consists of the company's emissions monetized at the rate of $236 per ton of carbon dioxide equivalents. 

In this table, you should take the total emissions and monetize them by applying the following calculations:

- If the emissions are reported in millions of tons of carbon dioxide equivalents, multiply them by 236 million.  
- If the emissions are reported in tons of carbon dioxide equivalents, multiply them by 236.
  
When you calculate that number, express it in billions of dollars, correct to two decimal places.

The next section of your output should be CSV data. Introduce the section stating that. This section provides a row of CSV data which you can copy and paste into a spreadsheet, program, or anything else you are using to analyze this data with. Firstly, there should be a header row. This header row is based upon all the parameters we discussed and must remain exactly the same between usages. Beneath that, in a separate section, is the data row. This section, unlike the header row, can be edited by the user with an inline text editor. The field will pre populate with all the data that was computed during the analysis. If any data points are missing, they should be noted as simply empty values, but the strict format of the CSV should be preserved according to the data header row.

 At the bottom of the Analyze data view that will populate after the data has been analyzed, there should be a button which simply says Clear data. When the user clicks this button, all of the input fields should clear from the program as well as the output. Display a  Warning pop up after the user clicks this button and before the data is removed from the UI. The pop up is a confirmation box. The pop up text can say Warning. Clicking OK will clear all the data that the app has produced. If the user clicks OK, the clearing process goes ahead. If the user clicks on cancel, it's canceled and the UI remains as it was before. 

Here are some additional instructions for UI elements:

The app should have the title Sustainability Report Document Parsing Tool. 

Beneath that, there should be a paragraph that says how this works. 

That should say, this tool is a tool for extracting greenhouse gas emission sustainability data from textual sustainability reports.

The tool supports upload as docx or pdf formats. 

Other formats are not supported at this time.

Next there should be an accordion element drop down that says detailed using instructions.

Upload your sustainability report by dragging and dropping it into the app.

After doing this, the program will analyze the document for any GHG reporting data across scopes 1, 2, and 3. 

It will provide the detected parameters as both their values, and it will also provide details about where it encountered these in the test. 

Additionally, there will be a field of CSV data enabling you to copy this data and use it in your own data analysis workflows. 

Disclaimer, this app was both AI generated and utilizes AI. 

Therefore, the accuracy of the calculations cannot be guaranteed, and it's recommended that you verify the calculations.

# Reformatted output

## Prompt

Your task is to take this detailed code generation prompt, which I wrote for a large language model and reformat it for clarity, adding in the missing headings, organizing the content better, but you must not remove any of the instructions at all. 

## LLM-Optimised Prompt

The following prompt contains a detailed set of instructions for generating a Streamlit application. Your task is to generate the entire application. If possible, format this as a single Python file enclosed within a code fence that the user can copy and paste into an IDE. 

Instructions:

## Sustainability Report Document Parsing Tool

### **Overview**

This tool is designed to extract greenhouse gas (GHG) emissions data from sustainability reports in textual formats. It supports PDF and DOCX uploads and provides detailed analysis of Scope 1, Scope 2, and Scope 3 emissions, along with their units. The app also computes aggregated values, monetized emissions, and outputs the data in a CSV format.

---

### **How This Works**

This tool extracts GHG emission data from sustainability reports. It supports uploads in DOCX or PDF formats. Other formats are not supported at this time.

---

### **Detailed User Instructions**

- **Uploading Your Report**: Drag and drop your sustainability report into the app.
- **Data Analysis**: The program will analyze the document for GHG reporting data across Scopes 1, 2, and 3.
  - It will extract numeric values and their reporting units.
  - It will provide details about where these values were found in the document (e.g., page numbers and quotes).
- **CSV Data**: A CSV output will be generated for easy integration into your data analysis workflows.
- **Disclaimer**: This app uses AI for its calculations. Accuracy cannot be guaranteed; please verify the results.

---

### **App Features**

#### **File Upload**
- **Supported Formats**: Only PDF or DOCX files are accepted.
- **Drag-and-Drop Interface**: Users can upload files by dragging them into the designated area.
- **Error Handling**: If unsupported formats (e.g., CSV or XLSX) are uploaded, an error message will inform users that only documents are accepted.

#### **Data Extraction**
The app extracts the following information:
1. **Scope 1 Emissions**
   - Numeric value
   - Reporting unit
2. **Scope 2 Emissions**
   - Numeric value
   - Reporting unit
3. **Scope 3 Emissions**
   - Numeric value
   - Reporting unit

#### **Parsing Rules**
- If multiple tables provide data (e.g., equity basis vs. operating basis), select values from the operating basis table.
- For Scope 2 emissions:
  - If both market basis and location basis are reported, choose location basis.
- For Scope 3 emissions:
  - Extract total Scope 3 emissions if multiple bases are reported.
- If any scope is missing:
  - Note it as `0` in the output.
  - Add a note explaining that the scope was not included in the report.
- If Scopes 1 and 2 are grouped together:
  - Report the total as Scope 2 emissions.
  - Set Scope 1 to `0` and include a note about this reporting method.

#### **Output Details**
1. **Parsed Data Section**
   - For each scope (1, 2, and 3):
     - Provide extracted numeric values and units.
     - Include a description of where the data was found (page number and quote).
2. **All Scopes Reporting**
   - Compute total GHG emissions by summing Scopes 1, 2, and 3 using consistent units.
   - Label this as "Total All Scopes GHG Emissions."
3. **Monetized GHG Emissions**
   - Monetize total emissions at $236 per ton of CO₂ equivalents:
     - For millions of tons: Multiply by $$236 \times 10^6$$.
     - For tons: Multiply by $$236$$.
   - Express results in billions of dollars (rounded to two decimal places).
4. **CSV Data Section**
   - Provide a header row with all parameters discussed.
   - Include a pre-populated data row with computed values.
   - Allow users to edit data inline while maintaining strict CSV formatting.

#### **Clear Data Functionality**
- A "Clear Data" button is provided at the bottom of the output view.
- Clicking this button clears all input fields and output data.
- A confirmation pop-up warns users before clearing:
  - Text: *"Warning: Clicking OK will clear all the data that the app has produced."*
  - Options: OK (proceed) or Cancel (abort).

---

### **UI Design**

#### Title
**Sustainability Report Document Parsing Tool**

#### Instructions
A paragraph below the title explains how this works:
*"This tool is a tool for extracting greenhouse gas emission sustainability data from textual sustainability reports. The tool supports upload as DOCX or PDF formats. Other formats are not supported at this time."*

#### Accordion Element
An expandable section titled "Detailed Using Instructions" provides step-by-step guidance:
1. Upload your sustainability report by dragging and dropping it into the app.
2. The program analyzes the document for GHG reporting data across Scopes 1, 2, and 3.
3. Outputs include detected parameters, their values, details about where they were found in the text, and CSV-formatted data for further analysis.

#### Disclaimer
*"Disclaimer: This app was both AI-generated and utilizes AI. Therefore, the accuracy of the calculations cannot be guaranteed, and it's recommended that you verify the calculations."*

