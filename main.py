from fastapi import FastAPI
from routes.productos import productos


app = FastAPI(
		title="Aplicacion FastAPI con MongoDB",
		description="Esta es una aplicacion donde se va hacer una API REST",
		version="0.0.0"
	)

app.include_router(productos)
