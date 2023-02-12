import pandas as pd
import xlsxwriter


df = pd.DataFrame({
    'Miesiąc':[1,2,3,4,5,6,7,8,9,10,11,12],
    'Wartość sprzedaży':[2340,2189,8970,5460,3425,7890,1234,2567,6789,5432,9854,6782],
    'Procent':[.04,.08,.11,.16,.28,.18,.24,.31,.09,.1,.4,.14]
})
