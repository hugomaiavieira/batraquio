#$<
def scape_html_tags(code):
    return code.replace('<','&lt;').replace('>','&gt;')
#    return code.replace('<','&lt;').replace('\>','&gt;') # Comentar a linha de cima

#return scape_html_tags($GEDIT_SELECTED_TEXT)
#>

