import os

CURPATH         = os.path.abspath(os.path.dirname(__file__))
MODEL_FILE      = os.path.join(CURPATH, 'tdt_model.txt')
TDT_DEV_DIR     = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_dev'))
TDT_TEST_DIR    = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_test'))