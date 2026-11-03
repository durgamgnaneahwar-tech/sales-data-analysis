from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pathlib import Path

out = Path(r'C:\Users\Gnaneshwar\Documents\Codex\2026-11-03\referenced-chatgpt-conversation-this-is-an\outputs\Durgam_Gnaneshwar_Data_Analyst_Resume.pdf')
doc = SimpleDocTemplate(str(out), pagesize=letter, rightMargin=0.62*inch, leftMargin=0.62*inch, topMargin=0.5*inch, bottomMargin=0.48*inch, title='Durgam Gnaneshwar - Data Analyst Resume', author='Durgam Gnaneshwar')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='Name', parent=styles['Title'], fontName='Helvetica-Bold', fontSize=18, leading=21, alignment=TA_CENTER, textColor=colors.HexColor('#18324B'), spaceAfter=3))
styles.add(ParagraphStyle(name='Contact', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=11, alignment=TA_CENTER, textColor=colors.HexColor('#394957'), spaceAfter=6))
styles.add(ParagraphStyle(name='Section', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=10.1, leading=12, textColor=colors.HexColor('#18324B'), spaceBefore=6, spaceAfter=3, keepWithNext=True))
styles.add(ParagraphStyle(name='BodyX', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.3, leading=12.2, textColor=colors.HexColor('#202830'), spaceAfter=2))
styles.add(ParagraphStyle(name='BulletX', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.0, leading=11.5, leftIndent=11, firstLineIndent=-7, bulletIndent=0, textColor=colors.HexColor('#202830'), spaceAfter=1))
styles.add(ParagraphStyle(name='Edu', parent=styles['BodyText'], fontName='Helvetica', fontSize=9.0, leading=11.5, textColor=colors.HexColor('#202830'), spaceAfter=1))

story = []
story.append(Paragraph('DURGAM GNANESHWAR', styles['Name']))
story.append(Paragraph('Hyderabad, Telangana, India&nbsp;&nbsp; | &nbsp;&nbsp;7794982720&nbsp;&nbsp; | &nbsp;&nbsp;durgamgnanwahwar@gmail.com<br/><link href="https://www.linkedin.com/in/gnaneshwar-durgam-1734b9398/" color="#394957">linkedin.com/in/gnaneshwar-durgam-1734b9398</link>', styles['Contact']))
story.append(HRFlowable(width='100%', thickness=0.8, color=colors.HexColor('#8DA2B3'), spaceBefore=0, spaceAfter=2))

def section(title, content):
    story.append(Paragraph(title.upper(), styles['Section']))
    story.extend(content)

section('Professional Summary', [Paragraph('Aspiring Data Analyst and Data Scientist with a B.Tech in Electrical and Electronics Engineering and foundational knowledge of Python and SQL. Interested in data analysis, statistical techniques, data visualization, and machine learning, with a focus on turning data into useful insights for decision-making.', styles['BodyX'])])
section('Technical Skills', [Paragraph('<b>Programming:</b> Python &nbsp; | &nbsp; <b>Database:</b> MySQL, SQL<br/><b>Focus Areas:</b> Data Analysis, Data Science, Statistical Analysis, Data Visualization, Machine Learning', styles['BodyX'])])
section('Projects', [
    KeepTogether([Paragraph('<b>Sales Data Analysis</b>', styles['BodyX']), Paragraph('- Analyzed sales data to identify trends, revenue patterns, and top-performing products using Python and Pandas.<br/>- Used SQL queries to retrieve and summarize sales information, generating insights to support business decisions.', styles['BulletX'])]),
    Spacer(1,2),
    KeepTogether([Paragraph('<b>Student Performance Analysis</b>', styles['BodyX']), Paragraph('- Organized and analyzed student marks using Python and Pandas to understand academic performance trends.<br/>- Applied SQL to calculate average marks and identify top-performing students; summarized patterns in the results.', styles['BulletX'])])
])
section('Education', [
    Paragraph('<b>Bachelor of Technology (B.Tech), Electrical and Electronics Engineering</b><br/>Mother Theressa College of Engineering, Peddapally &nbsp; | &nbsp; 2025<br/>CGPA: 8.8 &nbsp; | &nbsp; Percentage: 69%', styles['Edu']),
    Spacer(1,2), Paragraph('<b>Intermediate (12th Standard)</b> &nbsp; | &nbsp; Marks: 890', styles['Edu'])
])
section('Strengths', [Paragraph('Analytical Thinking &nbsp; | &nbsp; Problem Solving &nbsp; | &nbsp; Quick Learner &nbsp; | &nbsp; Adaptability &nbsp; | &nbsp; Self-Motivated', styles['BodyX'])])

doc.build(story)
print(out)

