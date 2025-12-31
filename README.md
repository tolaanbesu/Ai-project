
# 🧬 PCA From Scratch in Python

A minimal but **powerful** command‑line tool that performs Principal Component Analysis (PCA) from scratch using NumPy. 

---

## 👥 Authors

- 1. Lisan Geberetensay — UGR/1712/15  
- 2. Tola Anbesu — UGR/7995/15  
- 3. Yohannes Gizaw — UGR/6435/15  
- 4. Nathnael Hailemariam — UGR/9299/16

---

## 📊 What This Project Does

This project lets you: 

- Implement PCA using covariance matrix and eigen decomposition  
- Interactively enter your own dataset via a menu‑driven CLI  
- Choose the number of principal components \(k\) and reduce dimensionality  
- See reduced data, top eigenvalues, and original vs reduced shapes  
- Benefit from input validation and basic error handling  

---

## 🧠 Quick Primer: What Is PCA?

Principal Component Analysis (PCA) is a dimensionality reduction technique widely used in: 

- Machine learning  
- Data science  
- Statistics  

It transforms high‑dimensional data into a lower‑dimensional space while preserving as much variance as possible, making patterns more **visible** and models simpler. 

---

## 🛠️ Requirements

Make sure you have the following installed: 

- Python (3.x recommended)  
- NumPy  

Install NumPy with: 

```bash
pip install numpy
```


---

## ▶️ How to Run

1. Clone this repository or download the project files. 
2. Open a terminal in the project directory. 
3. Run the main program: 
```bash
python main.py
```


---

## 📋 Interactive Workflow

When you run the program, use the menu to choose **Compute PCA**, then follow the prompts: 

1. Enter number of samples (rows). 
2. Enter number of features (columns). 
3. Input dataset values row by row. 
4. Enter the desired number of principal components $k$. 

The program outputs: 

- Reduced dataset
- Top eigenvalues
- Original and reduced data shapes

---

## 🧪 Example Session

Example input: 

- Number of samples: `3`
- Number of features: `2`

```text
Row 1: 2 4
Row 2: 1 3
Row 3: 0 2

k = 1
```

Example output: 

```text
Original shape: (3, 2)
Reduced shape: (3, 1)
Top eigenvalue(s): [2.]
Reduced data:
[[-1.414]
 [ 0.   ]
 [ 1.414]]
```


---

## 📂 Project Structure

```text
main.py
│
├── pca(X, k)        # Core PCA function
└── main program     # Menu-driven user interface
```



---

## ⚙️ PCA Algorithm Steps

Under the hood, the PCA implementation performs: 

1. Compute the mean of the dataset
2. Center the data by subtracting the mean
3. Compute the covariance matrix
4. Find eigenvalues and eigenvectors
5. Sort eigenvalues in descending order
6. Select the top $k$ eigenvectors
7. Project the data into a lower‑dimensional space

---


```
`
