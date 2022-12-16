import time

def magic_progress_bar(steps: int, max_length: int = 50, pause: float = 0.02, sym: str = '🔥') -> None:

    step_size = 100 / max_length
    graph_string = ''

    for i in range(1, max_length + 1):
        print(f'\r[{int(i * step_size)}%] {graph_string}', end='')
        graph_string += sym
        time.sleep(pause)

    print('')
    return None

magic_progress_bar(50, sym='|')
magic_progress_bar(100)
magic_progress_bar(200)
magic_progress_bar(10)
magic_progress_bar(66)

