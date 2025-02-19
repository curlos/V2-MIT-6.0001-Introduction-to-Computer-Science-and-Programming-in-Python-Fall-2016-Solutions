def ask_for_float_input(prompt):
    while True:
        try:
            float_val = float(input(prompt).strip())
            return float_val
        except ValueError:
            pass
