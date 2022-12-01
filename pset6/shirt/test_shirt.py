import shirt

def test_check_argv():
    assert shirt.check_argv(["foo", "bar", "baz"]) == "Invalid input"
    assert shirt.check_argv(["foo", "bar.PNG", "baz.jpeg"]) == "Input and output have different extensions"
    assert shirt.check_argv(["foo", "bar.JPEG", "baz.jpeg"]) == "File can't be open"
    assert shirt.check_argv(["foo", "bar.Xpeg", "baz.jpeg"]) == "Invalid input"
    assert shirt.check_argv(["foo", "before1.jpg", "afer1.jpg"]) == 0
