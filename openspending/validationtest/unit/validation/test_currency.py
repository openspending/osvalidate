
from openspending.reference import currency
from openspending.validation.model.dataset import valid_currency

from ... import TestCase, helpers as h

class TestCurrency(TestCase):
    def test_currency_constant(self):
        h.assert_equal(currency.CURRENCIES['EUR'], ('Euro', True))
        h.assert_equal(currency.CURRENCIES['USD'], ('US Dollar', True))

    def test_currency_type_raises_invalid(self):
        assert valid_currency('not-a-code') is not True

    def test_currency_type_returns_valid(self):
        assert valid_currency('usd') is True

