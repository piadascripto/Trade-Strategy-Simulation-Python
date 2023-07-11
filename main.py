import random
import statistics

def calculate_trades():
	investment = 2000
	broken = -investment
	trades_day = 4.0
	strategy_efficiency = 0.85
	order_amount = 5 / 100
	highest_order_amount = 15000
	gain_percentage = 0.12
	loss_percentage = -0.30
	investment_goal = 1000000

	trades = []
	trades_quantity = 0

	def array_trades(investment):
		nonlocal trades_quantity
		highest_amount = investment
		trades_quantity = 0

		def get_trade_amount():
			_order_amount = order_amount * investment
			actual_order_amount = min(_order_amount, highest_order_amount)
			return actual_order_amount

		while investment <= investment_goal and investment > broken:
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
			'Quantity_of_trades': trades_quantity,
			'Trades': trades
		})


	quantity_of_trades = [item['Quantity_of_trades'] for item in all_simulated_trades]
	
	average = statistics.mean(quantity_of_trades)
	std_deviation = statistics.stdev(quantity_of_trades)
	
	min_trades_quantity = min(quantity_of_trades)
	max_trades_quantity = max(quantity_of_trades)
	
	minus_two_std_deviation = (average - 2 * std_deviation) 
	plus_two_std_deviation = (average + 2 * std_deviation) 
	
	print("======To achieve USD " + str(investment_goal) + "===========")
	print("Lowest number of trades:", min_trades_quantity)
	print("Maximum number of trades:", max_trades_quantity)
	print("=========Years===========")
	print("Min of years to achive:", min_trades_quantity / trades_day / 252)
	print("-2 Standard Deviation:", minus_two_std_deviation / trades_day / 252)
	print("Average years:", average / trades_day / 252)
	print("+2 Standard Deviation:", plus_two_std_deviation / trades_day / 252)
	print("Max of years to achive:", max_trades_quantity / trades_day / 252)



	



calculate_trades()
