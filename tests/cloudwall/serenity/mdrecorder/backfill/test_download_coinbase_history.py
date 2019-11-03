import datetime
from decimal import Decimal
from datetime import date

from pytest_mock import MockFixture

from cloudwall.serenity.mdrecorder.backfill.download_coinbase_history import backfill_coinbase_trades


def test_backfill_coinbase_trades(mocker: MockFixture):
    mocker.patch('os.makedirs')
    mock_cbp_client = mocker.patch('coinbasepro.PublicClient').return_value
    mock_cbp_client.get_product_historic_rates.return_value = [{'time': datetime.datetime(2019, 7, 20, 4, 0),
                                                                'low': Decimal('10532.15'),
                                                                'high': Decimal('10548.72'),
                                                                'open': Decimal('10532.91'),
                                                                'close': Decimal('10547.58'),
                                                                'volume': Decimal('0.36697351')},
                                                               {'time': datetime.datetime(2019, 7, 20, 3, 59),
                                                                'low': Decimal('10529.07'),
                                                                'high': Decimal('10534.13'),
                                                                'open': Decimal('10529.08'),
                                                                'close': Decimal('10533.51'),
                                                                'volume': Decimal('1.3777413')}]
    mocker.patch('pandas.DataFrame.to_hdf')
    backfill_coinbase_trades(start_date=date(2019, 7, 20), end_date=date(2019, 7, 20))
    assert mock_cbp_client.get_product_historic_rates.call_count == 6
