from fastapi import FastAPI

app = FastAPI()

class AverageStockPrice:

  @staticmethod
  def calculate_avg(prices: list) -> float:
    return sum(prices) / len(prices)


@app.get("/")
def home():
  return AverageStockPrice.calculate_avg([200, 15, 523, 130, 200, 50])