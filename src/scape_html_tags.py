#$<
def scape_html_tags(code):
    code = code.replace('<','&lt;')
    code = code.replace('>','&gt;')
#    code = code.replace('\>','&gt;') # Comentar a linha de cima
    return code

#return scape_html_tags($GEDIT_SELECTED_TEXT)
#>

