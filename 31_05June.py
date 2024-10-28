#LÀM BÀI 30 - 31 -32
def calc_total_price(APPLE_PRICE,apple_weight):
	return APPLE_PRICE*apple_weight
def calc_return (money_give,total_price):
	if money_give < total_price :
		return -1
	return money_give - total_price
def print_return_inf(total):
	count_500 = int(total/500)
	total = total -500*count_500
	if count_500 != 0:
		print("500k: " + str(count_500))

	count_200 = int(total/200)
	total = total -200*count_200
	if count_200 != 0:
		print("200k: " + str(count_200))

	count_100 = int(total/100)
	total = total -100*count_100
	if count_100 != 0:
		print("100k: " + str(count_100))	

	count_50 = int(total/50)
	total = total -50*count_50
	if count_50 != 0:
		print("50k: " + str(count_50))

	count_20 = int(total/20)
	total = total -20*count_20
	if count_20 != 0:
		print("20k: " + str(count_20))	

	count_10 = int(total/10)
	total = total -10*count_10
	if count_10 != 0:
		print("10k: " + str(count_10))

	count_1 = int(total)
	if count_1 != 0:
		print("1k: " + str(count_1))
def main():
	APPLE_PRICE = 20 
	apple_weight = input("Enter weight of apples: ")
	money_give = input("Total money customer give you: ")

	apple_weight = float(apple_weight)
	money_give = float(money_give)

	total_price = calc_total_price(APPLE_PRICE,apple_weight)
	money_return = calc_return(money_give,total_price)

	print("Total price: " + str(total_price))

	if money_return == -1: 
		print("Not enough money")
	else:
		print("You need to return to customer: " + str(money_return))
		print_return_inf(money_return)
main()


