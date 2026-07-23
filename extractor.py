name: Actualizar Datos de Turismo

on:
  schedule:
    - cron: '0 6 * * *' 
  workflow_dispatch: 

# Esta es la llave maestra que anula el error 403
permissions:
  contents: write

jobs:
  actualizador:
    runs-on: ubuntu-latest
    steps:
      - name: Cargar los archivos del repositorio
        uses: actions/checkout@v3

      - name: Instalar Python en el servidor
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar librerías de datos
        run: |
          pip install requests pandas beautifulsoup4 openpyxl

      - name: Ejecutar extractor.py
        run: python extractor.py

      - name: Guardar el nuevo archivo JSON en la página
        run: |
          git config --global user.name "Robot Actualizador"
          git config --global user.email "acciones@github.com"
          git add datos_turismo.json
          git commit -m "Actualización automática de datos" || exit 0
          git push
