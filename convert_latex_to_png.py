import subprocess
import time
import os
import re

def sanitize_latex(latex_str):
    # Replace Unicode π with LaTeX \pi using regular expression
    latex_str = re.sub(r'Ï€', r'\\pi ', latex_str)
    latex_str = re.sub(r'Îµ', r'\\epsilon', latex_str)
    latex_str = re.sub(r'Ã—', r'\\times', latex_str)

    # Fix incorrect math mode usage
    latex_str = re.sub(r'(?<!\\)\$', r'\\$', latex_str)  # Escape $ not preceded by \
    latex_str = re.sub(r'(?<!\\)\[', r'\\[', latex_str)  # Escape [ not preceded by \
    latex_str = re.sub(r'(?<!\\)\]', r'\\]', latex_str)  # Escape ] not preceded by \

    # Fix unsupported commands
    latex_str = re.sub(r'\\text\{([^}]*)\}', r'\\mathrm{\1}', latex_str)  # Replace \text{} with \mathrm{}

    return latex_str

# Example usage:
input_latex = r"Back: \( = \frac{e^2}{4m} \frac{32π^2\hbar^2}{ε_0^2} = 2.17 × 10^{-18} \, \text{J} = 13.6 \, \text{eV} \) (6.12)  Comment: Energy required to ionize a hydrogen atom from its ground state."
sanitized_latex = sanitize_latex(input_latex)
print(sanitized_latex)








def convert_latex_to_png(raw_latex_str):

    resolution_dpi = 300  # resolution in DPI

    # Define LaTeX code with white background and modified font size
    width_cm = 7.5  # width in centimeters
    height_cm = 7.5  # height in centimeters

    # Convert dimensions from centimeters to inches
    width_in = width_cm / 2.54  # 1 inch = 2.54 centimeters
    height_in = height_cm / 2.54

    # Convert dimensions from inches to points
    width_pt = width_in * 72.27  # 1 inch = 72.27 points
    height_pt = height_in * 72.27


    latex_str = sanitize_latex(raw_latex_str)
    print("the input string is " + latex_str + "ØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØØ")
    
    # Use the dimensions in LaTeX code
    latex_code = r"""
\documentclass{article}
\usepackage[utf8]{inputenc} % Specify UTF-8 encoding
\usepackage[T1]{fontenc} % Specify font encoding
\usepackage{amsmath}
\usepackage{lmodern} % Latin Modern font which supports Greek letters
\usepackage[paperwidth=""" + str(width_pt) + r"pt, paperheight=" + str(height_pt) + "pt]{geometry}" + r"""
\usepackage{xcolor} % Required for colors
\begin{document}
\pagecolor{white} % Set page background color to white
\centering
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
    # Convert PDF to PNG using ImageMagick with specified resolution
    convert_process = subprocess.run(["magick", "convert", "-density", str(resolution_dpi), "output.pdf", "-quality", "100", "output.png"])
    if convert_process.returncode != 0:
        print("Error occurred during PDF to PNG conversion.")
        exit(1)

    # Check if PNG file was created
    if not os.path.exists("output.png"):
        print("PNG file was not created.")
        exit(1)

    # Open the resulting PNG file with the default application
    # subprocess.run(["start", "output.png"], shell=True)
    return "output.png"



#latex_str = "Reduced Planck constant: $\hbar$"

# Open the resulting PNG file with the default application
#subprocess.run(["start", convert_latex_to_png(latex_str)], shell=True)