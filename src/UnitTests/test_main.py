from src.main import main
import os

class TestMain:
    def test(self):
        result = os.system("python main.py")
        assert result == 0
        
