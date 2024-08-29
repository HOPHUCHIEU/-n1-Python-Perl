from docxtpl import DocxTemplate

doc = DocxTemplate("invoice_template.docx")

invoice_list = [[2, "pen", 0.5, 1],
                [3, "pencil", 0.25, 2],
                [4, "eraser", 0.75, 3],
                [5, "ruler", 1.00, 4]]

doc.render({"name":"pandora",
            "phone":"999999999",
            "invoice_list": invoice_list,
            "subtotal": 10,
            "salestax":"10%",
            "total":9})


doc.save("new_invoice.docx")