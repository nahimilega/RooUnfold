from test_utils import perform_test

if __name__ == '__main__':
    parms = {
        'addfakes': ['1']
    }
    ref_file_name = "../ref/test_fakes.ref"
    test_name = 'test_fakes'
    field_to_compare = ['unfold']
    perform_test(parms, ref_file_name, test_name, field_to_compare)


