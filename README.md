Group members
📊 Principal Component Analysis (PCA) in Python

This project implements Principal Component Analysis (PCA) from scratch using NumPy.
It allows users to reduce the dimensionality of a dataset by selecting the top k principal components.

The program runs in a menu-driven, interactive command-line interface, where users manually input data and compute PCA results.

🚀 Features

PCA implementation using covariance matrix and eigen decomposition

Interactive menu-based CLI

User-defined:

Number of samples

Number of features

Dataset values

Number of principal components (k)

Displays:

Reduced data

Top eigenvalues

Original and reduced data shapes

Input validation and error handling

🧠 What is PCA?

Principal Component Analysis (PCA) is a dimensionality reduction technique used in:

Machine Learning

Data Science

Statistics

It transforms high-dimensional data into a lower-dimensional space while preserving as much variance as possible.

🛠️ Requirements

Make sure you have Python and NumPy installed.

pip install numpy

▶️ How to Run

Clone the repository or download the file.

Open a terminal in the project directory.

Run the program:

python main.py

📋 How the Program Works

Choose Compute PCA from the menu.

Enter:

Number of samples (rows)

Number of features (columns)

Input dataset values row by row.

Enter the number of principal components (k).

The program outputs:

Reduced dataset

Top eigenvalues

Original and reduced shapes

🧪 Example Input
Number of samples: 3
Number of features: 2

Row 1: 2 4
Row 2: 1 3
Row 3: 0 2

k = 1

Output
Original shape: (3, 2)
Reduced shape: (3, 1)
Top eigenvalue(s): [2.]
Reduced data:
[[-1.414]
 [ 0.   ]
 [ 1.414]]

📂 Code Structure
main.py
│
├── pca(X, k)        # PCA function
└── main program     # Menu-driven user interface

⚙️ PCA Algorithm Steps

1.Compute the mean of the dataset

2.Center the data

3.Compute the covariance matrix

4.Find eigenvalues and eigenvectors

5.Sort eigenvalues in descending order

6.Select top k eigenvectors

7.Project data into lower-dimensional space
