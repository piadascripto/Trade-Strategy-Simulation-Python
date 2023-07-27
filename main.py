import random
import statistics
import itertools


def calculate_trades():
    investment = 2000
    trades_day = 3.0
    strategy_efficiency = 0.85
    order_amount = 5 / 100
    highest_order_amount = 15000
    gain_percentage = 0.12
    loss_percentage = -0.30
    years_to_simulate = 1
    trades_within_year = trades_day * 252 * years_to_simulate

    trades = []
    highest_amount = 0

    def array_trades(investment):
        nonlocal highest_amount
        trades_quantity = 0

        def get_trade_amount():
            _order_amount = order_amount * investment
            actual_order_amount = min(_order_amount, highest_order_amount)
            return actual_order_amount

        while trades_quantity <= trades_within_year:
            trade_result = gain_percentage * get_trade_amount() if random.random() < strategy_efficiency else loss_percentage * get_trade_amount()
            investment += trade_result
            highest_amount = max(highest_amount, investment)
            trades.append(trade_result)
            trades_quantity += 1

        return trades

    all_simulated_trades = []
    for i in range(50):
        trades = array_trades(investment)
        all_simulated_trades.append({
            'Highest Amount': highest_amount,
            'Trades': trades
        })

    highest_amounts = [item['Highest Amount'] for item in all_simulated_trades]

    average = statistics.mean(highest_amounts)
    std_deviation = statistics.stdev(highest_amounts)

    min_highest_amount = min(highest_amounts)
    max_highest_amount = max(highest_amounts)

    minus_two_std_deviation = average - 2 * std_deviation
    plus_two_std_deviation = average + 2 * std_deviation

    lowest_highest_amounts = [item['Trades'] for item in all_simulated_trades if item['Highest Amount'] == min_highest_amount]
    highest_highest_amounts = [item['Trades'] for item in all_simulated_trades if item['Highest Amount'] == max_highest_amount]

    print("======Simulate " + str(years_to_simulate) + " years of trading===========")
    print("Min of $ to achieve:", min_highest_amount)
    print("-2 Standard Deviation:", minus_two_std_deviation)
    print("Average $:", average)
    print("+2 Standard Deviation:", plus_two_std_deviation)
    print("Max of $ to achieve:", max_highest_amount)


    # Accumulate trades for lowest_highest_amounts
    accumulated_lowest_trades = list(itertools.chain.from_iterable(lowest_highest_amounts))
    accumulated_lowest_trades = list(itertools.accumulate(accumulated_lowest_trades))

    # Accumulate trades for highest_highest_amounts
    accumulated_highest_trades = list(itertools.chain.from_iterable(highest_highest_amounts))
    accumulated_highest_trades = list(itertools.accumulate(accumulated_highest_trades))





calculate_trades()