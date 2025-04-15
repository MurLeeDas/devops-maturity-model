"""
Generate PDF reports from assessment results using ReportLab.
"""
import datetime
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch

def generate_pdf_report(results, answers, questions, phases):
    """Generate a PDF report using ReportLab."""
    # Create filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"DevOps_Maturity_Report_{timestamp}.pdf"
    
    # Create document
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Modify existing styles instead of creating new ones
    title_style = styles['Title']
    title_style.alignment = 1  # Center alignment
    
    heading2_style = styles['Heading2']
    heading2_style.spaceBefore = 12
    heading2_style.spaceAfter = 6
    
    heading3_style = styles['Heading3']
    heading3_style.spaceBefore = 10
    heading3_style.spaceAfter = 5
    
    # Build content
    elements = []
    
    # Title
    elements.append(Paragraph("DevOps Maturity Assessment Report", title_style))
    elements.append(Spacer(1, 0.25*inch))
    
    # Date
    today = datetime.datetime.now().strftime("%B %d, %Y")
    elements.append(Paragraph(f"Generated on: {today}", styles['Normal']))
    elements.append(Spacer(1, 0.25*inch))
    
    # Overall Results
    elements.append(Paragraph("Overall Maturity Assessment Results", heading2_style))
    
    overall_level = results["overall_level"]
    percentage = results["percentage"]
    elements.append(Paragraph(f"Your overall DevOps maturity level is: {overall_level}/5 ({percentage:.1f}%)", styles['Normal']))
    elements.append(Spacer(1, 0.2*inch))
    
    # Section scores
    elements.append(Paragraph("Section Scores", heading2_style))
    
    # Create a table for section scores
    section_data = [["Section", "Score"]]
    for section, score in results["section_scores"].items():
        section_data.append([section, f"{score:.1f}/5"])
    
    section_table = Table(section_data, colWidths=[4*inch, 1*inch])
    section_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    
    elements.append(section_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Recommendations by phase
    elements.append(Paragraph("Improvement Roadmap", heading2_style))
    
    # For each phase
    for phase_name, recommendations in phases.items():
        if recommendations:
            elements.append(Paragraph(f"Phase: {phase_name}", heading3_style))
            
            for i, rec in enumerate(recommendations, 1):
                # Title with priority
                elements.append(Paragraph(f"{i}. {rec['title']} (Priority: {rec['priority']})", heading3_style))
                
                # Details
                elements.append(Paragraph(rec["details"], styles['Normal']))
                
                # Recommended actions header
                elements.append(Paragraph("Recommended Actions:", styles['BodyText']))
                
                # Actions as a bulleted list
                for action in rec["actions"]:
                    elements.append(Paragraph(f"• {action}", styles['BodyText']))
                
                elements.append(Spacer(1, 0.2*inch))
    
    # Build the PDF
    doc.build(elements)
    
    return filename