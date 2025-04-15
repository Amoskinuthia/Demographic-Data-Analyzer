import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file.
    # The Adult dataset does not have column headers by default; we specify them here.
    column_names = [
        'age', 'workclass', 'fnlwgt', 'education', 'education-num',
        'marital-status', 'occupation', 'relationship', 'race', 'sex',
        'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
    ]
    df = pd.read_csv('C:/Users/kkinut/Documents/PD/adult.data.csv', header=None, names=column_names)

    # 1. How many of each race are represented in this dataset?  
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100

    # 4. Advanced education: Bachelors, Masters, or Doctorate
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # Percentage with salary >50K for those with advanced education
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
    # Percentage with salary >50K for those without advanced education
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100

    # 5. What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # 6. What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = num_min_workers[num_min_workers['salary'] == '>50K']
    rich_percentage = (rich_min_workers.shape[0] / num_min_workers.shape[0]) * 100 if num_min_workers.shape[0] > 0 else 0

    # 7. What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    high_income_country_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    percentage_per_country = (high_income_country_counts / country_counts) * 100
    highest_earning_country = percentage_per_country.idxmax()
    highest_earning_country_percentage = percentage_per_country.max()

    # 8. Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", round(average_age_men, 1))
        print(f"Percentage with Bachelors degrees: {round(percentage_bachelors, 1)}%")
        print(f"Percentage with higher education that earn >50K: {round(higher_education_rich, 1)}%")
        print(f"Percentage without higher education that earn >50K: {round(lower_education_rich, 1)}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {round(rich_percentage, 1)}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {round(highest_earning_country_percentage, 1)}%")
        print("Top occupation in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# To run the function and see the output, uncomment the following line:
calculate_demographic_data()
