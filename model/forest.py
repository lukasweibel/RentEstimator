from cmath import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from db.db_accessor import add_entry_to_db, delete_all_entries, get_all_entries
import pandas as pd
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def train(documents_df, n_estimators, max_depth, min_samples_split, min_samples_leaf):

    #print(documents_df)

    features = documents_df.iloc[:, 1:].values
    target = documents_df['rent'].values

    #print(target)
    #print(features)

    # Splitting the dataset into training and testing set
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

    # Initialize the Random Forest Regressor
    #regressor = RandomForestRegressor(n_estimators=n_estimators, random_state=42, max_depth=max_depth, min_samples_leaf=min_samples_leaf, min_samples_split=min_samples_split)
    regressor = RandomForestRegressor(n_estimators=n_estimators, random_state=42, max_depth=max_depth)

    # Fit the regressor to the training data
    regressor.fit(X_train, y_train)

    # Predicting on the test set
    y_pred = regressor.predict(X_test)

    # Evaluating the model
    #rmse = sqrt(mean_squared_error(y_test, y_pred))
    #print(f"RMSE: {rmse}")

    new_property_features = [[27, 1, 8400]]

    # Predicting the rent using the trained regressor
    #predicted_rent = regressor.predict(new_property_features)

    #print(f"Predicted rent for the new property: {predicted_rent[0]}")

    r_squared = r2_score(y_test, y_pred)

    print(f"R-squared: {r_squared}")

    return r_squared

def run():
    best = {
        'r_squared': 0,
        'n_estimators': 0,
        'max_depth': 0,
        'min_samples_split': 0,
        'min_samples_leaf': 0,
    }

    param_grid = {
        'n_estimators': (1, 20),
        'max_depth': (1, 50),
        'min_samples_split': (1, 2),
        'min_samples_leaf': (1, 2),
    }

    documents_df = get_all_entries()
    
    for max_depth in range(param_grid['max_depth'][0], param_grid['max_depth'][1]):
        for min_samples_split in range(param_grid['min_samples_split'][0], param_grid['min_samples_split'][1]):
            for min_samples_leaf in range(param_grid['min_samples_leaf'][0], param_grid['min_samples_leaf'][1]):
                for n_estimators in range(param_grid['n_estimators'][0], param_grid['n_estimators'][1]):
                    #r_squared = train(documents_df, n_estimators, max_depth, min_samples_split/10, min_samples_leaf)
                    r_squared = train(documents_df, n_estimators, max_depth, min_samples_split/10, min_samples_leaf)
                    if r_squared > best['r_squared']:
                        best['n_estimators'] = n_estimators
                        best['r_squared'] = r_squared
                        best['max_depth'] = max_depth
                        best['min_samples_split'] = min_samples_split/10
                        best['min_samples_leaf'] = min_samples_leaf
    print(f"The best so far: {best}")
    
    print('')
    print('The best result:')
    print(best)
        

if __name__ == '__main__':
    run()