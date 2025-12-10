from fpdf import FPDF

name = input("Write a name: ")
i = f"{name} took CS50"

#A PDF is created as a portrait format and A4 sheet size.
pdf = FPDF(orientation="P", format="A4")

#The page is created where the shirt will be put.
pdf.add_page()

#The shirt is manually centered on the page.
pdf.image("shirtificate.png", x=10, y=60, w=190)

#The font and size of the header text is set.
pdf.set_font("Times", size=36)
#The header text is automatically centered.
pdf.cell(text="CS50 Shirtificate", align="C", center=True)


#The font and size of the shirt text is set.
pdf.set_font("Times", size=30)
#Shirt text color is set as white.
pdf.set_text_color(255, 255, 255)
#The vertical position of the shirt text is set.
pdf.set_y(120)
#The shirt text is automatically centered.
pdf.cell(text=i, align="C", center=True)

#The shirt pdf is created.
pdf.output("shirtificate.pdf")
