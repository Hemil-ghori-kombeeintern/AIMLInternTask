
# Bias, Variance, Underfitting and Overfitting in Machine Learning

## 1. Introduction

When we build a Machine Learning model, our goal is not only to make it perform well on the training data.

The real goal is:

> **The model should learn the underlying pattern in the data and perform well on new, unseen data.**
> 

To understand whether a model is learning correctly, we need to understand four important concepts:

1. **Bias**
2. **Variance**
3. **Underfitting**
4. **Overfitting**

These concepts are closely related to the **Bias-Variance Tradeoff**.

---

# 2. Bias

## What is Bias?

**Bias is the error caused by a model making overly simple assumptions about the data.**

A model with high bias is not powerful enough to capture the real pattern in the data.

In simple words:

> **High Bias = Model is too simple.**
> 

For example, suppose the real relationship between two variables is curved:

```
        *
      *   *
    *       *
  *           *
 *             *
```

But we use a simple linear model:

```
*
  *
    *
      *
        *
```

The linear model cannot capture the curved relationship properly.

Therefore, it has **high bias**.

---

## 2.1 Characteristics of High Bias

A high-bias model usually has:

- Low training performance
- Low validation/test performance
- High training error
- High validation/test error
- A model that is too simple

This situation is usually called **underfitting**.

---

# 3. Variance

## What is Variance?

**Variance describes how much a model’s predictions change when the training data changes.**

A high-variance model is very sensitive to the training dataset.

In simple words:

> **High Variance = Model is too sensitive and too complex.**
> 

For example, suppose we train a very deep Decision Tree.

The tree may learn:

- Useful patterns
- Noise
- Outliers
- Random details
- Specific examples from the training dataset

The model may perform extremely well on training data but poorly on new data.

This is called **overfitting**.

---

## 3.1 Characteristics of High Variance

A high-variance model usually has:

- Very high training performance
- Lower validation/test performance
- Very low training error
- High validation/test error
- A model that is too complex

This situation is usually called **overfitting**.

---

# 4. Underfitting

## What is Underfitting?

**Underfitting occurs when a model is too simple to learn the important patterns in the training data.**

The model has not learned enough from the data.

Therefore, it performs poorly on both:

- Training data
- Testing/validation data

### Typical pattern

```
Training Performance    = LOW
Testing Performance     = LOW
```

or:

```
Training Error          = HIGH
Testing Error           = HIGH
```

Underfitting is generally associated with **high bias**.

---

# 5. Example of Underfitting

Imagine that the real data has a complex pattern:

```
        *
      *   *
    *       *
  *           *
    *       *
      *   *
        *
```

But our model is extremely simple and assumes:

```
*
  *
    *
      *
        *
```

The model cannot learn the real pattern.

Therefore:

```
Simple Model
     ↓
Cannot learn enough
     ↓
High Bias
     ↓
Underfitting
```

---

# 6. How to Detect Underfitting

We can compare training and validation/test performance.

For example:

| Metric | Result |
| --- | --- |
| Training Accuracy | 65% |
| Validation Accuracy | 63% |

Both scores are low.

This suggests that the model is not learning the problem well.

### General pattern

```
Training Score      LOW
Validation Score    LOW

        ↓

    Underfitting

        ↓

     High Bias
```

---

# 7. Causes of Underfitting

Underfitting can happen because:

### 1. Model is too simple

Example:

```python
DecisionTreeClassifier(max_depth=1)
```

A tree with depth 1 may be unable to capture complex relationships.

### 2. Too much regularization

Strong regularization can prevent the model from learning enough.

### 3. Not enough useful features

The model may not have enough information to learn the target pattern.

### 4. Model is trained for too little time

This can happen with some iterative models such as neural networks.

### 5. Poor feature representation

The available features may not represent the important relationships in the data.

---

# 8. How to Reduce Underfitting

To reduce underfitting, we can:

- Increase model complexity
- Add useful features
- Reduce excessive regularization
- Train the model for longer
- Use a more powerful algorithm
- Improve feature engineering

For example:

```
Simple Decision Tree
        ↓
Increase max_depth
        ↓
More complex model
        ↓
Better ability to learn patterns
```

---

# 9. Overfitting

## What is Overfitting?

**Overfitting occurs when a model learns the training data too closely, including noise and unnecessary patterns.**

The model performs extremely well on training data but performs poorly on unseen data.

In simple words:

> **The model has memorized the training data instead of learning a general pattern.**
> 

---

# 10. Example of Overfitting

Imagine we have training data:

```
Training Data
      ↓
Model learns useful patterns
      +
Model learns noise
      +
Model learns individual examples
      ↓
Very high training performance
```

When new data is given:

```
New Data
   ↓
Model cannot generalize
   ↓
Poor performance
```

Therefore:

```
Very High Training Performance
              +
Low Testing Performance
              ↓
         Overfitting
              ↓
        High Variance
```

---

# 11. How to Detect Overfitting

Suppose we get:

| Metric | Result |
| --- | --- |
| Training Accuracy | 99% |
| Validation Accuracy | 78% |

There is a large gap between training and validation performance.

This is a strong indication of overfitting.

### General pattern

```
Training Score       VERY HIGH
Validation Score     MUCH LOWER

           ↓

       Overfitting

           ↓

      High Variance
```

---

# 12. Causes of Overfitting

Overfitting can happen because:

### 1. Model is too complex

For example:

```python
DecisionTreeClassifier(max_depth=None)
```

A very deep tree can memorize the training data.

### 2. Training dataset is too small

A complex model may memorize a small dataset.

### 3. Too many irrelevant features

Noise and irrelevant features can make the model learn unnecessary patterns.

### 4. Too little regularization

Regularization helps prevent excessive model complexity.

### 5. Training for too long

Some models, especially neural networks, can eventually start fitting noise.

---

# 13. How to Reduce Overfitting

Common solutions include:

### 1. Reduce model complexity

For example:

```python
DecisionTreeClassifier(max_depth=5)
```

instead of:

```python
DecisionTreeClassifier(max_depth=None)
```

### 2. Use more training data

More representative data can improve generalization.

### 3. Use regularization

Common types include:

- L1 regularization
- L2 regularization
- Dropout for neural networks

### 4. Feature selection

Remove unnecessary or noisy features.

### 5. Cross-validation

Use cross-validation to evaluate whether the model generalizes.

### 6. Early stopping

Useful for models such as neural networks and gradient boosting.

---

# 14. Bias vs Variance

Bias and variance describe two different sources of model error.

## High Bias

The model is too simple.

```
Model
 ↓
Too Simple
 ↓
Misses important patterns
 ↓
High Bias
 ↓
Underfitting
```

## High Variance

The model is too complex.

```
Model
 ↓
Too Complex
 ↓
Learns noise/details
 ↓
High Variance
 ↓
Overfitting
```

---

# 15. Bias-Variance Tradeoff

There is usually a tradeoff between bias and variance.

As model complexity increases:

```
Model Complexity
        →
```

Generally:

```
Bias
 ↓↓↓

Variance
   ↑↑↑
```

A very simple model tends to have:

```
High Bias
Low Variance
```

A very complex model tends to have:

```
Low Bias
High Variance
```

The goal is to find a good balance.

---

# 16. Model Complexity

Consider a Decision Tree.

### Very Small Tree

```
max_depth = 1
```

The model is simple.

Possible result:

```
High Bias
Low Variance
Underfitting
```

### Medium Tree

```
max_depth = 5
```

The model has enough complexity to learn useful patterns.

Possible result:

```
Balanced Bias
Balanced Variance
Good Generalization
```

### Very Deep Tree

```
max_depth = None
```

The model may become extremely complex.

Possible result:

```
Low Bias
High Variance
Overfitting
```

---

# 17. Training Error vs Validation Error

One of the easiest ways to understand model behavior is to compare training and validation errors.

## Underfitting

```
Training Error       HIGH
Validation Error     HIGH
```

Example:

```
Training Error    = 35%
Validation Error  = 37%
```

The model performs poorly everywhere.

---

## Good Fit

```
Training Error       LOW
Validation Error     LOW
```

Example:

```
Training Error    = 8%
Validation Error  = 10%
```

The model performs well and generalizes.

---

## Overfitting

```
Training Error       VERY LOW
Validation Error     HIGH
```

Example:

```
Training Error    = 1%
Validation Error  = 22%
```

The model has learned the training data too closely.

---

# 18. Important Comparison Table

| Property | Underfitting | Good Fit | Overfitting |
| --- | --- | --- | --- |
| Model Complexity | Too Low | Appropriate | Too High |
| Bias | High | Balanced | Low |
| Variance | Low | Balanced | High |
| Training Error | High | Low | Very Low |
| Validation Error | High | Low | High |
| Training Accuracy | Low | High | Very High |
| Validation Accuracy | Low | High | Low |
| Generalization | Poor | Good | Poor |

---

# 19. Visual Concept

```
                 MODEL COMPLEXITY
                       →

     Underfitting       Good Fit       Overfitting
          |                |                |
          ↓                ↓                ↓
      Too Simple      Appropriate       Too Complex
          |                |                |
      High Bias        Balanced        High Variance
          |                |                |
          ↓                ↓                ↓
      Poor Model       Good Model       Poor Model
```

---

# 20. Learning Curves

A learning curve shows model performance as the amount of training data increases.

We usually plot:

- Training score
- Validation score

### Underfitting

The two scores may both remain low:

```
Score
 ^
 |
 |  Training  ─────────
 |  Validation─────────
 |
 +--------------------------> Training Data
```

This suggests **high bias**.

---

### Overfitting

Training score remains high while validation score is lower:

```
Score
 ^
 | Training  ─────────────
 |
 | Validation ─────────
 |
 +--------------------------> Training Data
```

A large gap suggests **high variance / overfitting**.

---

# 21. Cross-Validation

Instead of relying on only one train-test split, we can use **K-Fold Cross-Validation**.

For example, with 5-fold cross-validation:

```
Dataset
   ↓
+----+----+----+----+----+
| F1 | F2 | F3 | F4 | F5 |
+----+----+----+----+----+

Round 1 → F1 validation, F2-F5 training
Round 2 → F2 validation, F1,F3-F5 training
Round 3 → F3 validation, F1,F2,F4,F5 training
Round 4 → F4 validation, F1-F3,F5 training
Round 5 → F5 validation, F1-F4 training
```

Then we calculate the average validation performance.

Cross-validation gives us a more reliable estimate of how the model generalizes.

---

# 22. Practical Example

Suppose we train three models.

### Model A

```
Training Accuracy   = 65%
Validation Accuracy = 63%
```

Diagnosis:

```
High Bias
   ↓
Underfitting
```

---

### Model B

```
Training Accuracy   = 94%
Validation Accuracy = 92%
```

Diagnosis:

```
Good Fit
   ↓
Good Generalization
```

---

### Model C

```
Training Accuracy   = 100%
Validation Accuracy = 75%
```

Diagnosis:

```
High Variance
   ↓
Overfitting
```

---

# 23. How to Diagnose a Model

When you train a Machine Learning model, follow these steps.

### Step 1: Check training performance

```
How well does the model perform on training data?
```

### Step 2: Check validation/test performance

```
How well does it perform on unseen data?
```

### Step 3: Compare the two

```
Training Low + Validation Low
        ↓
    Underfitting

Training High + Validation High
        ↓
      Good Fit

Training Very High + Validation Low
        ↓
     Overfitting
```

### Step 4: Check the learning curve

Look for:

- Low scores → possible high bias
- Large train-validation gap → possible high variance

### Step 5: Use cross-validation

Check whether the model performs consistently across different splits.

---

# 24. Simple Real-World Example

Imagine a student preparing for an exam.

## Underfitting Student

The student studies very little.

```
Studies very little
       ↓
Does not understand enough concepts
       ↓
Poor performance in practice tests
       ↓
Poor performance in final exam
```

This is similar to **high bias / underfitting**.

---

## Overfitting Student

The student memorizes only the exact questions from practice papers.

```
Memorizes practice questions
       ↓
Excellent practice-test performance
       ↓
New questions appear in final exam
       ↓
Poor performance
```

This is similar to **high variance / overfitting**.

---

## Good Student

The student understands the underlying concepts.

```
Understands concepts
       ↓
Can solve different types of questions
       ↓
Good practice performance
       ↓
Good final-exam performance
```

This is similar to a model with **good generalization**.

---

# 25. Key Differences

## Bias

> Bias is the error caused by overly simplistic assumptions.
> 

## Variance

> Variance is the sensitivity of a model to changes in the training data.
> 

## Underfitting

> Underfitting happens when the model is too simple and cannot learn the underlying pattern.
> 

## Overfitting

> Overfitting happens when the model learns the training data too closely and fails to generalize to unseen data.
> 

---

# 26. Quick Revision

```
HIGH BIAS
   ↓
Model too simple
   ↓
Underfitting
   ↓
Training performance LOW
Validation performance LOW
```

```
HIGH VARIANCE
   ↓
Model too complex
   ↓
Overfitting
   ↓
Training performance VERY HIGH
Validation performance LOW
```

```
GOOD MODEL
   ↓
Balanced Bias + Variance
   ↓
Good Training Performance
   +
Good Validation Performance
   ↓
Good Generalization
```

---

# 27. Final Summary

The most important relationship to remember is:

| Concept | Meaning |
| --- | --- |
| **Bias** | Error caused by overly simple assumptions |
| **Variance** | Sensitivity to changes in training data |
| **Underfitting** | Model is too simple |
| **Overfitting** | Model is too complex and learns noise |
| **High Bias** | Usually leads to underfitting |
| **High Variance** | Usually leads to overfitting |
| **Good Generalization** | Model performs well on unseen data |

### The Golden Rule

> **A good Machine Learning model should learn the important patterns without memorizing the training data.**
> 

```
             Model Complexity
                    →

    Underfitting    Good Fit    Overfitting
         ↓             ↓             ↓
     High Bias      Balanced     High Variance
         ↓             ↓             ↓
      Too Simple    Best Zone    Too Complex
```