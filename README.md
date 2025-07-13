# -AUTOMATED-REPORT-GENERATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: DINESH

*INTERN ID*: CT04DH1263

*DOMAIN*: PYTHON

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

# TASK DESCRPTION

The objective of this task was to develop a complete Python-based solution that reads data from a file, performs basic data analysis, and generates a structured PDF report. The task involved multiple stages, including data collection, preprocessing, analysis, and automated report generation using appropriate Python libraries. The final output is a professional-looking PDF file summarizing the analyzed results in a clear and organized format.

To begin with, the data source used for this project was a CSV (Comma-Separated Values) file named data.csv, which contained a simple dataset of student names and their corresponding scores. This format was chosen for its simplicity and compatibility with data analysis tools. The CSV file was created and saved in the same working directory as the script to ensure easy access and seamless integration during file reading.

The next step was to use the pandas library, a powerful tool in Python for data manipulation and analysis. Using pandas, the script successfully read the contents of the CSV file into a DataFrame. Basic data cleaning was performed, such as stripping any extra spaces in column headers and dropping rows with missing values to avoid errors during analysis. After this, a few key statistical calculations were performed, including determining the average score, the highest score along with the student who achieved it, and the lowest score along with the corresponding student. These calculations provided a quick summary of the dataset.

Once the analysis was complete, the next challenge was to present the findings in a readable and visually appealing format. For this, the FPDF library was used, which allows for programmatic creation of PDF files in Python. A custom PDF class was defined to handle the structure and layout of the report. It included a header with a title, a footer with the page number, and methods to add a summary of the analysis as well as a table of the original data. All text was carefully formatted using different fonts, sizes, and alignments to maintain clarity and a professional look.

The summary section of the report included the calculated statistics: the average score, the highest and lowest scores, and the names of the students associated with those values. Following the summary, a table was generated that listed each student and their corresponding score. Special attention was given to data type conversion to ensure that all values passed to the PDF were strings, preventing any runtime errors.

Finally, the script generated the PDF file and saved it with the name sample_report.pdf in the working directory. A confirmation message was printed to indicate successful completion. This task showcases a practical use of Python for automating repetitive documentation tasks, particularly in fields like education, HR, and business reporting.

The overall project demonstrated how to integrate file handling, data analysis, and report generation into a single automated workflow. It can be further enhanced with additional features such as charts, logos, timestamping, or integration with email services for automatic distribution of reports.

# OUTPUT

*(1)*


<img width="1913" height="1013" alt="Image" src="https://github.com/user-attachments/assets/2e9c5ba3-a533-4b8f-af1c-84f6b67ea701" />

*(2)*



<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/e96dfb80-942f-476e-a029-03facc3b7a78" />

*(3)*



<img width="867" height="593" alt="Image" src="https://github.com/user-attachments/assets/6d223761-9cdf-4af0-9c9d-c1fb2c0d632c" />
