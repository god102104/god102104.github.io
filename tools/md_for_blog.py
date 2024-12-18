from pathlib import Path
from datetime import datetime
import shutil

input_dir = 'C:/Users/user/Documents/god102104/Study/Leetcode/CPP'
out_dir = Path('C:/Users/user/Desktop/god102104.github.io/_posts/temp')
md_paths = Path(input_dir).rglob("*.md")
#2024-12-17-2
now = datetime.now()



for md_path in md_paths:
    new_md_path = out_dir/f'{now.year}-{now.month}-{now.day}-{md_path.name}'
    with open(md_path, mode='r') as original_file:
        with open(new_md_path,mode = 'w') as file:
            tempstring = md_path.stem.replace(" ","-").lower()
            
            description_page = tempstring[tempstring.find('.')+2:] if '.' in tempstring else ""
            header = \
f"""
---
layout: post
title: {md_path.name}
category: leetcode
date: {now.year}-{now.month}-{now.day} {now.strftime("%H:%M:%S")} +0900
description: https://leetcode.com/problems/{description_page}/description/
img: leetcode.png # Add image post (optional)
fig-caption: # Add figcaption (optional)

---

            """
            file.write(header)
            file.write('\n')
            data = original_file.read()
            file.write(data)
            
        