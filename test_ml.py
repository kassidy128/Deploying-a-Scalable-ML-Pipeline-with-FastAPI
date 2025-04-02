import pytest
import random
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from ml.model import train_model
from train_model import data
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_model_instance():
    """
    Tests if the the model used is the RandomForestClassifer
    """
    X = np.array([[0, 1, 2], [3, 4, 5]])
    y = np.array([0, 1])

    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_age_data_range():
    """
    Tests the age data against the expected range 
    """
    
    assert data['age'].between(0,100).all()


# TODO: implement the third test. Change the function name and input as needed
def test_train_test_split():
    """
    Tests if the test and train datasets have the expected size
    """
    X = np.random.rand(100, 5)
    y = np.random.randint(0, 2, 100)
    
    train_size = 80
    test_size = 20

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    assert len(X_train) == train_size, "Training data size does not match expected size"
    assert len(X_test) == test_size, "Test data size does not match expected size"
    assert len(y_train) == train_size, "Training labels data size does not match expected size"
    assert len(y_test) == test_size, "Testing labels data size does not match expected size"