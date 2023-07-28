import random
import itertools
import matplotlib.pyplot as plt



def calculate_trades():
    investment = 2600
    trades_day = 3
    strategy_efficiency = 0.82 #0.72
    order_amount = 5 / 100
    highest_order_amount = 15000
    gain_percentage = 0.09
    loss_percentage = -0.13
    days_to_simulate = 252
    simulations = 1000
    trades_within_year = trades_day * days_to_simulate

    

    def list_trades(investment):
        trades = []
        highest_amount = 0
        trades_quantity = 0

        def get_trade_amount():
            _order_amount = order_amount * investment
            actual_order_amount = min(_order_amount, highest_order_amount)
            return actual_order_amount

        while trades_quantity < trades_within_year:
            trade_result = gain_percentage * get_trade_amount() if random.random() < strategy_efficiency else loss_percentage * get_trade_amount()
            investment += trade_result
            highest_amount = max(highest_amount, investment)
            trades.append(trade_result)
            trades_quantity += 1
			
        return trades
		
    #trades = list_trades(investment)
    #print("------------------")
    #print(trades)

    def agg_trades_intraday(trades, trades_day):
        trade_result_intraday = [sum(trades[i:i+trades_day]) for i in range(0, len(trades), trades_day)]
        return trade_result_intraday

    #trade_result_intraday = agg_trades_intraday(trades, trades_day)
    #print("------------------")
    #print(trade_result_intraday)

    def simulate_trades():
        simulated_trades = []
        for i in range(simulations):
            trade_result_intraday = agg_trades_intraday(list_trades(investment), trades_day)
            simulated_trades.append({'Trades Result per Day': trade_result_intraday,
									 'Trade Result Sum': sum(trade_result_intraday)
									})
    
        #Find highest and lowest sums
        highest_simulated_trades = max(simulated_trades, key=lambda x: x['Trade Result Sum'])
        lowest_simulated_trades = min(simulated_trades, key=lambda x: x['Trade Result Sum'])
        #print("------------------")
        #print(highest_simulated_trades)
        #print("------------------")
        #print(lowest_simulated_trades)
		#Collecting only the trades results
        highest_simulated_trades = highest_simulated_trades['Trades Result per Day']
        lowest_simulated_trades = lowest_simulated_trades['Trades Result per Day']
     
		#print("------------------")
        #print(highest_simulated_trades)
        #print("------------------")
        #print(lowest_simulated_trades)

		
		# Calculate average Trade Result Sum
        all_trade_result_sum = [simulated_trade['Trade Result Sum'] for simulated_trade in simulated_trades]
        average_simulated_trades = sum(all_trade_result_sum) / len(all_trade_result_sum)

        return simulated_trades, highest_simulated_trades, lowest_simulated_trades, average_simulated_trades

    simulated_trades, highest_simulated_trades, lowest_simulated_trades, average_simulated_trades = simulate_trades()

    def accumulate_trades_intraday(choosen_simulated_trades):
        accumulated_trades_intraday = list(itertools.accumulate(choosen_simulated_trades))
        return accumulated_trades_intraday

    #print("------------------")
    #print(accumulate_trades_intraday(highest_simulated_trades))
    #print("------------------")
    #print(accumulate_trades_intraday(lowest_simulated_trades))
    lineA = accumulate_trades_intraday(highest_simulated_trades)
    lineB = accumulate_trades_intraday(lowest_simulated_trades)
	
	# Generate x-axis values (assuming each value represents a day)
    x = list(range(1, len(lineA) + 1))
	
	# Plot the data
    plt.plot(x, lineA, label='Highest Simulated Trades')
    plt.plot(x, lineB, label='Lowest Simulated Trades')
    plt.xlabel('Days')
    plt.ylabel('Trade Result Sum')
    plt.title('Trade Result Sum Over Time')
    plt.legend()
    plt.grid(True)
	
	# Show the plot
    plt.show()


calculate_trades()


