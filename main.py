import re
from unidecode import unidecode
from dotenv import load_dotenv
import os
import pdfrw
import database



def modify_text(text):
    ''' modify text to pdf format and  return text  as a string '''
    pattern =  r"\((.*?)\)"
    result = re.search(pattern, text).group(1)
    result = unidecode(result).replace(' ', '_')
    return result


def radio_button(fields, value):
    ''' update the radio button field value to the given value and   return the new value '''
    for each in fields['/Kids']:
        keys = each['/AP']['/N'].keys()
        keys.remove('/Off')
        export = keys[0]

        if f'/{value}' == export:
            val_str = pdfrw.objects.pdfname.BasePdfName(f'/{value}')
        else:
            val_str = pdfrw.objects.pdfname.BasePdfName('/Off')
        each.update(pdfrw.PdfDict(AS=val_str))

    fields.update(pdfrw.PdfDict(V=pdfrw.objects.pdfname.BasePdfName(f'/{value}')))


def checkbox(fields, value):
    ''' Check box field value '''
    val_str = pdfrw.objects.pdfname.BasePdfName(f'/{value}')
    fields.update(pdfrw.PdfDict(V=val_str,AS=val_str))


def create_form_pdf(pdf_file, values: dict):
    '''Create form with data from database  and return a pdf file'''
    if '/AcroForm' in pdf_file['/Root'] and \
            isinstance(pdf_file['/Root']['/AcroForm'], dict):
        fields = pdf_file['/Root']['/AcroForm']['/Fields']
        for field in fields:
            value = values[modify_text(field['/T'])]
            if field['/F'] == '4' and field.get('/FT') == '/Btn' :
                checkbox(field,value)
            elif '/Kids' in field:
                field.update(pdfrw.PdfDict(V=f'/{value}', AP=f'/{value}'))
                radio_button(field, value)
            else:
                field.update(pdfrw.PdfDict(V=value, AP=value))

        # save the form
        pdfrw.PdfWriter().write(f'report_{values["id"]}.pdf', pdf_file)


def check_environment_variables() -> bool:
    ''' check that environment variables are loaded '''
    envs = ["DATABASE_HOST", "DATABASE_NAME", "DATABASE_USERNAME", "DATABASE_PASSWORD", "FILENAME"]
    # Check if each variable is defined
    for env in envs:
        if os.getenv(env) is None:
            print(f"The environment variable {env} is not set.")
            return False
    return True

def main():
    '''fill out form with data from database'''
    load_dotenv()
    
    if not check_environment_variables():
        return  

    pdf_file = pdfrw.PdfReader(os.getenv("FILENAME"))
    db_mysql = database.Database(
                                os.getenv('DATABASE_HOST'),
                                os.getenv('DATABASE_USERNAME'), 
                                os.getenv('DATABASE_PASSWORD'), 
                                os.getenv('DATABASE_NAME'))

    forms = database.Forms(db_mysql).get_forms()
    for form in forms:
        create_form_pdf(pdf_file, form)


if __name__ == '__main__':
    main()