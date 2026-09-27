# Evaluation Results

The final experiment used a scaled Logistic Regression classifier.

## Test-set metrics

- Accuracy: **75.33%**
- Precision: **64.91%**
- Recall: **67.27%**
- F1-score: **66.07%**
- ROC-AUC: **81.47%**

## Confusion matrix

| | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | 79 | 20 |
| Actual 1 | 18 | 37 |

The model correctly classified 79 negative and 37 positive test cases, with 20 false positives and 18 false negatives.

## Cross-validation

Mean 5-fold cross-validation accuracy: approximately **76.06%**.

## Interpretation

Accuracy alone does not fully describe a binary classifier. Precision describes the proportion of positive predictions that were correct, recall describes the proportion of observed positive cases identified by the model, F1-score balances precision and recall, and ROC-AUC evaluates ranking performance across classification thresholds.

These results describe this dataset and evaluation split. They should not be interpreted as evidence of clinical effectiveness.
