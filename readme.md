# 🧠 Student Digital Wellbeing Predictor

### Predicting Student Stress Levels and Mental Health Scores Using Machine Learning

A machine learning project that analyzes students' demographic characteristics, digital usage patterns, and lifestyle habits to predict **Stress Levels** and **Mental Health Scores**.

This project combines exploratory data analysis, feature engineering, machine learning model comparison, hyperparameter tuning, and an interactive Streamlit application to demonstrate the application of machine learning to student digital wellbeing.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-objectives)
- [Application Screenshots](#-application-screenshots)
- [Prediction Targets](#-prediction-targets)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Model Selection and Evaluation](#-model-selection-and-evaluation)
- [Project Structure](#-project-structure)
- [Installation and Setup](#-installation-and-setup)
- [Running the Application](#-running-the-application)
- [Model Files](#-model-files)
- [Key Insights](#-key-insights)
- [Future Improvements](#-future-improvements)
- [Disclaimer](#-disclaimer)
- [Author](#-author)

---

## 📖 Project Overview

Digital technology and social media are an integral part of students' daily lives. Digital usage patterns, sleep, physical activity, and study habits may be associated with stress levels and mental wellbeing.

This project uses machine learning to explore these relationships and predict two outcomes:

1. **Stress Level Prediction:** Classifies a student's stress level into one of four categories.
2. **Mental Health Score Prediction:** Estimates a numerical mental health score.

The project includes a Jupyter Notebook for exploratory data analysis and model development, along with a Streamlit application that allows users to enter their information and view both predictions through interactive gauges.

## 🎯 Objectives

- Explore relationships between student digital behavior, lifestyle habits, and wellbeing.
- Perform exploratory data analysis (EDA) to understand the dataset.
- Engineer additional features from digital usage and phone unlock frequency.
- Compare Random Forest and XGBoost algorithms.
- Evaluate classification and regression models using appropriate performance metrics.
- Apply hyperparameter tuning to improve model performance.
- Develop an interactive application for generating both predictions.
- Present machine learning predictions through intuitive visualizations.

---

## 🖥️ Application Screenshots

The Streamlit application provides an interactive interface for entering student information and generating stress-level and mental-health-score predictions.

### 1. Personal Information

Users can enter demographic information, including age, gender, country, and academic level.

![Personal Information](Application%20Screenshots/input1.jpg)

### 2. Digital Usage and Lifestyle

Users can provide information about digital usage patterns, phone unlock frequency, study hours, physical activity, and sleep duration.

![Digital Usage and Lifestyle](Application%20Screenshots/input2.jpg)

### 3. Prediction Results

The application displays the predicted stress level and mental health score through interactive gauges.

![Prediction Results](Application%20Screenshots/output.jpg)

---

## 🔍 Prediction Targets

### 1. Stress Level — Classification

**Target variable:** `Stress_Level`

The classification model predicts one of four stress-level categories:

- Low
- Medium
- High
- Very High

The model is evaluated using classification metrics, including accuracy and weighted F1 score, alongside cross-validation.

**Selected model:** Baseline Random Forest Classifier.

### 2. Mental Health Score — Regression

**Target variable:** `Mental_Health_Score`

The regression model estimates a numerical mental health score based on the input features.

The model is evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² score
- Cross-validation

**Selected model:** Tuned Random Forest Regressor.

The targets are modeled separately because stress level is categorical, whereas mental health score is numerical.

## ✨ Key Features

- **Dual prediction:** Predicts stress level and mental health score from the same set of inputs.
- **Exploratory data analysis:** Examines feature distributions and relationships with both prediction targets.
- **Feature engineering:** Creates additional features related to screen usage and phone unlock frequency.
- **Model comparison:** Evaluates Random Forest and XGBoost algorithms.
- **Hyperparameter tuning:** Uses RandomizedSearchCV to explore Random Forest configurations.
- **Interactive application:** Collects personal, digital usage, and lifestyle information through Streamlit.
- **Visual predictions:** Displays both prediction results using interactive Plotly gauges.
- **Reproducible workflow:** Includes the Jupyter Notebook, application source code, and dependency list.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical operations |
| Scikit-learn | Preprocessing, machine learning pipelines, model evaluation, and hyperparameter tuning |
| XGBoost | Gradient-boosting model comparison |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Jupyter Notebook | Exploratory data analysis and model development |
| Streamlit | Interactive web application |
| Plotly | Interactive prediction gauges |
| Joblib | Saving and loading trained models |
| KaggleHub | Dataset download in the notebook |

---

## ⚙️ Machine Learning Workflow

The project follows a structured machine learning workflow.

1. **Data acquisition:** Downloads the dataset using KaggleHub.
2. **Data understanding:** Examines dataset structure, variables, missing values, and duplicate records.
3. **Exploratory data analysis:** Studies feature distributions and relationships with the prediction targets.
4. **Feature engineering:** Derives additional features from digital usage patterns.
5. **Data preprocessing:** Prepares numerical and categorical features for model training.
6. **Baseline modeling:** Trains Random Forest models for classification and regression.
7. **Model comparison:** Evaluates XGBoost alternatives against Random Forest models.
8. **Hyperparameter tuning:** Uses RandomizedSearchCV with cross-validation to tune Random Forest models.
9. **Model evaluation:** Compares performance using classification and regression metrics.
10. **Model saving:** Saves the selected models as `.pkl` files.
11. **Application development:** Loads the trained models into a Streamlit application to generate predictions.

### Engineered Features

The application calculates two additional features from user inputs:

| Feature | Description |
|---|---|
| `Screen_Nonscreen_Ratio` | Ratio of average daily screen usage hours to non-screen hours |
| `Unlocks_Per_Usage_Hour` | Number of phone unlocks per hour of digital usage |

These features provide additional representations of digital usage behavior.

---

## 📊 Model Selection and Evaluation

The project evaluates Random Forest and XGBoost algorithms for both prediction targets.

### Model Comparison

| Prediction Target | Algorithms Evaluated | Selected Model |
|---|---|---|
| Stress Level (Classification) | Random Forest Classifier and XGBoost Classifier | Baseline Random Forest Classifier |
| Mental Health Score (Regression) | Random Forest Regressor and XGBoost Regressor | Tuned Random Forest Regressor |

### Stress Level Classification

The notebook reports the following results for the baseline Random Forest Classifier.

| Evaluation Metric | Result |
|---|---:|
| Test Accuracy | 89.9% |
| Weighted F1 Score | 0.899 |
| Cross-Validation Accuracy | 0.871 |
| Cross-Validation Weighted F1 Score | 0.870 |

The baseline Random Forest Classifier was selected based on its reported performance in the model comparison.

### Mental Health Score Regression

The notebook reports the following results for the tuned Random Forest Regressor.

| Evaluation Metric | Result |
|---|---:|
| R² Score | 0.913 |
| Root Mean Squared Error (RMSE) | 0.39 |
| Mean Absolute Error (MAE) | 0.289 |
| Cross-Validation R² Score | 0.891 |

The tuned Random Forest Regressor was selected based on its reported performance in the regression model comparison.

**Note:** These are the results reported in the notebook. They describe performance on the evaluated dataset and do not guarantee equivalent performance on new data or populations.

---

## 📁 Project Structure

The repository is organized as follows:

```text
student-digital-wellbeing-predictor/
│
├── Application Screenshots/
│   ├── input1.jpg
│   ├── input2.jpg
│   └── output.jpg
│
├── Dataset/
│   └── Student Social Media And Mental Health Impact.csv
│
├── .gitignore
├── mhs_app.py
├── readme.md
├── requirements.txt
└── student_digital_wellbeing_predictor.ipynb
```

The trained model files are intentionally excluded from GitHub:

- `stress_level_model.pkl`
- `mental_health_score_model.pkl`

These files must be generated locally or obtained separately before running the application.

## 🚀 Installation and Setup

### Prerequisites

Install the following:

- Python
- Git
- Jupyter Notebook or JupyterLab

### Step 1: Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/student-digital-wellbeing-predictor.git
```

Navigate to the project directory:

```bash
cd student-digital-wellbeing-predictor
```

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

The requirements file should include the packages needed by the application and notebook, such as Streamlit, Pandas, Joblib, Plotly, Scikit-learn, XGBoost, KaggleHub, and the visualization libraries used in the notebook.

### Step 4: Generate the Trained Models

Open the Jupyter Notebook:

```bash
jupyter notebook student_digital_wellbeing_predictor.ipynb
```

Execute the notebook cells in the required order, including the model-training and model-saving sections.

The selected models should be saved as:

```text
stress_level_model.pkl
mental_health_score_model.pkl
```

The notebook requires access to the dataset source and the appropriate Python dependencies. Model training and hyperparameter tuning may take some time.

Before continuing, verify that both `.pkl` files exist in the project root.

---

## ▶️ Running the Application

Once both trained model files have been generated, run the following command from the project root:

```bash
streamlit run mhs_app.py
```

Streamlit will start a local web server and display a URL in the terminal. Open that URL in your browser to use the application.

### Application Inputs

The application collects information in three categories.

**Personal Information**
- Age
- Gender
- Country
- Academic level

**Digital Usage**
- Most-used platform
- Purpose of use
- Average daily usage hours
- Daily phone unlocks

**Lifestyle**
- Study hours per day
- Physical activity hours per day
- Sleep hours per night

### Prediction Results

After entering the required information and clicking **Predict**, the application displays:

- **Stress Level:** A predicted category displayed using an interactive gauge.
- **Mental Health Score:** A predicted numerical score displayed using an interactive gauge.

Both predictions are generated from the trained models using the same input information.

## 📦 Model Files and GitHub

The trained `.pkl` files are excluded from GitHub using `.gitignore` to avoid uploading large binary files.

The application loads these files from the project root:

```python
stress_model = joblib.load("stress_level_model.pkl")
mhs_model = joblib.load("mental_health_score_model.pkl")
```

Consequently, cloning the repository alone is not sufficient to run the application. You must generate the model files by executing the relevant training and saving cells in the notebook or obtain compatible model files separately.

The `.gitignore` configuration prevents Git from tracking these files when they are not already tracked. It does not delete the files from your local machine.

---

## 💡 Key Insights

The notebook's exploratory analysis identifies relationships worth investigating:

- Average daily usage hours and daily phone unlock frequency show negative associations with mental health scores in the analyzed dataset.
- Sleep duration, study hours, and physical activity show positive associations with mental health scores in the analyzed dataset.
- Digital usage and lifestyle features show relationships with stress-level categories.
- Random Forest and XGBoost provide different levels of predictive performance depending on the target variable.

These observations describe patterns in the analyzed dataset. They do not establish causation or prove that a particular behavior directly causes a specific mental health outcome.

## 🔮 Future Improvements

Potential improvements include:

- Adding a model evaluation dashboard.
- Improving model interpretability using SHAP or other feature-importance techniques.
- Conducting additional robustness and subgroup evaluations.
- Improving input validation and application error handling.
- Automating model training and evaluation.
- Adding reproducible dataset and model versioning.
- Deploying the Streamlit application to a hosting platform.
- Expanding the documentation with additional screenshots and evaluation results.

## ⚠️ Disclaimer

This project is intended for educational, research, and portfolio demonstration purposes.

The predictions are generated by machine learning models trained on the available dataset. They are not clinical assessments, mental health diagnoses, or substitutes for professional medical advice.

The results should be interpreted cautiously because model performance may vary across individuals, populations, and real-world settings.

---

## 👤 Author

**Biprasish Singha**

- GitHub: [biprasish-singha](https://github.com/biprasish-singha)

---

If you find this project useful, feel free to explore the repository and its machine learning workflow.