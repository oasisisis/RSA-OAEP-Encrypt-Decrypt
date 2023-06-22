# RSA-OAEP-Encrypt-Decrypt
南京邮电大学 -《信息安全综合实验》- RSA-OAEP 的实现<br>
NJUPT-'Information Security Experiments'- RSA-OAEP<br>

一个图形化的 RSA 加密解密工具<br>
This is a tool to encrypt plaintext into RSA ciphertext and decrypt into raw text.

<img width="568" alt="Screenshot 2023-06-21 at 16 44 03" src="https://github.com/oasisisis/RSA-OAEP-Encrypt-Decrypt/assets/62041306/9327a159-7948-455e-aba8-16e1ba4496aa">



## 环境要求 / What you need to run this software
`Python 3.x`<br>
`PyQt5`


## 如何使用 / How to use
运行 'Main' 文件夹中的 `main.py`<br>
Run `main.py` in 'Main' folder


## Issue
暂时只有中文界面<br>
No multi-language support for now.<br>

推荐在 macOS 运行，Windows 上运行时会缺少一些字体，可自行修改 'Main' 文件夹中名称为 `xxxui.py` 的界面文件，将其中所有的字体名称改为你系统中已经安装的<br>
Missing fonts on windows, so to get better experience it is suggested to run it on macOS.<br>

有时使用程序生成的密钥对进行解密时可能导致程序闪退，重新生成即可<br>
Sometimes the key pair you generate may cause crash in encryping module, please re-generate key pair to avoid this problem.

