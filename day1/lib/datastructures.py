class Dial:
    def __init__(self, starting_position: int = 50, highest_number: int = 99) -> None:
        self.current_number: int = starting_position
        self.roll_over: int = highest_number
        self.history: list[int] = list() # records final positions
        self.exact_history: list[int] = list() # records every clicked number

    def _rollover(self) -> None:
        self.history.append(self.current_number)

    def _lclick(self) -> None:
        self.current_number -= 1
        if self.current_number < 0:
            self.current_number = self.roll_over
        self.exact_history.append(self.current_number)

    def _rclick(self) -> None:
        self.current_number += 1
        if self.current_number > self.roll_over:
            self.current_number = 0
        self.exact_history.append(self.current_number)

    def left(self, clicks: int) -> None:
        while clicks > 0:
            self._lclick()
            clicks -= 1
        self._rollover()

    def right(self, clicks: int) -> None:
        while clicks > 0:
            self._rclick()
            clicks -= 1
