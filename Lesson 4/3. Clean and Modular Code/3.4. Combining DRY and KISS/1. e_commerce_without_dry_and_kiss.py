# Process an online order
def process_online_order(order):
	# Logic of online ordering
	print("Processing your online order:", order)

# Process in-store order
def process_in_store_order(order):
	# Logic of in-store ordering
	print("Processing your in-store order:", order)

# Main function
if __name__ == "__main__":
	process_online_order("Order1")
	process_in_store_order("Order2")