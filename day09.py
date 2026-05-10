import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()

text = (
	"This example shows custom line spacing in a paragraph. "
	"The same fragment can contain enough text to wrap across multiple lines. "
	"That makes the spacing effect easy to see in the output PDF."
)

fragment = ap.text.TextFragment(text)
fragment.text_state.font_size = 12
fragment.text_state.line_spacing = 16

page.paragraphs.add(fragment)
document.save("day09.pdf")
