import pytest
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from HeartFailure.config import config
from HeartFailure.processing.data_handling import load_dataset
from HeartFailure.predict import generate_predictions

@pytest.fixture
def single_prediction():
    test_dataset = load_dataset(config.TEST_FILE)
    single_row = test_dataset[:1]
    result = generate_predictions(single_row)
    return result

def test_single_pred_not_none(single_prediction):
    assert single_prediction is not None

def test_single_pred_int_type(single_prediction):
    assert isinstance(single_prediction.get("Predictions")[0], str)

def test_single_pred_validate(single_prediction):
    assert single_prediction.get("Predictions")[0] == "High Risk"
