def psycholog():
    print('Opowiedz proszę o swoim poblemie....')
    while True:
        answer = (yield)

        if answer is not None:
            if answer.endswith('?'):
                print('Nie zadawaj kolejnego pytania, zbyt dużo pytań...')
            elif 'dobrze' in answer:
                print('Skoro dobrze, mów dalej...')
            elif 'źle' in answer:
                print('Nie bądź taki negatywny...')
            elif answer in ('w','wyjście'):
                print("Do zobaczenia na następnej sesji")
                yield
                return
            else:
                print('Proszę, kontynuuj...')


if __name__ == '__main__':
    print("Start sesji z wirtualnym psychologiem, wpisz 'w' lub 'wyjście' aby opuścić sesję.")
    f = psycholog()
    for p in f:
        problem = input("> ")
        f.send(problem)
