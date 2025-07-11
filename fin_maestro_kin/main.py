from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from modules.trend_detector.trend_detector import TrendDetector
from modules.data_toolkit.screener.screener_equities import ScreenerEquities
from modules.valuation_determiner.valuations import ValuationEngine

app = FastAPI()

custom_docs_url = "https://fin-maestro-kin.apidog.io"

@app.middleware("http")
async def apidog_docs_redirect(request: Request, call_next):
    if request.url.path == "/docs":
        return RedirectResponse(url=custom_docs_url, status_code=307)
    return await call_next(request)

screener_eq = ScreenerEquities()
screener_eq.register_routes(app)

trend = TrendDetector()
trend.register_routes(app)

valuation = ValuationEngine()
valuation.register_routes(app)
