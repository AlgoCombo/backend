from algorithms.core.baseAlgorithm import BaseAlgorithm
import pandas as pd


class MovingAverageAlgorithm(BaseAlgorithm):
    _name = "Moving Average Algorithm"
    _description = "Moving average algorithm to test algocombo"

    def __init__(self, inputs, timeframe='day', name=None, description=None, *args, **kwargs):
        super().__init__(inputs, timeframe, name, description, *args, **kwargs)

    def clean_data(self):
        df = pd.DataFrame(self._inputs, columns=['timestamp', 'price'])
        return df

    def get_signal(self, short_window=20, long_window=50, day_number=101):
        """
        1=buy, 
        0=hold, 
        -1=sell

        @param short_window: int
        @param long_window: int
        @param day_number: int the day for which the signal is required .ie. for the 101st day, day_number=101
        @return: int the buy/sell signal for the day_number'th day

        given day is the day before the required day to get the signal for
        """
        data = self.clean_data()
        data['Short_MA'] = data['price'].rolling(
            window=short_window, min_periods=1).mean()
        data['Long_MA'] = data['price'].rolling(
            window=long_window, min_periods=1).mean()

        # Generate buy/sell signals based on crossover
        data['Signal'] = 0
        data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1
        data.loc[data['Short_MA'] < data['Long_MA'], 'Signal'] = -1

        # Extract the moving averages for the 101st day
        short_ma_given_day = data.iloc[day_number-2]['Short_MA']
        long_ma_given_day = data.iloc[day_number-2]['Long_MA']

        # Use the moving averages from the given day to predict the signal for the 101st day
        signal_required_day = 0  # Initialize the signal for the required day

        if short_ma_given_day > long_ma_given_day:
            signal_required_day = 1
        elif short_ma_given_day < long_ma_given_day:
            signal_required_day = -1

        return signal_required_day

    def __str__(self):
        return self._name

    def __repr__(self):
        return self._name
