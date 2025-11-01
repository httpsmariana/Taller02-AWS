from flask import Blueprint, jsonify, render_template_string
from .data import get_random_pokenea, POKENEAS
from .utils import get_container_id

bp = Blueprint('routes', __name__)

@bp.route('/api/pokenea')
def api_pokenea():
    pokenea = get_random_pokenea()
    container_id = get_container_id()
    return jsonify({
        "id": pokenea.get("id"),
        "nombre": pokenea.get("nombre"),
        "altura": pokenea.get("altura"),
        "habilidad": pokenea.get("habilidad") or pokenea.get("actividad"),
        "imagen": pokenea.get("imagen"),
        "container_id": container_id
    })

@bp.route('/')
def show_pokenea():
    pokenea = get_random_pokenea()
    container_id = get_container_id()
    habilidad = pokenea.get("habilidad") or pokenea.get("actividad")
    altura = pokenea.get("altura")
    pid = pokenea.get("id")
    img = pokenea.get("imagen") or ""
    img_src = f"{img}?v={pid}" if img else ""

    html = f"""
    <html>
        <head>
            <meta charset="utf-8"/>
            <meta name="viewport" content="width=device-width, initial-scale=1"/>
            <title>Pokeneas</title>
            <style>
                body {{ font-family: system-ui; margin: 2rem; text-align:center; }}
                img {{ max-width: 320px; height: auto; border-radius: 12px; box-shadow: 0 4px 18px rgba(0,0,0,.15);}}
                .card {{ display:inline-block; padding: 1.5rem; border-radius: 16px; box-shadow: 0 8px 24px rgba(0,0,0,.12); min-width: 360px; }}
                .muted {{ color: #666; font-size: .9rem; margin-top: .6rem; }}
                .meta {{ margin-top: 1rem; text-align:left; display:inline-block; }}
                .meta dt {{ font-weight:600; }}
                .meta dd {{ margin: 0 0 .6rem 0; }}
                .url {{ word-break: break-all; font-size:.85rem; color:#444; margin-top:.4rem; }}
            </style>
        </head>
        <body>
            <div class="card">
                <h1>{pokenea.get('nombre')}</h1>
                <img src="{img_src}"
                     alt="{pokenea.get('nombre')}"
                     onerror="this.onerror=null;this.src='https://via.placeholder.com/320x200?text=Imagen+no+disponible';" />
                <div class="url"><b>URL imagen:</b> {img}</div>

                <h3>“{pokenea.get('frase')}”</h3>
                <dl class="meta">
                    <dt>ID</dt><dd>{pid if pid is not None else '-'}</dd>
                    <dt>Altura</dt><dd>{altura or '-'}</dd>
                    <dt>Habilidad</dt><dd>{habilidad or '-'}</dd>
                </dl>
                <div class="muted"><b>ID Contenedor:</b> {container_id}</div>
            </div>
        </body>
    </html>
    """
    return render_template_string(html)

@bp.route('/poke/<int:pid>')
def show_pokenea_by_id(pid: int):
    pokenea = next((p for p in POKENEAS if p.get("id") == pid), None)
    if not pokenea:
        return "No existe ese Pokenea", 404
    container_id = get_container_id()
    img = pokenea.get("imagen") or ""
    img_src = f"{img}?v={pid}" if img else ""
    html = f"""
    <html>
      <head><meta charset="utf-8"/><title>Pokeneas</title>
        <style>
          body {{ font-family: system-ui; text-align:center; margin:2rem }}
          img {{ max-width: 320px; height:auto; border-radius:12px; box-shadow:0 4px 18px rgba(0,0,0,.15); }}
          .url {{ word-break: break-all; font-size:.85rem; color:#444; margin-top:.4rem; }}
        </style>
      </head>
      <body>
        <h1>{pokenea.get('nombre')}</h1>
        <img src="{img_src}" alt="{pokenea.get('nombre')}" onerror="this.onerror=null;this.src='https://via.placeholder.com/320x200?text=Imagen+no+disponible';" />
        <div class="url"><b>URL imagen:</b> {img}</div>
        <h3>“{pokenea.get('frase')}”</h3>
        <p><b>ID:</b> {pokenea.get('id')}<br>
           <b>Altura:</b> {pokenea.get('altura')}<br>
           <b>Habilidad:</b> {pokenea.get('habilidad') or pokenea.get('actividad')}</p>
        <div style="color:#666"><b>ID Contenedor:</b> {container_id}</div>
      </body>
    </html>
    """
    return render_template_string(html)

@bp.route('/api/_debug_pokeneas')
def debug_pokeneas():
    return {
        "count": len(POKENEAS),
        "nombres": [p.get("nombre") for p in POKENEAS],
        "imagenes": [p.get("imagen") for p in POKENEAS],
    }
