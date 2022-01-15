import glob

files = glob.glob('.' + '/**/*.md', recursive=True)
for file in files:
    line_index = 0
    cnt=0
    lines = None
    key_value = None
    url_val = ""
    is_slash_present = False
    with open(file, 'r') as file_handler:
        lines = file_handler.readlines()
    metadata_tags = 0
    no_edit_needed = False
    for line in lines:
        cnt+=1
        if metadata_tags == 2:
            break
        if(line.find("---")!=-1):
            metadata_tags+=1
        if(line.find("redirect")!=-1):
            no_edit_needed = True
        if(line.find("permalink")!=-1):
            line_index = cnt
            if(line[-2] == '/'):
                is_slash_present = True
            key_value = line.split(':')
            url_val = key_value[1]

    url_val = url_val.strip()
    if(is_slash_present == False):
        url_val+='/'
    if no_edit_needed ==  False:

        lines.insert(line_index,'redirect_from: '+ url_val+'\n')

        with open(file , 'w') as file_handler:
            file_handler.writelines(lines)
