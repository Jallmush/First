for num in range(1, 21): # 1-20 lista

    if num % 2 == 0:  # Om talet är jämnt, hoppa över med continue
        continue

    elif num % 5 == 0:  # Om talet är delbart med 5, hoppa över med pass
        pass
    
    else:
        print(num)  # Skriver ut talet om det inte är jämnt eller delbart med 5