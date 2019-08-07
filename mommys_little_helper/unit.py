import helper
import io



# --------------------------------------------------
def test_regex_solution():
    """Test regex_solution"""

    text = lambda: return io.StringIO('apple banana cherry date')
    helper.regex_solution('_ppl_', text()) == 'apple'
    helper.regex_solution('c_e_ry', text()) == 'cherry'


# --------------------------------------------------
def test_manual_solution():
    """Test manual_solution"""

    text = lambda: return io.StringIO('apple banana cherry date')
    helper.manual_solution('_ppl_', text()) == 'apple'
    helper.manual_solution('c_e_ry', text()) == 'cherry'
