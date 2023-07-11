import random

def calculate_trades():
	investment = 2000
	broken = -investment
	trades_day = 4.0
	strategy_efficiency = 0.85
	trade_amount = 5 / 100
	highest_trade_amount = 10000
	gain_percentage = 0.12
	loss_percentage = -0.30
	investment_goal = 1000000

	trades = []
	num_trade = 0

	def array_trades(investment):
		nonlocal num_trade
		highest_amount = investment
		num_trade = 0

		def get_trade_amount():
			_trade_amount = trade_amount * investment
			actual_trade_amount = min(_trade_amount, highest_trade_amount)
			return actual_trade_amount

		while investment <= investment_goal and investment > broken:
			trade_result = gain_percentage * get_trade_amount() if random.random() < strategy_efficiency else loss_percentage * get_trade_amount()
			investment += trade_result
			highest_amount = max(highest_amount, investment)
			trades.append(trade_result)
			num_trade += 1

		return trades

	all_array_trades = []
	for i in range(1000):
		trades = array_trades(investment)
		all_array_trades.append({
			'numTrade': num_trade,
			'trades': trades
		})

	lowest_num_trade = min(item['numTrade'] for item in all_array_trades)
	max_num_trade = max(item['numTrade'] for item in all_array_trades)
	print("======To achieve USD " + str(investment_goal) + "===========")
	print("Lowest number of trades:", lowest_num_trade)
	print("Maximum number of trades:", max_num_trade)
	print("=========Years===========")
	print("Min of years to achive:", lowest_num_trade / trades_day / 252)
	print("Max of years to achive:", max_num_trade / trades_day / 252)


calculate_trades()
