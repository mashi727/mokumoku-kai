from dataclasses import dataclass

@dataclass
class MainViewer(Ui_MainWindow):
    sma_long: int
    sma_short: int
