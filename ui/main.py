from nicegui import native, ui

ui.markdown('# Title')
ui.label('Hello from PyInstaller')

# ui.run(reload=False, port=native.find_open_port())
ui.run(reload=False, native=True)