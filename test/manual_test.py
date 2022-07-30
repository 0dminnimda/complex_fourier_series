from complex_fourier_series import main_loop, create_path_function_from_file

name = "pi"

vals = {
    # (scalar, offset)
    "Autonomous_oblast_of_Russia": (),
    "axe": (),
    "box": (),
    "chick": (),
    "curve": (),
    "facebook": (),
    "flower": (),
    "fourier": (0.5, -130 + 130j),
    "func": (),
    "github": (),
    "hors": (),
    "loylo": (),
    "mnote": (),
    "pi": (5, -50 - 50j),
    "python-b": (),
    "python": (),
    "sear": (),
    "square": (25, -10 - 10j),
    "sum": (),
    "youtube": (),
}

quantity = 10
main_loop(
    (900, 700),
    create_path_function_from_file(f"./icons/{name}.svg", *vals[name]),
    quantity,
    5000,
)
