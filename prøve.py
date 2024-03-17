import subprocess
import time
import os

def convert_latex_to_png(latex_str):

    latex_code = r"""
    \documentclass{article}
    \usepackage{amsmath}
    \begin{document}
    """ + latex_str + r"""
    \end{document}
    """


    # Set MAGICK_HOME environment variable
    os.environ['MAGICK_HOME'] = r'C:\Program Files\gs'

    # Write LaTeX code to a .tex file
    with open("output.tex", "w") as f:
        f.write(latex_code)

    # Compile LaTeX code using pdflatex
    latex_process = subprocess.run(["pdflatex", "output.tex"])
    if latex_process.returncode != 0:
        print("Error occurred during LaTeX compilation.")
        exit(1)

    # Check if PDF file was created
    if not os.path.exists("output.pdf"):
        print("PDF file was not created.")
        exit(1)

    # Convert PDF to PNG using ImageMagick's convert command
    convert_process = subprocess.run(["magick", "convert", "-density", "300", "output.pdf", "-quality", "100", "output.png"])
    if convert_process.returncode != 0:
        print("Error occurred during PDF to PNG conversion.")
        exit(1)

    # Check if PNG file was created
    if not os.path.exists("output.png"):
        print("PNG file was not created.")
        exit(1)

    # Open the resulting PNG file with the default application
    subprocess.run(["start", "output.png"], shell=True)

# Example usage
    
latex_str = "Reduced Planck constant: $\hbar$"


convert_latex_to_png(latex_str)
