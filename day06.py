import aspose.pdf as ap

document = ap.Document()
page = document.pages.add()



document.save("latex_fragment.pdf")