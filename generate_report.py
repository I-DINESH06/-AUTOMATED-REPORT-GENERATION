import pandas as pd
from fpdf import FPDF

df = pd.read_csv("data.csv")
df.columns = df.columns.str.strip()
df.dropna(subset=['Name', 'Score'], inplace=True)

average_score = df['Score'].mean()
max_score = df['Score'].max()
min_score = df['Score'].min()
top_scorer = df.loc[df['Score'].idxmax(), 'Name']
lowest_scorer = df.loc[df['Score'].idxmin(), 'Name']

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, 'Student Score Report', ln=True, align='C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def add_summary(self, avg, high, low, top_name, low_name):
        self.set_font('Arial', '', 12)
        self.set_text_color(0, 0, 0)
        self.cell(0, 10, f'Average Score: {avg:.2f}', ln=True)
        self.cell(0, 10, f'Highest Score: {high} by {top_name}', ln=True)
        self.cell(0, 10, f'Lowest Score: {low} by {low_name}', ln=True)
        self.ln(10)

    def add_table(self, data_frame):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(90, 10, "Name", 1, 0, 'C', 1)
        self.cell(90, 10, "Score", 1, 1, 'C', 1)
        self.set_font('Arial', '', 12)

        for i, row in data_frame.iterrows():
            name = str(row['Name'])
            score = str(row['Score'])
            self.cell(90, 10, name, 1)
            self.cell(90, 10, score, 1)
            self.ln()

pdf = PDF()
pdf.add_page()
pdf.add_summary(average_score, max_score, min_score, top_scorer, lowest_scorer)
pdf.add_table(df)
pdf.output("sample_report.pdf")
print("PDF report generated successfully as 'sample_report.pdf'")

