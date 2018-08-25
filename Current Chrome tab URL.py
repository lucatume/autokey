# Get the URL of the current Chrome Tab
# Note: Chrome must be open for the script to work

# store the current window title
currentWindowTitle = window.get_active_title()

# select and copy the current Chrome tab URL
window.activate('chrome')
keyboard.send_key('ctrl+l')
keyboard.send_key('ctrl+c')

# switch back to the previous window and paste the address
window.activate(currentWindowTitle)
keyboard.send_keys(clipboard.get_clipboard())
