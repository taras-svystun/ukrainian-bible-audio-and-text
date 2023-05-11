from striprtf.striprtf import rtf_to_text

filepath = '../text_rtf/nwt_01_Ge_K.rtf'

with open(filepath, 'r', encoding='ISO-8859-1', errors='ignore') as file:
    content = file.readlines()
    text = rtf_to_text(content[0])

print(text[:300])

