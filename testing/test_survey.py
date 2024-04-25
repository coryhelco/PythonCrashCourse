import pytest
from survey import AnonymousSurvey

@pytest.fixture
def my_survey():
    """Create a survey instance for all tests."""
    question = "What language did you first learn to speak?"
    anonymous_survey = AnonymousSurvey(question)
    return anonymous_survey

def test_store_single_response(my_survey):
    """Test that a single response is stored properly."""
    my_survey.store_response('English')
    assert 'English' in my_survey.response

def test_store_three_responses(my_survey):
    """Test that three individual responses are stored properly."""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        my_survey.store_response(response)

    for response in responses:
        assert response in my_survey.response