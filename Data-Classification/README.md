# DataClassification — KNN Iris Classifier 

A supervised machine learning pipeline that classifies iris flowers into 3 species using the K-Nearest Neighbors algorithm. Built as Project 2 of the DecodeLabs AI Engineering Internship.

## Project Structure

```
DataClassification/
├── classifier.ipynb    # Full ML pipeline — EDA, training, evaluation
└── README.md
```

## Pipeline

```
Load Iris Dataset
      ↓
Exploratory Data Analysis (EDA)
      ↓
Train/Test Split (80/20)
      ↓
Feature Scaling (StandardScaler)
      ↓
Train KNN Model (K=5)
      ↓
Evaluate — Accuracy, F1 Score, Confusion Matrix
```

## Dataset

The Iris dataset is a classic ML benchmark loaded directly from sklearn.

| Property | Value |
|----------|-------|
| Samples | 150 |
| Classes | 3 (Setosa, Versicolor, Virginica) |
| Features | 4 (Sepal Length, Sepal Width, Petal Length, Petal Width) |
| Balance | Perfectly balanced (50 samples per class) |

## Results

| Metric | Score |
|--------|-------|
| Accuracy | 100% |
| Precision | 1.00 |
| Recall | 1.00 |
| F1 Score | 1.00 |

**Confusion Matrix — 30 test samples, 0 misclassifications:**

```
              Predicted
              Setosa  Versicolor  Virginica
Actual  Setosa    10           0          0
    Versicolor     0           9          0
     Virginica     0           0         11
```

## Key Concepts Learned

- **Train/Test Split** — separating data to evaluate on unseen samples
- **Feature Scaling** — StandardScaler normalizes features so KNN distance calculations aren't biased by scale
- **KNN Algorithm** — classifies by majority vote from K nearest neighbors
- **K Selection** — elbow method tested K=1 to K=19; Iris is clean enough that all K values achieved 0% error, so K=5 was chosen as the standard convention
- **Confusion Matrix** — visualizes correct vs incorrect predictions per class
- **F1 Score** — harmonic mean of precision and recall, more reliable than accuracy alone on imbalanced data
- **Why accuracy can mislead** — on imbalanced datasets, 99% accuracy can mean the model learned nothing

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| scikit-learn | ML pipeline — KNN, StandardScaler, metrics |
| pandas | Data handling |
| numpy | Numerical operations |
| matplotlib / seaborn | Visualization |

## Run Locally

```bash
pip install scikit-learn pandas numpy matplotlib seaborn jupyter
jupyter notebook classifier.ipynb
```

## Author

**Fatimah** — AI Engineering Intern @ DecodeLabs