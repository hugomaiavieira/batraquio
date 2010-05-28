$<
import re
global white_spaces
white_spaces = ''
regex=re.compile(r'(?P<white_spaces\>\s*)(def[ ]+)?(?P<method\>[ \w]+\w)\t*(\((?P<params\>.*)\))?:?')
regex=regex.match($GEDIT_CURRENT_LINE)
if regex:
    dictionary=regex.groupdict()
    method=dictionary['method'].replace(' ','_')
    white_spaces=dictionary['white_spaces']
    params= dictionary['params'] and dictionary['params'] or 'self'
    if dictionary['params']:
        if not dictionary['params'].count('self'):
            params = 'self, ' + dictionary['params']
    else:
        params = 'self'
    result = white_spaces + 'def ' + method + '(' + params + '):'
else:
    result = $GEDIT_CURRENT_LINE
return result
>
	$<return white_spaces>

