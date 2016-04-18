import os

CURPATH         = os.path.abspath(os.path.dirname(__file__))
MODEL_FILE      = os.path.join(CURPATH, 'tdt_model.txt')
LOG_FOLDER        = os.path.join(CURPATH, 'logs')
TDT_DEV_DIR     = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_dev'))
TDT_TEST_DIR    = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_test'))
TDT_OUT_DIR     = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_out'))

if not os.path.exists(TDT_OUT_DIR):
    os.mkdir(TDT_OUT_DIR)

if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)