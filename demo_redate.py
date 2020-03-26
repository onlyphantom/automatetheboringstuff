import shutil, os, re
DIR = os.path.abspath('usdates')

datePattern = re.compile(r"""^(.*?) # optional text before the date
            ((0|1)?\d)-             # one or two digits for the month
            ((0|1|2|3)?\d)-         # one or two digits for the day 
            ((19|20)\d\d)           # four digits for the year
            (.*?)$                  # optional text after the date
            """, re.VERBOSE
)

for f in os.listdir('usdates'):
    mo = datePattern.search(f)
    if mo is not None:
        beforeDate = mo.group(1)
        monthP = mo.group(2)
        dayP = mo.group(4)
        yearP = mo.group(6)
        afterDate = mo.group(8)
        
        oldFileName = os.path.join(DIR, f)
        newFileName = os.path.join(DIR, f'{beforeDate}{yearP}-{monthP}-{dayP}{afterDate}')
        shutil.move(oldFileName, newFileName)
