# Medical Insurance Cost Analysis

## Overview
This project explores the **Medical Insurance Cost dataset** to identify which factors most strongly influence medical charges. The analysis focuses on lifestyle and demographic variables such as smoking, age, BMI, sex, region, and number of children. Our goal was to test initial assumptions, uncover unexpected patterns, and reflect on the implications for fairness and healthcare costs.

## Dataset
- **Source:** Mosap Abdel-Ghany, *Medical Insurance Cost Dataset* (2025)  
- **Description:** The dataset includes 1,338 records with the following fields:  
  - **age:** Age of the primary beneficiary  
  - **sex:** Gender of the policyholder (male/female)  
  - **bmi:** Body Mass Index, providing a measure of body fat based on height and weight  
  - **children:** Number of dependents covered by insurance  
  - **smoker:** Whether the individual is a smoker (yes/no)  
  - **region:** Geographic region in the U.S. (northeast, southeast, southwest, northwest)  
  - **charges:** Medical insurance cost billed to the individual  

## How to Reproduce the Analysis
1. Clone or download this repository.  
2. Open the notebook `analysis.ipynb` in Jupyter Notebook or VS Code.  
3. Install the required dependencies:  
   ```bash
   pip install pandas numpy matplotlib seaborn
````

4. Run all cells in the notebook in order:

   * **Step 1:** Load and inspect the dataset
   * **Step 2:** Perform exploratory data analysis (EDA)
   * **Step 3:** Create visualizations (e.g., smoker vs. non-smoker, charges by age, BMI, children, region, and sex)
   * **Step 4:** Interpret results and discuss limitations

## Key Findings

* **Smoking is the strongest driver** of higher charges. Median charges for smokers exceed $30,000 compared to about $8,000 for non-smokers.
* **Age steadily increases charges**, with smokers paying significantly more at every age group.
* **Number of children** had little effect on charges, contrary to initial expectations.
* **Region and sex** showed small differences overall, though all categories had high-cost outliers.
* **BMI** correlated with higher costs, but its effect was weaker compared to smoking and age.

## Limitations and Ethical Considerations

* The dataset does not include marital status, specific insurance plan details, or systemic social and economic factors that influence healthcare costs.
* Outliers significantly impact averages and highlight the unpredictability of healthcare expenses.
* Using demographic features such as sex or region in pricing could reinforce unfair disparities.
* Smoking raises ethical questions: should insurers simply charge more to smokers, or invest in prevention through cessation programs?

## Reflection

This project demonstrates how lifestyle choices, particularly smoking, have a disproportionate effect on medical insurance costs compared to other demographic factors. It also underscores the importance of considering fairness and ethics when interpreting and applying health-related data.

Used ChatGPT5 to help create this README.md on 9/29/25 at 10:00pm.