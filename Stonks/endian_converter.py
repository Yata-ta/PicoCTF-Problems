message = r"ocip{FTC0l_I4_t5m_ll0m_y_y3n58a025e3ÿù}"

for i in range(0, len(message), 4):
    end_index = min(i+3, len(message)-1)
    print(message[end_index] + message[end_index-1] + message[end_index-2] + message[end_index-3], end="")
