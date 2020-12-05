import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
from read_data import get_data
import clean_data

data = get_data()
data_clean = clean_data.clean_columns(data)
data_clean_flat = clean_data.flatten_data(data_clean)

#drop additional unnecessary columns
data_use = data_clean_flat.drop(columns=['project_ID','script_ID','project_name','block_rank','block_type'])

#create outcome variables (called "labels") and predictors (called "features")
labels = np.array(data_use[['total_remixes','total_views', 'total_favorites', 'total_loves']])
features = data_use.drop(columns=['total_remixes', 'total_views', 'total_favorites', 'total_loves'])
feature_list = np.array(features.columns)
features = np.array(features)

# create test and training datasets
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 42)

#specify model and fit with multi-outputs
rf = RandomForestRegressor(n_estimators = 100, random_state = 42) # Train the model on training data
model = MultiOutputRegressor(estimator=rf)
model.fit(train_features, train_labels)

#add feature names to model
model.feature_names = list(train_features.columns.values)
#optional scoring checks
#train_score = model.score(train_features, train_labels)
#print("Training score:", train_score)
#test_score = model.score(test_features, test_labels)
#print("Test score:", test_score)

# export fitted model
joblib.dump(model,'fitted_model.sav')
