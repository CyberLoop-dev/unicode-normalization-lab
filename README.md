<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:14b8a6&height=145&section=header&text=Unicode%20Normalization%20Lab&fontColor=ffffff&fontSize=32" alt="Animated header"/>
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&pause=900&center=true&vCenter=true&width=620&lines=Unicode%20Normalization%20Lab;Compare%20NFC%20and%20NFKC" alt="Typing title"/>

[![License](https://img.shields.io/github/license/CyberLoop-dev/unicode-normalization-lab?label=MIT)](LICENSE)
![Language](https://img.shields.io/github/languages/top/CyberLoop-dev/unicode-normalization-lab)
![Stars](https://img.shields.io/github/stars/CyberLoop-dev/unicode-normalization-lab?style=social)
![Last commit](https://img.shields.io/github/last-commit/CyberLoop-dev/unicode-normalization-lab)

<img src="./assets/mark.svg" width="145" alt="Custom SVG illustration"/>

**Compare Unicode normalization forms and inspect their resulting code points.**

</div>

## ✨ Overview

A local Unicode workbench powered by Python's built-in Unicode database module. It helps explain canonical and compatibility normalization.

## 🚀 Features

- 🔤 Compares NFC, NFD, NFKC, and NFKD.
- 🧭 Shows code points, Unicode names, and categories.
- 🧪 Highlights whether each form changes the input.
- 🔒 Processes text locally without network access.

## 🧪 Demo

```bash
python main.py 'é'
python main.py 'ﬃ' --form NFKC
```

## ⚡ Quick Start

```bash
git clone https://github.com/CyberLoop-dev/unicode-normalization-lab.git
cd unicode-normalization-lab
python main.py 'é'
```

## 🧰 Tech Stack

Python 3.10+ · Standard library only.

## 🗂️ Folder Structure

```text
unicode-normalization-lab/
├── main.py
├── tests/test_main.py
├── requirements.txt
├── .github/workflows/tests.yml
└── assets/mark.svg
```

## 🗺️ Roadmap

- [x] Four standard normalization forms
- [x] Code-point inspection and tests
- [ ] Side-by-side visual character diff
- [ ] Text-file batch mode

## 🤝 Contributing

Add examples that demonstrate a specific Unicode normalization behavior and include expected output in tests.

## 📄 License

MIT — see [LICENSE](LICENSE).

<div align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:14b8a6,100:0f172a&height=100&section=footer" alt="Animated footer"/></div>
