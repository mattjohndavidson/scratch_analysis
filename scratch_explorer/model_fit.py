import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
import clean_data
import os

def fit_model(data):
    """
    Process data and fit RF regression model
    
    
    Creates outcome variables (called "labels") and predictors (called "features")
    Create testing and training datasets
    Creates model object
    Fits model object
    Calculates and stores model diagnostics

    Params
    -------
    data: a pandas dataframe with popularity scores, and a set of predictors

    Returns
    -------
    feature_list: List of feature names
    model: fitted multi output RF regression model
    diagnostics: various diagnostics about the fitted model

    """
    #clean and format data
    data_clean = clean_data.clean_columns(data)
    data_clean_flat = clean_data.flatten_data(data_clean)
    data_use = data_clean_flat.drop(columns=['project_ID','script_ID','project_name','block_rank','block_type'])

    labels = np.array(data_use[['total_remixes','total_views', 'total_favorites', 'total_loves']])
    features = data_use.drop(columns=['total_remixes', 'total_views', 'total_favorites', 'total_loves'])
    feature_list = list(features.columns)
    features = np.array(features)

    # create test and training datasets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.10, random_state = 1111)

    #create and fit model
    rf = RandomForestRegressor(n_estimators = 100) # Train the model on training data
    model = MultiOutputRegressor(estimator=rf)
    model.fit(train_features, train_labels)

    #create diagnostics
    """
    train_score = model.score(train_features, train_labels)
    test_score = model.score(test_features, test_labels)
    return train_score, test_score

    #get the avg for each pop metric as baselines for base line errors
    # out of model scoring fit, also out of model prediction
    # for each pop metric
    #'total_remixes','total_views', 'total_favorites', 'total_loves'
    # 0                  1               2                   3
    # The baseline predictions are the historical averages
    #baseline_preds = test_features[:, feature_list.index('average')]
    # Baseline errors, and display average baseline error
    #baseline_errors = abs(baseline_preds - test_labels)
    # Use the forest's predict method on the test data
    #predictions = rf.predict(test_features)
    # Calculate the absolute errors
    #errors = abs(predictions - test_labels)
    #add nrow for number of projects used for test/train etc
    """
    return feature_list, model, diagnostics

def export_files(model, feature_list, diagnostics):
    """
    Writes files to disk for use by Dash app
    
    Params
    ------
    model: fitted sklearn model object
    feature_list: list of features used by model
    diagnostics: model diagnostics

    Returns
    -------
    None; writes files to disk
    """
    dirname = os.path.dirname(__file__)
    filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
    filename_features = os.path.join(dirname, 'exports/feature_list.sav')
    filename_diagnostics = os.path.join(dirname, 'exports/diagnostics.sav')
    joblib.dump(model, filename_model)
    joblib.dump(feature_list, filename_features)
    joblib.dump(diagnostics, filename_diagnostics)
