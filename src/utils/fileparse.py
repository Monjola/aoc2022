
def file_rows_to_list(file:str):
    with open(file,'r') as f:
        listl=[]
        for line in f:
            strip_lines=line.strip()
            listl.append(strip_lines)
        return listl

def list_of_strs_to_ints(list_: list[str]) -> list[int]:
    for i,val in enumerate(list_):
        if val == '':
            list_[i] = 0
        else:
            list_[i] = int(val)
    return list_
