from cmath import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from db.db_accessor import add_entry_to_db, delete_all_entries, add_model, get_all_entries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from joblib import dump, load
from model.blob_accessor import load_model, save_model

def predict(area, rooms, zip, model):
    try:
        regressor = load_model(model)
        print("Model:")
        print(regressor)
    except (EOFError, FileNotFoundError) as e:
        optimize_model()
        regressor = load('model.joblib')
    new_property_features = [[area, rooms, zip]]
    predicted_rent = regressor.predict(new_property_features)
    print("predicted Rent: " + str(predicted_rent))
    return str(predicted_rent[0])

def train(documents_df, n_estimators, max_depth):

    features = documents_df[['area', 'rooms', 'zip']].values
    target = documents_df['rent'].values

    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    regressor = RandomForestRegressor(n_estimators=n_estimators, random_state=42, max_depth=max_depth)

    regressor.fit(X_train, y_train)

    y_pred = regressor.predict(X_test)

    r_squared = r2_score(y_test, y_pred)

    print(f"R-squared: {r_squared}")

    return (r_squared, regressor)

def optimize_model():
    best = {
        'r_squared': 0,
        'n_estimators': 0,
        'max_depth': 0,
    }

    param_grid = {
        'n_estimators': (10, 100),
        'max_depth': (1, 10)
    }

    documents_df = get_all_entries()
    
    for max_depth in range(param_grid['max_depth'][0], param_grid['max_depth'][1]):
                for n_estimators in range(param_grid['n_estimators'][0], param_grid['n_estimators'][1]):
                    result = train(documents_df, n_estimators, max_depth)
                    r_squared = result[0]
                    if r_squared > best['r_squared']:
                        best['n_estimators'] = n_estimators
                        best['r_squared'] = r_squared
                        best['max_depth'] = max_depth
    
    best_model = train_model_once(documents_df, best['n_estimators'], best['max_depth'])

    name = save_model(best_model)

    add_model(best['r_squared'], len(documents_df), name)

    print(f"The best model: {best}")

def train_model_once(documents_df, n_estimators, max_depth):
    features = documents_df[['area', 'rooms', 'zip']].values
    target = documents_df['rent'].values

    regressor = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, random_state=42)

    regressor.fit(features, target)

    return regressor

if __name__ == "__main__":
    optimize_model()