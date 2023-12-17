import json


def values_list(values):
    with open(values, mode='r', encoding='utf-8') as srcfl:
        data = json.load(srcfl)
        out_value = [i['value'] for i in data['values']]
        out_id = [i['id'] for i in data['values']]
    
        lst = {key: value for key, value in zip(out_id, out_value)}
    
    return lst    
      
    
def val_record(tests, lst):   
    with open(tests, mode='r', encoding='utf-8') as outfl:
        data = json.load(outfl)
        report_lst = []
    
        for el in data['tests']:
            for j in lst:
                if j == el['id']:
                    el['value'] = lst[j]
            # ---------------------------
            for j in el:
                if j == 'values':
                    for x in el[j]:
                        for j in lst:
                            if j == x['id']:
                                x['value'] = lst[j]
                        # -----------------------------
                        for z in x:
                            if z == 'values':
                                for s in x[z]:
                                    for j in lst:
                                        if j == s['id']:
                                            s['value'] = lst[j]
                                    # ---------------------------
                                    for n in s:
                                        if n == 'values':
                                            for b in s[n]:
                                                for j in lst:
                                                    if j == b['id']:
                                                        b['value'] = lst[j]

            report_lst.append(el)
    
    return report_lst
        

def w_report(report_lst):        
    with open('report.json', mode='w', encoding='utf-8') as outfl2:
        for i in report_lst:
            json.dump(i, outfl2, sort_keys=True, indent=4)
           



values = values_list(input('файл values: '))
val_rec = val_record(input('Файл tests: '), values)
report_write = w_report(val_rec)

      













