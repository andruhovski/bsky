import aspose.pdf as ap
from aspose.pdf.text import TextFragment, FontRepository

document = ap.Document()
page = document.pages.add()

# Create text fragments with different rotation angles
rotations = [0, 45, 90, 135, 180, 270]
y_position = 700

for i, angle in enumerate(rotations):
    text = TextFragment(f"Rotated text at {angle} degrees")
    text.position = ap.text.Position(200, 600)
    text.text_state.font = FontRepository.find_font("Arial")
    text.text_state.font_size = 14
    text.text_state.foreground_color = ap.Color.blue

    # Set rotation angle in degrees
    text.text_state.rotation = angle

    page.paragraphs.add(text)

# Add a more complex example with styled rotated text
styled_text = TextFragment("Styled Rotated Text")
styled_text.position = ap.text.Position(400, 400)
styled_text.text_state.font = FontRepository.find_font("Times New Roman")
styled_text.text_state.font_size = 18
styled_text.text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
styled_text.text_state.foreground_color = ap.Color.red
styled_text.text_state.rotation = 315  # -45 degrees

page.paragraphs.add(styled_text)

document.save("text_rotation.pdf")

    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)