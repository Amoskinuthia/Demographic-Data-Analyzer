# 📊 Demographic Data Analyzer

This project analyzes demographic data extracted from the **1994 U.S. Census database** using Python and Pandas. It answers insightful questions about work, education, income, and demographics across different population segments.

---

## 📌 Project Overview

The goal of this analysis is to extract meaningful statistics from a structured demographic dataset. The analysis covers:

- **Race distribution**
- **Average age of men**
- **Education level insights**
- **Income comparisons**
- **Work hours analysis**
- **Country-wise high-income analysis**
- **Occupation trends in specific countries**

The data is cleaned, processed, and queried using **Pandas** to produce well-structured statistical results.

---

## 📁 Dataset

- The dataset is derived from the **Adult Income dataset**, also known as the **Census Income dataset**.
- It includes the following features:

| Feature            | Description                                       |
|--------------------|---------------------------------------------------|
| age                | Age of the individual                             |
| workclass          | Type of employment                                |
| fnlwgt             | Final weight (used in census sampling)           |
| education          | Highest level of education attained              |
| education-num      | Number of years of education                      |
| marital-status     | Marital status                                    |
| occupation         | Type of job                                       |
| relationship       | Relationship status within a family              |
| race               | Race of the individual                            |
| sex                | Gender                                            |
| capital-gain       | Capital gains from investment                     |
| capital-loss       | Capital loss from investment                      |
| hours-per-week     | Number of work hours per week                     |
| native-country     | Country of origin                                 |
| salary             | Salary category (<=50K or >50K)                   |

---

## 🚀 Questions Answered

1. How many people of each race are represented in the dataset?
2. What is the average age of men?
3. What percentage of people have a Bachelor's degree?
4. What percentage of people with **advanced education** (Bachelors, Masters, Doctorate) make more than 50K?
5. What percentage of people without advanced education make more than 50K?
6. What is the minimum number of hours a person works per week?
7. What percentage of the people who work the **minimum number of hours per week** have a salary of more than 50K?
8. What **country** has the highest percentage of people that earn >50K and what is that percentage?
9. Identify the **most popular occupation for those who earn >50K in India**.

All percentage results are rounded to the **nearest tenth**.

---

## 🛠️ Tools and Libraries Used

- [Python 3.x](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Jupyter Notebook (optional for exploration)](https://jupyter.org/)
- [NumPy (optional)](https://numpy.org/)

---

## 📂 File Structure
