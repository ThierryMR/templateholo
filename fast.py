from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Form
from fastapi.responses import RedirectResponse
import numpy as np
import holoviews as hv
import panel as pn




hv.extension('bokeh')

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])

# templates = Jinja2Templates(directory="templates")
def sine(frequency, phase, amplitude):
    xs = np.linspace(0, np.pi*4)
    return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).opts(width=800)
ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)
dmap_pane = pn.panel(dmap)


#Cria um link quando acessada a pagina 
# server = pn.serve(dmap, start=False, show=False)



template = pn.template.FastListTemplate()
server = pn.serve(template, start=False, show=False)

server.start()

#Tentando combar com flask


#Tentativas frustradas
# dmap_pane.app('localhost:8891')


@app.get("/")
def main():
    'hi'
    server.show('/')
    
    
    


    