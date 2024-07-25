import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-interactive use

import matplotlib.pyplot as plt
import io
import base64
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def perform_analysis(data):
    """
    Perform linear regression analysis on the dataset.
    
    :param data: DataFrame containing the dataset.
    :return: Dictionary with analysis results.
    """
    results = {}
    
    # Define independent and dependent variables
    X = data[['X']]
    Y = data['Y']
    
    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    
    # Create and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, Y_train)
    
    # Get the coefficients
    intercept = model.intercept_
    slope = model.coef_[0]
    
    results['intercept'] = intercept
    results['slope'] = slope
    
    # Predict on the test set
    Y_pred = model.predict(X_test)
    
    # Calculate performance metrics
    mse = mean_squared_error(Y_test, Y_pred)
    r2 = r2_score(Y_test, Y_pred)
    
    results['mean_squared_error'] = mse
    results['r_squared'] = r2
    
    # Plot the regression line
    plt.figure()  # Create a new figure
    plt.scatter(X, Y, color='blue', label='Data Points')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression Line')
    plt.legend()
    plt.grid(True)
    
    # Save plot to a BytesIO object and encode it as base64 string
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()  # Close the plot to free up resources
    
    results['plot'] = img_base64
    
    return results
