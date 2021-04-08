from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


def pdf2txt(in_pdf_file, out_txt_file):

    # open the pdf file to be converted
    in_file = open(in_pdf_file, 'rb')

    # instantiate a variable of PDFResourceManager
    # to store shared resources in pdf file
    res_mgr = PDFResourceManager()

    # instantiate a variable of StringIO()
    # containing retrieved data of pdf file
    ret_data = StringIO()

    # laparams contains parameters to deal with adjusting
    # while getting the content of a pdf file
    la_params = LAParams()

    # a variable of TextConverter taking parameters
    # of PDFResourceManager, retrieved text and layout parameter
    txt_converter = TextConverter(res_mgr, ret_data, laparams=la_params)

    # a variable of PDFPageInterpreter taking parameters
    # of PDFResourceManager and TextConverter
    interpreter = PDFPageInterpreter(res_mgr, txt_converter)

    # process each page in pdf file
    for page in PDFPage.get_pages(in_file):
        interpreter.process_page(page)

    # get final text representation
    txt = ret_data.getvalue()

    # close all resources
    in_file.close()
    ret_data.close()
    txt_converter.close()

    # save output data to a text file
    with open(out_txt_file, 'w') as f:
        f.write(txt)


# main
# input file
in_pdf_file = 'attention-exercise.pdf'

# output file
out_txt_file = 'attention-exercise.txt'

# execute PDFToTXT function
pdf2txt(in_pdf_file, out_txt_file)
