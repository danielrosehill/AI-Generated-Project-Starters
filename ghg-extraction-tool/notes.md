# Use-Case For This Project

  The prompt contained in this output is quite a detailed 1300 word prompt which provides instructions for code generation targeting a program that can convert, parse PDF documents (sustainability reports) and attempt to extract three key variables in them, their greenhouse gas (GHG) emissions reports across scopes 1, 2, and 3. 
  
  The prompt includes instructions for calculations, descriptions for the UI elements, and instructions on variations that the program may expect to encounter in the type of reports that it is being asked to parse. 
  
  The prompt specifies that the LLM should generate a Streamlit app specifically, although this instruction could be easily modified to target a completely different implementation approach.
  
The use case is that many companies report their sustainability performance in long PDF reports. There is a strong public interest in analyzing this data on a cross-sectoral basis which requires aggregating and analysing this data at scale. 

As not every company reports their emissions data in data-native or data friendly formats, this creates some work for those trying to do that. 

# Data Accuracy 

Naturally, anyone using an AI tool such as the one that this prompt proposes to create is going to have concerns about the accuracy of the data extracted. 

For that reason, the prompt contains an instruction for the LLM to provide both the data points that it was able to identify and to provide verbatim quotes from the report where the data was encountered. 

The idea is that a human supervisor (human in the loop) could run this prompt quickly, find the data page referenced, and cross check the information. Even factoring in the time required for this supervision process, this would still probably be a significant time saving over having that same human read the report, search for the data, and find each data point manually.

A variation on this idea that could  be very useful would be adding an additional instruction for the model to convert the section of the text where the GHG emissions data was encountered, highlight it for clear visibility, and display those elements. alongside the data that was output
