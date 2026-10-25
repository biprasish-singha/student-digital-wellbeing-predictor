\# 🧠 Student Digital Wellbeing Predictor



\### Predicting Student Stress Levels and Mental Health Scores Using Machine Learning



A machine learning project that analyzes students' demographic characteristics, digital usage patterns, and lifestyle habits to predict \*\*Stress Level\*\* and \*\*Mental Health Score\*\*.



The project combines exploratory data analysis, feature engineering, model comparison, hyperparameter tuning, and an interactive Streamlit application to demonstrate how machine learning can be applied to student digital wellbeing.



\---



\## 📌 Table of Contents



\- \[Project Overview](#-project-overview)

\- \[Objectives](#-objectives)

\- \[Prediction Targets](#-prediction-targets)

\- \[Key Features](#-key-features)

\- \[Technology Stack](#-technology-stack)

\- \[Machine Learning Workflow](#-machine-learning-workflow)

\- \[Model Selection and Evaluation](#-model-selection-and-evaluation)

\- \[Project Structure](#-project-structure)

\- \[Installation and Setup](#-installation-and-setup)

\- \[Running the Application](#-running-the-application)

\- \[Model Files](#-model-files)

\- \[Key Insights](#-key-insights)

\- \[Future Improvements](#-future-improvements)

\- \[Disclaimer](#-disclaimer)



\---



\## 📖 Project Overview



Digital technology and social media are an integral part of students' daily lives. Screen time, phone usage frequency, sleep, physical activity, and study habits may be associated with their stress levels and mental wellbeing.



This project uses machine learning to explore these relationships and predict two outcomes:



1\. \*\*Stress Level Prediction:\*\* Classifies a student's stress level into one of four categories.

2\. \*\*Mental Health Score Prediction:\*\* Estimates a numerical mental health score.



The project includes a Jupyter Notebook for data analysis and model development, alongside a Streamlit application that allows users to enter their information and view both predictions through interactive gauges.



\## 🎯 Objectives



\- Explore relationships between student lifestyle, digital behavior, and wellbeing.

\- Perform exploratory data analysis (EDA) and visualize important patterns.

\- Engineer additional features from digital usage and lifestyle variables.

\- Compare Random Forest and XGBoost algorithms.

\- Evaluate classification and regression models using appropriate performance metrics.

\- Apply hyperparameter tuning to improve model performance.

\- Develop an interactive application for generating both predictions.



\## 🔍 Prediction Targets



\### 1. Stress Level — Classification



\*\*Target variable:\*\* `Stress\_Level`



The classification model predicts one of the following categories:



\- Low

\- Medium

\- High

\- Very High



The project evaluates classification performance using accuracy, weighted F1 score, and cross-validation.



\*\*Selected model:\*\* Baseline Random Forest Classifier.



\### 2. Mental Health Score — Regression



\*\*Target variable:\*\* `Mental\_Health\_Score`



The regression model estimates a numerical mental health score based on the input features.



Model performance is evaluated using:



\- Mean Absolute Error (MAE)

\- Root Mean Squared Error (RMSE)

\- R² score

\- Cross-validation



\*\*Selected model:\*\* Tuned Random Forest Regressor.



The two targets are modeled separately because stress level is categorical, whereas mental health score is numerical.



\## ✨ Key Features



\- \*\*Dual prediction:\*\* Predicts stress level and mental health score from the same set of inputs.

\- \*\*Exploratory data analysis:\*\* Examines numerical and categorical variables, distributions, correlations, and relationships with both targets.

\- \*\*Feature engineering:\*\* Creates additional features related to screen usage and phone unlock frequency.

\- \*\*Model comparison:\*\* Evaluates Random Forest and XGBoost approaches.

\- \*\*Hyperparameter tuning:\*\* Uses RandomizedSearchCV to explore Random Forest configurations.

\- \*\*Interactive interface:\*\* Provides an intuitive Streamlit application for entering user information.

\- \*\*Visual predictions:\*\* Displays the predicted stress level and mental health score using Plotly gauges.



\## 🛠️ Technology Stack



| Technology | Purpose |

|---|---|

| Python | Programming language |

| Pandas | Data manipulation and analysis |

| NumPy | Numerical operations |

| Scikit-learn | Machine learning pipelines, preprocessing, model evaluation, and hyperparameter tuning |

| XGBoost | Gradient-boosting model comparison |

| Matplotlib | Data visualization |

| Seaborn | Statistical visualization |

| Jupyter Notebook | Exploratory analysis and model development |

| Streamlit | Interactive web application |

| Plotly | Interactive prediction gauges |

| Joblib | Saving and loading trained models |

| KaggleHub | Dataset download in the notebook |



\## ⚙️ Machine Learning Workflow



The project follows these steps:



1\. \*\*Data acquisition:\*\* Downloads the dataset using KaggleHub.

2\. \*\*Data understanding:\*\* Examines the dataset structure, variables, missing values, and duplicate records.

3\. \*\*Exploratory data analysis:\*\* Studies feature distributions and relationships with both prediction targets.

4\. \*\*Feature engineering:\*\* Derives additional digital usage features.

5\. \*\*Preprocessing:\*\* Uses preprocessing pipelines to handle numerical and categorical features.

6\. \*\*Baseline modeling:\*\* Trains Random Forest models for classification and regression.

7\. \*\*Model comparison:\*\* Evaluates XGBoost alternatives against the baseline models.

8\. \*\*Hyperparameter tuning:\*\* Uses randomized search with cross-validation to tune Random Forest models.

9\. \*\*Model evaluation:\*\* Compares performance using classification and regression metrics and examines potential overfitting.

10\. \*\*Model deployment:\*\* Saves the selected models and loads them into the Streamlit application.



\### Engineered Features



The project creates additional features, including:



\- `Screen\_Nonscreen\_Ratio`

\- `Unlocks\_Per\_Usage\_Hour`



These features are intended to represent aspects of digital usage and behavioral patterns beyond the original input variables.



\## 📊 Model Selection and Evaluation



The notebook evaluates two algorithms for both prediction targets.



| Prediction Target | Algorithms Evaluated | Selected Model |

|---|---|---|

| Stress Level | Random Forest Classifier and XGBoost Classifier | Baseline Random Forest Classifier |

| Mental Health Score | Random Forest Regressor and XGBoost Regressor | Tuned Random Forest Regressor |



\### Stress Level Classification



The notebook's final conclusion reports that the baseline Random Forest Classifier achieved:



\- \*\*Test accuracy:\*\* 89.9%

\- \*\*Weighted F1 score:\*\* 0.899

\- \*\*Cross-validation accuracy:\*\* 0.871

\- \*\*Cross-validation weighted F1 score:\*\* 0.870



The baseline Random Forest was selected because it outperformed the alternatives evaluated in the notebook on the reported classification metrics.



\### Mental Health Score Regression



The notebook's final conclusion reports the following results for the tuned Random Forest Regressor:



\- \*\*R² score:\*\* 0.913

\- \*\*Root Mean Squared Error (RMSE):\*\* 0.39

\- \*\*Mean Absolute Error (MAE):\*\* 0.289

\- \*\*Cross-validation R² score:\*\* 0.891



These results indicate strong predictive performance on the evaluation data used in the notebook.



\*Note: These are the results reported in the notebook. They describe performance on the evaluated dataset and do not guarantee equivalent performance on new populations or real-world use cases.\*



\## 📁 Project Structure



```text

student-digital-wellbeing-predictor/

│

├── Dataset/

│   └── Dataset downloaded for model development

│

├── Application Screenshots/

│   └── Screenshots of the Streamlit application

│

├── student\_digital\_wellbeing\_predictor.ipynb

│   └── Exploratory data analysis, feature engineering,

│       model training, comparison, and evaluation

│

├── mhs\_app.py

│   └── Streamlit application for both predictions

│

├── requirements.txt

│   └── Python dependencies

│

├── .gitignore

│   └── Excludes model files and generated files from Git

│

└── README.md

&#x20;   └── Project documentation

```



The trained model files are intentionally excluded from GitHub:



\- `stress\_level\_model.pkl`

\- `mental\_health\_score\_model.pkl`



These files must be generated locally by running the appropriate model-training steps in the notebook before the application can make predictions.



\## 🚀 Installation and Setup



\### Prerequisites



Install the following before starting:



\- Python

\- Git

\- Jupyter Notebook or JupyterLab

\- A GitHub account if you want to clone the repository



\### Step 1: Clone the Repository



Replace `YOUR-USERNAME` with your GitHub username.



```bash

git clone https://github.com/YOUR-USERNAME/student-digital-wellbeing-predictor.git

```



Navigate into the project directory:



```bash

cd student-digital-wellbeing-predictor

```



\### Step 2: Create a Virtual Environment



```bash

python -m venv .venv

```



Activate the environment on Windows PowerShell:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



If you use Command Prompt instead:



```cmd

.venv\\Scripts\\activate.bat

```



\### Step 3: Install Dependencies



Install the packages listed in `requirements.txt`:



```bash

python -m pip install -r requirements.txt

```



Ensure the requirements file includes the packages imported by the application and notebook, including Streamlit, Pandas, Joblib, Plotly, Scikit-learn, XGBoost, KaggleHub, and the data visualization libraries used in the notebook.



\### Step 4: Download the Dataset and Generate the Models



The notebook downloads the dataset using KaggleHub and contains the analysis, training, evaluation, and model-saving steps.



Open the notebook:



```bash

jupyter notebook student\_digital\_wellbeing\_predictor.ipynb

```



Execute the notebook's cells in the required order, including the final model-saving section.



The notebook saves the selected models as:



```text

stress\_level\_model.pkl

mental\_health\_score\_model.pkl

```



\*\*Important:\*\* Model training and hyperparameter tuning may take some time. The notebook requires access to the dataset source, and the necessary Python dependencies must be installed.



Verify that both files exist in the project root before proceeding.



\## ▶️ Running the Application



After generating both model files, run the following command from the project root:



```bash

streamlit run mhs\_app.py

```



Streamlit will start a local web server and display a URL in the terminal. Open that URL in your browser.



\### Application Inputs



The application collects information in three groups:



\*\*Personal Information\*\*

\- Age

\- Gender

\- Country

\- Academic level



\*\*Digital Usage\*\*

\- Most-used platform

\- Purpose of use

\- Average daily usage hours

\- Daily phone unlocks



\*\*Lifestyle\*\*

\- Study hours per day

\- Physical activity hours per day

\- Sleep hours per night



\### Prediction Results



After entering the information and clicking \*\*Predict\*\*, the application displays:



\- Predicted stress level using a categorical gauge.

\- Predicted mental health score using a numerical gauge.



Both predictions are generated from the trained models using the same input information.



\## 📦 Model Files



The trained `.pkl` files are intentionally excluded from the repository to avoid uploading large binary files.



The application currently loads the models from the project root:



```python

stress\_model = joblib.load("stress\_level\_model.pkl")

mhs\_model = joblib.load("mental\_health\_score\_model.pkl")

```



Consequently, cloning the repository alone is not sufficient to run the application. Generate the model files locally by executing the relevant training and model-saving cells in the notebook.



\## 💡 Key Insights



The notebook's exploratory analysis identifies several relationships worth investigating:



\- Average daily usage hours and daily phone unlock frequency show negative associations with mental health scores.

\- Sleep duration, study hours, and physical activity show positive associations with mental health scores in the analyzed dataset.

\- Digital usage and lifestyle features show relationships with stress-level categories.

\- Random Forest and XGBoost provide different levels of predictive performance depending on the target variable.



These findings describe patterns in the analyzed data. They should not be interpreted as proof that any single behavior causes a particular mental health outcome.



\## 🔮 Future Improvements



Potential extensions include:



\- Adding a dedicated model evaluation dashboard.

\- Improving model interpretability using SHAP or other feature-importance techniques.

\- Performing additional robustness and subgroup evaluations.

\- Improving input validation and application error handling.

\- Automating model training and evaluation.

\- Adding reproducible dataset and model versioning.

\- Deploying the Streamlit application to a hosting platform.

\- Expanding the documentation with application screenshots and a detailed evaluation report.



\## ⚠️ Disclaimer



This project is intended for educational, research, and portfolio demonstration purposes.



The predictions are based on machine learning models trained on the available dataset. They are not clinical assessments, mental health diagnoses, or substitutes for professional medical advice.



The results should be interpreted cautiously, as model performance may vary across individuals, populations, and real-world settings.



\---



\## 👤 Author



\*\*Your Name\*\*



Add your GitHub profile, LinkedIn profile, or portfolio website here.

