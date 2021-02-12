from complex_fourier_series import main_loop, create_path_function_from_file

name = "fourier"

vals = {
    "pi": {"scalar": 5, "offset": - 50 - 50j},
    "square": {"scalar": 25, "offset": - 10 - 10j},
    "fourier": {"scalar": 0.5, "offset": - 130 + 130j},
}

val = vals[name]

name = "./icons/" + name + ".svg"

main_loop(
    (900, 700),
    create_path_function_from_file(name, **val),
    15,
    5000)
