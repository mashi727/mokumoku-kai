import backtrader as bt
import yfinance as yf

class TurtleStrategy(bt.Strategy):
    params = (('long_period', 20), ('short_period', 10),)

    def __init__(self):
        self.order = None
        self.buy_price = None
        self.buy_comm = None

        self.high = bt.indicators.Highest(self.data.high, period=self.p.long_period)
        self.low = bt.indicators.Lowest(self.data.low, period=self.p.short_period)

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('BUY EXECUTED, %.2f' % order.executed.price)
            elif order.issell():
                self.log('SELL EXECUTED, %.2f' % order.executed.price)

        self.order = None

    def next(self):
        if self.order:
            return

        if not self.position:
            if self.data.close > self.high:
                self.log('BUY CREATE, %.2f' % self.data.close[0])
                self.order = self.buy()

        else:
            if self.data.close < self.low:
                self.log('SELL CREATE, %.2f' % self.data.close[0])
                self.order = self.sell()

    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(f'{dt.isoformat()}, {txt}')


def run_backtest():
    cerebro = bt.Cerebro()

    data = yf.download('AAPL','2000-01-01','2023-05-31')
    datafeed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(datafeed)

    cerebro.addstrategy(TurtleStrategy)
    cerebro.broker.setcash(100000.0)

    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())

if __name__ == '__main__':
    run_backtest()