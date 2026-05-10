import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

rotations = [0, 45, 90, 135, 180, 270]
y_position = 700

for angle in rotations:
    text = ap.text.TextFragment(f"Rotated text at {angle} degrees")
    text.position = ap.text.Position(120, y_position)
    text.text_state.font = ap.text.FontRepository.find_font("Arial")
    text.text_state.font_size = 14
    text.text_state.foreground_color = ap.Color.blue
    text.text_state.rotation = angle

    page.paragraphs.add(text)
    y_position -= 80

styled_text = ap.text.TextFragment("Styled Rotated Text")
styled_text.position = ap.text.Position(400, 400)
styled_text.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
styled_text.text_state.font_size = 18
styled_text.text_state.font_style = ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
styled_text.text_state.foreground_color = ap.Color.red
styled_text.text_state.rotation = 315

page.paragraphs.add(styled_text)

document.save("day12.pdf")