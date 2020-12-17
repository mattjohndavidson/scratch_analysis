import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
from sklearn.model_selection import train_test_split
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
    
    #replacing dashes with underscores
    data = data.dropna()
    data.columns = [i.replace('-', '_') for i in data.columns]
    data_use = data.drop(columns=['p_ID','project_name','username'])
    
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
    train_score = model.score(train_features, train_labels)
    test_score = model.score(test_features, test_labels)
    
    #get the average for each popularity metric as baselines
    baseline_predictions = ([test_labels[0].mean(), test_labels[1].mean(), test_labels[2].mean(),
                             test_labels[3].mean()])
    baseline_errors = abs(baseline_predictions - test_labels)
    predictions = model.predict(test_features)
    errors = abs(predictions - test_labels)
    observations = test_features.shape[0]
    
    diagnostics = {'train_score': train_score,
                   'test_score': test_score,
                   'baseline_error': baseline_errors.mean(),
                   'test_error': errors.mean(),
                   'observations': observations}
    return model, feature_list, diagnostics

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
    feature_imps = pd.DataFrame(columns=["Importance"], index=feature_list)
    for i in range(3):
        feature_imps[i] = model.estimators_[i].feature_importances_
    feature_imps = feature_imps.sort_values("Importance", ascending=False)
    model_features = feature_imps.index[:10]
    
    dirname = os.path.dirname(__file__)
    filename_model = os.path.join(dirname, 'exports/fitted_model.sav')
    filename_features = os.path.join(dirname, 'exports/feature_list.sav')
    filename_diagnostics = os.path.join(dirname, 'exports/diagnostics.sav')
    joblib.dump(model_features, filename_model)
    joblib.dump(feature_list, filename_features)
    joblib.dump(diagnostics, filename_diagnostics)

def main(): 
    """
    Runs model fit module with full dataset

    example usage in terminal from root dir of repo: 
    python scratch_explorer/model_fit.py
    """
    filename_data = os.path.join('scratch_explorer/data/scratch_sample.csv')
    data = pd.read_csv(filename_data)
    model, feature_list, diagnostics = fit_model(data)
    export_files(model, feature_list, diagnostics)

if __name__== "__main__":
    main()
