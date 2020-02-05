
## Prerequisite

```
pip install pefile
```

---
## Installation

```
pip install git+https://github.com/ohjeongwook/petool
```

---
## Update

```
pip install git+https://github.com/ohjeongwook/petool --upgrade
```

---
## PYTHONPATH

```
python %PYTHONHOME%\Lib\site-packages\petool\petool.py
```

---
## Use Case

---
### Fixing Sections

* After dumping PE image from process, you can use petool to fix sections.

```
python -m petool.petool -c fix <input> <output>
```
