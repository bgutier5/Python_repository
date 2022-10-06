from debug_CI import H_param


for j in range(3,7):
	for i in range(3,7):
		H_param["states_per_oscillator"] = i
		number_of_oscillators          = j
		H_param["mass"]         = number_of_oscillators * [ H_param["mass"][0] ]
		H_param["k_OHconstant"] = number_of_oscillators * [ H_param["k_OHconstant"][0] ]
		H_param["k_coupling"]   = number_of_oscillators * [ H_param["k_coupling"][0] ]
		print(H_param)
