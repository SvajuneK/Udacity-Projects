# Loan Data from Prosper
## by Svajune Klimasauskaite


## Goal

This project has two parts that demonstrate the importance and value of data visualization techniques in the data analysis process. In the first part, I will use Python visualization libraries to systematically explore a selected dataset, starting from plots of single variables and building up to plots of multiple variables. In the second part, I will produce a short presentation that illustrates interesting properties, trends, and relationships that you discovered in your selected dataset. The primary method of conveying findings will be through transforming my exploratory visualizations from the first part into polished, explanatory visualizations.

## Dataset

This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others.
Please see Data Dictionary for the attribute explanation. 

## Conslusions

>Here is a list of surprising correlations that were captured with the correlation matrix:
   * Income Verifiable over Dept to Income Ration (corr = -0.60)
   * Bankcard Utilisation over Credit Score Rating (corr = -0.41)
   * The correlation for Stated Monthly Income and Income Range was surprisingly low, only 0.31. 

>Loan characteristics changed over the years: 
   * More Term varieties were introduced 
   * Business was capable to scale and offer larger amount loans
   * Over the years there were introduced higher granularity Loan Statuses
   * Over the years the risk was better differentiated. 
    
>Borrower characteristics changed over the years: 
   * After the financial crisis, the majority of the borrowers were homeowners.
   * With the years there were fewer borrowers without a job and without an income.
   * With the years' loans changed for the borrowers with a longer employment status duration.
    
>Financial characteristics showed maturity level over the years, i.e.:
   * fewer outliers over the years,
   * more secured loans,
   * better risk distribution.
    
>Additional Financial views showed:
   * Bigger amount of loans have lower borrow rate and issued for the borrowers with higher monthly salary.  
   * Credit score rate correlates with Bankcard Utilisation. With higher Bankcard Utilisation and lower monthly salary, there is a high chance to be rated with a lower Credit Score.
    
>Prosper Rating is well established. 

----------
