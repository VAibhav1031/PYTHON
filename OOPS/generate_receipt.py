from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch

def generate_receipt(filename, items, total):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    # Add title
    data = [["RECEIPT"]]
    table = Table(data, colWidths=[6*inch])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 16),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
    ]))
    elements.append(table)

    # Add items
    data = [["Item", "Price"]] + items + [["Total", f"${total:.2f}"]]
    table = Table(data, colWidths=[4*inch, 2*inch])
    table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('BACKGROUND', (0, -1), (-1, -1), colors.lightgrey),
    ]))
    elements.append(table)

    # Build the PDF
    doc.build(elements)

# Example usage
items = [
    ["Item 1", "$10.00"],
    ["Item 2", "$15.00"],
    ["Item 3", "$5.50"],
]
total = sum(float(item[1].replace('$', '')) for item in items)

generate_receipt("receipt.pdf", items, total)