
# Bank Note Authentication

This is a **Bank Note Authentication Prediction** project, in which I tried to build a **Machine Learning Model** which helps we can check whether the note is original or duplicate, You can click on the below link and go to the web app to check how it is looking and working.

[Go To The Web App](https://banknoteauthenticationwebapp.herokuapp.com/)

![Bank Note Authentication Prediction](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Web_App_1.png)

**Domain = Banking**

**Level = Beginner**

**Accuracy Score = 99%>**

**Project Type = End To End Project**

![User Libraries](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/li_im.jpg)

## Table Of Content
- Problem Statement
- Data Collection 
- Data Description
- Data Preprocessing
- Handle Outliers 
- Exploratory Data Analysis (EDA)
- Feature Selection
- Data Scaling
- Model Building
- Model Performances & Feature Importance
- Make Pickle File
- Create New Enviornment
- Create Web App With Streamlit
- Upload All Files In Github repository
- Deploy Model On Heroku

**Web App Overview**

![Bank Not Authentication Web App](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Web_App_2.png)
## Problem Statement

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images

In a simple word, we have to build a model which helps anyone can check the note is orignal or duplicate
## Data Collection
I got this dataset from kaggle, first I downloaded dataset in my local storage then uploaded in Github Repo and then imported in jupyter notebook

```
df = pd.read_csv('https://raw.githubusercontent.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/main/BankNote_Authentication.csv')

```
**Data Overview**

![Data Overview](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Data_Overview.png)
## Data Description

The Bank Note Authentication Prediction dataset has 1372 rows and 5 columns. This data frame contains the following columns:

variance - 
variance of Wavelet Transformed image (continuous)

skewness -
skewness of Wavelet Transformed image (continuous)

curtosis -
curtosis of Wavelet Transformed image (continuous)

entropy -
entropy of image (continuous)

class -
Output Value (categorical)


## Data Preprocessing
In this step first I checked there are any null and duplicate values present or not, and I found there are no 
null values present but some duplicate values was there, I dropped them and check there are any incorrect data 
present or not, and I found there was no wrong data.

![Data Preprocessing ](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Data_Preprocessing.png)

## Handle outliers
After correcting incorrect data, I checked whether there are any outliers present or not, and I found that there was some amount 
of outliers present, for more clarification, I used the IQR method to check outliers and I found there were some outliers and I dropped them.

![Outliers 1](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Outliers_1.png)
![Outliers 2](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Outliers_2.png)
![Outliers 3](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Outliers_3.png)
![Outliers 4](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Outliers_4.png)

## Exploratory Data Analysis (EDA)
In this step I tried to Analyze the data very efficiently and deeply, first I checked correlation between features, 
then check feature distribution and then relation between features and target by graph

![EDA 1](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/EDA_1.png)
![EDA 2](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/EDA_2.png)
![EDA 3](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/EDA_3.png)

## Feature Selection
In this step first I splits features and target, then splits data into train
and test data

```
# split data into features and target
X = dfs.drop('class',axis = 1)
y = dfs['class']
```

```
# import train test split to split train and test data
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y, test_size=0.2)
```

## Data Scaling

After data Spliting I scaled features train and test data 

```
# import standard scaler to scale data
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
```

## Model Building
In this step, I build different - different models and checked their performance, and then chose the best model for the dataset

![Model 1](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Model_1.png)
![Model 2](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Model_2.png)

## Model Performances & Feature Importance
After model Building, I checked their performance by accuracy score and the model whose accuracy score was higher I consider that model to be a final model and then I checked important features based on that model 

![Model Performance](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Model_Performance.png)
![Feature Importance](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Feature_Importance.png)

## Make Pickle File
After getting score from the best model I created a Pickle file for the web app

```
import pickle as pkl
pkl.dump(greed_rfc, (open('bna_model.pkl','wb')))
```

## Create New Enviornment
After making pickle file I created new virtual environment for the 
project and install required libraries and created web app in VS Code IDE

```
conda create -p banknote python==3.9 -y
```

```
pip install streamlit numpy pandas sklearn
``` 

## Create Web App With Streamlit
After installing all required libraries and dependencies I created web app 

![Web App 2](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Web_App_2.png)

## Upload All Files In Github repository

After creating web app I uploaded all files in github repository by git CLI
```
git config --global user.name "FIRST_NAME LAST_NAME"
```

```
git config --global user.email "myemail@gmail.com"
```

```
git add files_name
```

```
git commit -m  "about the commit"
```

```
git push origin main
```

## Deploy Model On Heroku

In the end, I deployed the model on Heroku, so that anybody can use the web app

[Bank Note Authentication Prediction Web App](https://banknoteauthenticationwebapp.herokuapp.com/)

![Bank Note Authentication Prediction](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/Web_App_1.png)

## Deployment Requirement Tools 

![Deploy](https://github.com/vishalkrishna90/BANK-NOTE-AUTHENTICATION-PREDICTION/blob/main/Images/li_im.jpg)

 - [Streamlit](https://streamlit.io/)
 - [Github Account](https://github.com/)
 - [Heroku Account](https://dashboard.heroku.com/apps)
 - [Visual Studio Code](https://code.visualstudio.com/)
 - [Git CLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)


