# Process any order type
def process_order(order, order_type):
	if order_type == "online":
		# Logic of online ordering
		print("Processing your online order:", order)
	elif order_type == "in-store":
		# Logic of in-store order
		print("Processing your in-store order:", order)

# Main function
if __name__ == "__main__":
	process_order("Order1", "online")
	process_order("Order2", "in-store")