# Logistic-regression-using-LIBLINEAR-in-sklearn
penalty= 'l1', solver = 'liblinear',

====================================reults=============================

****************************** logistic model ******************************

Regression coefficients：

[[ 0.33386485  0.03588297  0.02153707 -0.10904045 -0.35580895  0.19109178
   0.34664197 -0.03244156 -0.70304986 -0.36607281 -0.71407291 -0.12732962
   0.39184716 -0.04090133  1.00036415  0.60470255  1.00170215  0.35441492
   0.60768378]]
   
****************************** actual value ******************************

[0 0 1 0 0 0 0 1 1 0 1 0 0 1 0 0 0 0 0 1 1 0 0]

****************************** predictive value ******************************

[1 0 1 0 0 1 0 0 1 0 1 0 0 1 1 1 0 1 1 1 1 1 0]

****************************** recall ratio ******************************

              precision    recall  f1-score   support

          cars       0.90      0.56      0.69        16
          rails       0.46      0.86      0.60         7

          micro avg       0.65      0.65      0.65        23
          macro avg       0.68      0.71      0.65        23
          weighted avg       0.77      0.65      0.66        23

accuracy 0.6521739130434783

![confusion matrix](https://github.com/yukiiwong/Logistic-regression-using-LIBLINEAR-in-sklearn/blob/master/Figure_1.png)

class report              precision    recall  f1-score   support

           0       0.90      0.56      0.69        16
           1       0.46      0.86      0.60         7

   micro avg       0.65      0.65      0.65        23
   macro avg       0.68      0.71      0.65        23
weighted avg       0.77      0.65      0.66        23


Process finished with exit code 0
