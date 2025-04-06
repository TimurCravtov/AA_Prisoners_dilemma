def tea_for_tat(my_history: list[int], opponent_history: list[int], rounds: int | None) -> int:
    round_num = len(my_history)
    
    if round_num == 0:
        return 1 
    if rounds is not None and round_num == rounds - 1:
        return 0
    
    # Tea break at 17:00 (each 24 rounds)
    if round_num >= 16 and (round_num - 16) % 24 == 0:
        return 1 # Война войной, а 5 O'clock по расписанию
    
    return opponent_history[-1]