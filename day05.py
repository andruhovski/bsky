import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()
latex_content = "$ \\sqrt{x^2+y^2} $"

latex_fragment = ap.TeXFragment(latex_content)

page.paragraphs.add(latex_fragment)
document.save("latex_fragment.pdf")