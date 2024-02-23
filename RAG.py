import PyPDF2

class ResumeAnalyzer:
    def __init__(self, pdf_path):
        self.resume_text = self.read_resume_pdf(pdf_path)
    
    def read_resume_pdf(self, pdf_path):
        """
        Reads text content from a PDF resume file.

        Args:
        pdf_path (str): The path to the PDF file.

        Returns:
        str: The extracted text content from the PDF.
        """
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ''
            for page in reader.pages:
                text += page.extract_text()
        return text

    def retrieve_information(self, query):
        """
        Retrieves relevant information categories from resume text based on a given query.

        Args:
        query (str): The query string used to search for relevant information.

        Returns:
        list: A list of tuples containing relevant information categories and keywords.
        """
        # Define keywords for each category of information
        keywords = {
            "contact": ["contact", "phone", "email", "address", "linkedin"],
            "education": ["education", "Bachelor Of Arts", "History", "magna cum laude", "RIVER BROOK UNIVERSITY"],
            "key skills": ["key skills", "Microsoft Office", "Spanish", "English", "typing speed", "Problem solving", "Team leadership"],
            "awards": ["awards", "AWARD TITLE", "Administrative Assistant", "B.A. in History", "Microsoft Excel"],
            "professional experience": ["professional experience", "Administrative Assistant", "REDFORD & SONS", "SECRETARY", "BRIGHT SPOT LTD", "SUNTRUST FINANCIAL"]
        }
        
        # Convert the query to lowercase for case insensitivity
        query = query.lower()
        relevant_info = []

        # Search for keywords in the resume text and extract relevant information
        for category, category_keywords in keywords.items():
            for keyword in category_keywords:
                if keyword.lower() in self.resume_text.lower() and query in keyword.lower():
                    relevant_info.append((category.capitalize(), keyword))
                    break

        return relevant_info

    def generate_response(self, retrieved_info):
        """
        Generates a response based on retrieved information from the resume.

        Args:
        retrieved_info (list): A list of tuples containing relevant information categories and keywords.

        Returns:
        str: The response message containing the retrieved information or a notification if no relevant information is found.
        """
        response = ""
        if not retrieved_info:
            response = "No relevant information found."
        else:
            response = "Relevant Information:\n"
            for category, keyword in retrieved_info:
                response += f"{category}: {keyword}\n"
        return response

if __name__ == "__main__":
    # Specify the full path to your resume PDF file
    pdf_path = r'C:\Users\AYUSH NATH TIWARI\Downloads\61eea70f164bb4.82895381.pdf'
    resume_analyzer = ResumeAnalyzer(pdf_path)
    
    # Print the extracted resume text for debugging purposes
    print("Resume Text:")
    print(resume_analyzer.resume_text)
    
    # Handle user queries
    while True:
        query = input("Enter your query (type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        # Retrieve relevant information based on the user query
        retrieved_info = resume_analyzer.retrieve_information(query)
        # Generate a response based on the retrieved information
        response = resume_analyzer.generate_response(retrieved_info)
        print(response)
