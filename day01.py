import os
import aspose.pdf as ap


# Global configuration

DATA_DIR = "E:\\Samples\\Text"

def add_text_simple_case(outfile):
    """
    Add simple text to a PDF document.
    Creates a new PDF document with a single page and adds a text fragment
    "Hello, World!" at position (100, 600) on the page.
    Args:
        outfile (str): The file path where the generated PDF document will be saved.
    Returns:
        None: The function saves the document to the specified output file.
    Example:
        >>> add_text_simple_case("output.pdf")
        # Creates a PDF file named "output.pdf" with "Hello, Aspose!" text
    """

    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 700)

    page.paragraphs.add(text_fragment)
    document.save(outfile)


