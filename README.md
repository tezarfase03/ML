# Machine Learning Notebooks

A collection of Jupyter notebooks covering data preprocessing and feature engineering techniques using the Titanic and House Prices datasets.

---

## Folder Structure

```
ML/
├── imputation/
│   ├── CCA.ipynb
│   ├── Frequent_value_imputation.ipynb
│   ├── arbitrary_value_imputation.ipynb
│   └── missing_cateogry_imputation.ipynb
│
├── missing_indicator/
│   ├── automatically-select-imputer.ipynb
│   ├── knn-imputer.ipynb
│   ├── missing-indicator.ipynb
│   └── random-sample-imputation.ipynb
│
├── feature_engineering/
│   ├── binarization.ipynb
│   └── binning.ipynb
│
├── transformers/
│   ├── Transformers.ipynb
│   └── powertransformers.ipynb
│
├── pipelines/
│   └── Pipe.ipynb
│
├── train.csv
└── house-train.csv
```

---

## Topics Covered

### Imputation (`imputation/`)
Techniques to handle missing values in datasets.

| Notebook | Description |
|---|---|
| `CCA.ipynb` | Complete Case Analysis — drop rows with missing values |
| `Frequent_value_imputation.ipynb` | Fill missing values with the most frequent value |
| `arbitrary_value_imputation.ipynb` | Fill missing values with a fixed arbitrary value |
| `missing_cateogry_imputation.ipynb` | Handle missing values in categorical columns |

---

### Missing Indicator (`missing_indicator/`)
Advanced imputation techniques that preserve data distribution.

| Notebook | Description |
|---|---|
| `automatically-select-imputer.ipynb` | Use GridSearchCV to automatically find the best imputer strategy |
| `missing-indicator.ipynb` | Add True/False columns to flag which values were originally missing |
| `random-sample-imputation.ipynb` | Fill missing values with randomly sampled real values to preserve distribution |
| `knn-imputer.ipynb` | Use K-Nearest Neighbours to fill missing values based on similar rows |

---

### Feature Engineering (`feature_engineering/`)
Techniques to transform raw features into more useful representations.

| Notebook | Description |
|---|---|
| `binarization.ipynb` | Convert numerical values into binary (0 or 1) |
| `binning.ipynb` | Group continuous values into discrete buckets/bins |

---

### Transformers (`transformers/`)
Techniques to change the distribution or scale of features.

| Notebook | Description |
|---|---|
| `Transformers.ipynb` | Standard scaling, min-max scaling and other transformations |
| `powertransformers.ipynb` | Box-Cox and Yeo-Johnson transformations to normalize skewed data |

---

### Pipelines (`pipelines/`)
Combining multiple preprocessing steps into one clean workflow.

| Notebook | Description |
|---|---|
| `Pipe.ipynb` | Build sklearn pipelines with ColumnTransformer and GridSearchCV |

---

## Datasets

| File | Description |
|---|---|
| `train.csv` | Titanic dataset — predict passenger survival |
| `house-train.csv` | House Prices dataset — predict sale price of houses |

---

## Requirements

Install required libraries:

```
pip install numpy pandas scikit-learn matplotlib seaborn
```

## Tools Used

- Python 3
- Jupyter Notebook
- scikit-learn
- pandas
- numpy
- matplotlib
- seaborn
