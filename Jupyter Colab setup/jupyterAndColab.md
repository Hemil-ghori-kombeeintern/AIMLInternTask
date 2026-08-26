# Jupyter_Colab_Quick_Notes

## Install Jupyter

```bash
python --version
pip --version
pip install notebook
jupyter --version

```

## Install Jupyter using conda

```bash
conda install notebook
jupyter notebook

```

## Launch

```bash
jupyter notebook
```

JupyterLab:

```bash
pip install jupyterlab
jupyter lab
```

Stop Jupyter:

```
Ctrl + C
```

## Virtual Environment

Create:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install Jupyter:

```bash
pip install notebook
jupyter notebook
```

Deactivate:

```bash
deactivate
```

## Virtual Environment using conda

Create:

```bash
conda activate
conda list
conda env list
conda create -n <venvname>
conda activate <venvname>
conda deactivate
conda env remove -n <venvname>
```

## Python Cells

```python
print("Hello, World!")

x = 10
y = 20
print(x + y)
```

Run cell:

```
Shift + Enter
```

Install package:

```python
%pip install pandas
```

Run terminal command:

```python
!pip --version
```

## Notebook

File extension:

```
.ipynb
```

Example:

```
python_basics.ipynb
```

Save:

```
Ctrl + S
```

## Shortcuts

```
Shift + Enter → Run cell
Ctrl + Enter  → Run cell
A             → Add cell above
B             → Add cell below
M             → Markdown cell
Y             → Code cell
DD            → Delete cell
```

## Google Colab

Open:

```
https://colab.research.google.com/
```

Create **New Notebook** and run:

```python
print("Hello Colab")
```

Check Python:

```python
import sys
print(sys.version)
```

Save:

```
File → Save
File → Save a copy in Drive
```

## Key Concepts

```
Notebook → .ipynb file containing code, output and notes
Cell     → Individual code or Markdown block
Kernel   → Process that executes notebook code
Runtime  → Computing environment used by Colab
Jupyter  → Local notebook environment
Colab    → Cloud-based Jupyter environment
```