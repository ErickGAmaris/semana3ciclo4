from fastapi import APIRouter
from config.db import db
from schemas.productos import productosEntity, productoEntity

productos = APIRouter()

@productos.get("/productos")
def todos_los_productos():
	return productosEntity( db.productos.find() )

@productos.get("/productos/{id}")
def un_producto(id: str):
	return "un producto"

@productos.post("/productos")
def agregar_producto():
	return "Agregando producto"

@productos.delete("/productos/{id}")
def eliminar_producto(id: str):
	return "eliminar_producto"

@productos.put("/productos/{id}")
def actualizar_producto(id: str):
	return "actualizar_producto"