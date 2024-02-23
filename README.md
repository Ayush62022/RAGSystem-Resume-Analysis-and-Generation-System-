# RAGSystem-Resume-Analysis-and-Generation-System-
The main goal of this project is to create a system that automatically analyzes resumes to extract important information. This system will help streamline the recruitment process by quickly identifying key details such as contact information, education history, skills, awards, and work experience from resumes submitted in PDF format. Additionally, the system will generate structured responses based on user queries, making it easier for recruiters to access relevant information within the resumes. Ultimately, this project aims to enhance efficiency in the recruitment process by automating the analysis and retrieval of vital information from resumes.

## RAG(Retrieval-Augmentation-Generation)

RAG, or Retrieval-Augmented Generation, enhances AI-generated responses by incorporating external knowledge sources. This approach improves response quality in question answering systems by providing up-to-date information and allowing users to verify claims for accuracy and reliability.

RAG (Retrieval-Augmentation-Generation) is pivotal in this project for its ability to comprehensively analyze resumes, augmenting retrieved data for enhanced relevance, and generating structured responses. This approach ensures accurate information extraction, improves user experience, and accommodates various data formats, maximizing versatility.

## Steps invovled in building RAG model
### 1. Initalize the class:
 First we initalize the class 'ResumeAnalyzer' and import necessary libarary PyPDF2
### 2. Extract Text from PDF Resume:
 The read_resume_pdf method extracts text from a PDF resume file specified by pdf_path. It utilizes PyPDF2 library to read the file, iterating over each page to extract text content. The extracted text is concatenated and returned as a string, facilitating further analysis and processing within the application.
### 3. Retrieve Relevant Information:
   The retrieve_information method identifies and retrieves relevant information categories from a resume text based on a user-provided query. It utilizes predefined keywords associated with different information categories to match and extract relevant data.
   #### Use of Keywords:
Keywords are employed to streamline the process of information retrieval by identifying specific patterns or terms indicative of relevant information categories within the resume text. By defining a set of keywords for each category, the method efficiently matches and extracts pertinent details, enhancing the accuracy and effectiveness of the resume analysis process. This approach enables systematic categorization and organization of information, facilitating further analysis and presentation to users.
### 4.  Generate Response:
   The generate_response method creates a response message based on the retrieved information from the resume. It takes a list of tuples containing relevant information categories and keywords (retrieved_info) as input and generates a formatted response message accordingly.
This method plays a crucial role in presenting the extracted information from the resume in a structured and readable format, facilitating easy comprehension for the user or further processing within the application.
### 5. Resume Analyzer  for the ouput:
   The script serves as an application for analyzing resumes. It utilizes the ResumeAnalyzer class to extract text content from a PDF resume file, retrieve relevant information based on user queries, and generate responses containing the extracted information.
   Execution:

Execute the script.
Enter queries to retrieve specific information from the resume.
The script generates responses based on the extracted information and displays them to the user.
This application simplifies the process of analyzing resumes by providing an interactive interface for querying and retrieving relevant information, enhancing user experience and efficiency in resume evaluation.



!![Screenshot 2024-02-23 120718](https://github.com/Ayush62022/RAGSystem-Resume-Analysis-and-Generation-System-/assets/140695614/cfb850eb-7ecc-48b8-90f9-91b5295860a4)

