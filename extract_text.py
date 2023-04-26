import  re

"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+   extract german text                                     +
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

with open('The_Dark_Knight_German.srt') as read_file:
    content = read_file.read()   # read main file

    result = ' '

    while result:
        # use regex to detect test
        delete_text = '[0-9]([0-9]?)([0-9]?)([0-9]?)\n[0-9][0-9]\D[0-9][0-9]\D[0-9][0-9],[0-9][0-9][0-9]\s-->\s[0-9][0-9]\D[0-9][0-9]\D[0-9][0-9],[0-9][0-9][0-9]\n'
        result = re.search(delete_text, content)

        if result:
            text = result.group(0)
            # delete the founded text
            new_content = content.replace(text, '')

            # modify content for the next search
            content = new_content
            # print(text)



with open('german.txt', 'w') as f:
    f.write(content)




