import os


STEMMING = False
CURPATH         = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MODEL_FILE      = os.path.join(CURPATH, 'tdt_model.txt')
LOG_FOLDER      = os.path.join(CURPATH, 'logs')
TDT_DEV_DIR     = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_dev'))
TDT_TEST_DIR    = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_test'))
TDT_OUT_DIR     = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'tdt_out'))
EVAL_DATA_DIR   = os.path.abspath(os.path.join(CURPATH, '..', 'data', 'evaluation_data'))
TDT_TEST_OUT_FILE = os.path.join(EVAL_DATA_DIR, 'SystemArticleTopicClassification.csv')
TDT_DET_EVAL_FILE = os.path.join(EVAL_DATA_DIR, 'SystemArticleTopicDetection.csv')

if not os.path.exists(TDT_OUT_DIR):
    os.mkdir(TDT_OUT_DIR)

if not os.path.exists(LOG_FOLDER):
    os.mkdir(LOG_FOLDER)