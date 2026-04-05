# Linear Regression From Scratch

This is a simple linear regression model built from scratch.

## Closed-Form Linear Regression

Regression coefficient:

```text
w = {n * sum(x * y) - sum(x) * sum(y)} / {n * sum(x**2) - (sum(x)**2)}
```

Intercept formula:

```text
b = (y - mean) - (w * (x - mean))
```

This notebook does not use scikit-learn by any means. It is based only on pure maths.

## Dataset Used

Dataset:
https://www.kaggle.com/datasets/rohankayan/years-of-experience-and-salary-dataset

Two features, 30 rows.
