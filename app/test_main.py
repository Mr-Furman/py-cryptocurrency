from unittest import mock

from app.main import cryptocurrency_action


def test_cryptocurrency_action_buy() -> None:
    current_rate = 100
    prediction_rate = 120
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        action = cryptocurrency_action(current_rate)

    assert action == "Buy more cryptocurrency"


def test_cryptocurrency_action_sell() -> None:
    current_rate = 100
    prediction_rate = 80
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        action = cryptocurrency_action(current_rate)

    assert action == "Sell all your cryptocurrency"


def test_cryptocurrency_action_do_nothing() -> None:
    current_rate = 100
    prediction_rate = 105
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        action = cryptocurrency_action(current_rate)

    assert action == "Do nothing"


def test_cryptocurrency_action_do_nothing2() -> None:
    current_rate = 100
    prediction_rate = 95
    with mock.patch("app.main.get_exchange_rate_prediction",
                    return_value=prediction_rate):
        action = cryptocurrency_action(current_rate)

    assert action == "Do nothing"
