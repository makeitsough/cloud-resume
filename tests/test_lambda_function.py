import pytest
from unittest.mock import MagicMock

import os
import sys

# Add root directory to Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

# Import handler function
from updateDB.lambda_function import handler

@pytest.fixture
def mock_dynamodb_resource():
    return MagicMock()

def test_handler_with_mock_dynamodb_resource(mock_dynamodb_resource):
    # Set up the mock response for get_item
    mock_dynamodb_resource.Table.return_value.get_item.return_value = {
        'Item': {
            'id': '0',
            'views': 5
        }
    }

    # Invoke the handler with a sample event
    event = {
        'key1': 'value1',
        'key2': 'value2'
    }
    context = None
    result = handler(event, context, dynamodb_resource=mock_dynamodb_resource)

    # Assert that the result is an integer
    assert isinstance(result, int)
