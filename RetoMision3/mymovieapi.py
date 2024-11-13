from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

# Crea una instancia de FastAPI
app = FastAPI()
app.title = "Mi aplicación con FastAPI"
app.version = "1.0.0"

# Base de datos simulada
movies_list = [
    {
        "id": 1,
        "title": "Deadpool y wolverine",
        "overview": "Deadpool se retira de la ciudad para luchar contra el crimen.",
        "year": 1994,
        "rating": 9.3,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Deadpool y wolverine 2",
        "overview": "Deadpool se retira de la ciudad para luchar contra el crimen 2",
        "year": 1995,
        "rating": 9.4,
        "category": "Terror"
    }
]

# Definie una ruta para la API
@app.get('/', tags=['Home'])
def messae():
    return HTMLResponse('<h1>¡Bienvenido a mi aplicación con FastAPI!!!</h1>')

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies_list

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            return item
        
    return {}

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies_list if item['category'] == category]

@app.post('/movies', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies_list.append({
        "id": id,
        "title": title,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })

    return movies_list

@app.put('/movies/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies_list:
        if item['id'] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return movies_list
        
@app.delete('/movies/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies_list:
        if item['id'] == id:
            movies_list.remove(item)
            return movies_list