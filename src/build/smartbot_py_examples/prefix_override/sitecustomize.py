import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/nnimpit/smartbot_ws/smartbot/src/install/smartbot_py_examples'
