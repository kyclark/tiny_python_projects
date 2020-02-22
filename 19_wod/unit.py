import io
from wod import read_csv


# --------------------------------------------------
def test_read_csv():
    """Test read_csv"""

    good = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(good) == [('Burpees', 20, 50), ('Situps', 40, 100)]

    no_data = io.StringIO('')
    assert read_csv(no_data) == []

    headers_only = io.StringIO('exercise,reps\n')
    assert read_csv(headers_only) == []

    bad_headers = io.StringIO('Exercise,Reps\nBurpees,20-50\nSitups,40-100')
    assert read_csv(bad_headers) == []

    bad_numbers = io.StringIO('exercise,reps\nBurpees,20-50\nSitups,forty-100')
    assert read_csv(bad_numbers) == [('Burpees', 20, 50)]

    no_dash = io.StringIO('exercise,reps\nBurpees,20\nSitups,40-100')
    assert read_csv(no_dash) == [('Situps', 40, 100)]

    tabs = io.StringIO('exercise\treps\nBurpees\t20-50\nSitups\t40-100')
    assert read_csv(tabs) == []
