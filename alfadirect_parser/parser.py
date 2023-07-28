# -*- coding: utf-8 -*-
import pandas as pd

from xml.etree.ElementTree import parse
doc = parse('/tmp/alfa.xml').getroot()

all_items = []

for i in doc.iter('{TaxAppendix}Details'):
  all_items.append(i.attrib)

xmlToDf = pd.DataFrame(all_items)

# как правльно загрузить кириллицу в маковский эксель?
#xmlToDf.to_csv('/tmp/alfa.csv',encoding='utf-8',index=False)
xmlToDf.to_excel('/tmp/alfa.xlsx')