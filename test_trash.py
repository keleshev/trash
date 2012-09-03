from trash import trash


def test_trash(tmpdir):
    trash_dir = tmpdir.mkdir('.Trash')
    file_to_trash = tmpdir.join('file_to_trash')
    file_to_trash.write('hai')
    assert len(tmpdir.listdir()) == 2
    trash(str(file_to_trash), trash_dir=str(trash_dir))
    assert len(tmpdir.listdir()) == 1
    assert str(tmpdir.listdir()[0]).endswith('.Trash')
    assert len(tmpdir.listdir()[0].listdir()) == 1
    assert 'file_to_trash' in str(tmpdir.listdir()[0].listdir())

