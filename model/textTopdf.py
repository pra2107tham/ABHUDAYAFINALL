import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def text_to_pdf(folder_path, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    width, height = letter
    y_position = height - 40  # Start position for text

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                c.setFont("Helvetica", 12)
                c.drawString(30, y_position, f"--- {filename} ---")  # File title
                y_position -= 20  # Space after filename

                for line in lines:
                    if y_position < 40:  # Create a new page if out of space
                        c.showPage()
                        c.setFont("Helvetica", 12)
                        y_position = height - 40
                    c.drawString(30, y_position, line.strip())
                    y_position -= 15

                y_position -= 20  # Extra space after each file

    c.save()
    print(f"PDF saved as {output_pdf}")

# Example usage
folder_path = "dataset_soham"
output_pdf = "output.pdf"
text_to_pdf(folder_path, output_pdf)
