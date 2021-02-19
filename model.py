import pandas as pd
from joblib import dump
from xgboost.sklearn import XGBRegressor
from sklearn.model_selection import GridSearchCV,  KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, explained_variance_score, r2_score


TRAIN = False

# Load the data file
df = pd.read_csv("dbo.ml_input_predictive_210213.txt")

# Select columns according to feature importance for predicting Predictive score
df = df[['predictive_score', 'relevancy_score', 'students', 'reviews', 'duration', 'rating',
         'p_level_all', 'p_level_int', 'p_level_beg', 'p_level_exp', 'last_updated', 'list_price',
         'cat_match', 'subcat_match', 'topic_match']].copy()

# Drop rows with no values
df.dropna(inplace=True)

# Split the dataframe into train and test set
train_df, test_df = train_test_split(df, train_size=0.90)

# Split training dataframe into training and target dataframes
train_target = train_df.iloc[:, 1].copy()
train_df = train_df.iloc[:, 1:].copy()

# Split testing dataframe into testing and testing target datframes
test_target = test_df.iloc[:, 1].copy()
test_df = test_df.iloc[:, 1:].copy()

# reset index for training and testing dataframes
train_df.reset_index(drop=True, inplace=True)
train_target.reset_index(drop=True, inplace=True)
test_df.reset_index(drop=True, inplace=True)
test_target.reset_index(drop=True, inplace=True)

# Define search parameters dictionary for grid search
n_estimators = [350, 400, 450, 500, 550, 600]
max_depth = [12, 14, 16, 18]
learning_rate = [0.1, 0.2, 0.3]
param_grid = dict(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate)


if __name__ == "__main__":
    if TRAIN:
        # perform 5 Kfold cross validation
        kfold = KFold(n_splits=5, shuffle=True, random_state=786)

        # Define XGBRegressor model
        model = XGBRegressor()

        # Perform grid search to find model with best parameters
        grid_search_model = GridSearchCV(model, param_grid,
                                         scoring=('explained_variance', 'r2', 'neg_mean_absolute_error',
                                                  'neg_mean_squared_error',
                                                  'neg_root_mean_squared_error'), cv=kfold,
                                         refit='neg_mean_absolute_error', verbose=10, n_jobs=1)

        grid_search_model.fit(train_df, train_target)

        print(" Results from Grid Search ")
        print("\n The best estimator across ALL searched params:\n",
              grid_search_model.best_estimator_)
        print("\n The best score across ALL searched params:\n",
              grid_search_model.best_score_)
        print("\n The best parameters across ALL searched params:\n",
              grid_search_model.best_params_)

        # Predict the test target using the gridsearch model
        predictions = grid_search_model.predict(test_df)

        print("R2_score: ", r2_score(test_target, predictions))
        print("mean absolute error: ", mean_absolute_error(test_target, predictions))
        print("explained variance: ", explained_variance_score(test_target, predictions))

        dump(grid_search_model, 'models/XGBRegressor_model.pkl')

        print("Training completed")
    else:
        print("Training not enabled. Please find trained model in the models directory or enable training.")







