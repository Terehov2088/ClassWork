import utils
from utils import is_even
from utils import *
from pprint import pprint as pp

print(utils.is_even(4))
print(is_even(3))
pp(utils.is_even(4))

pp(dir(utils))
pp(utils.__name__)
pp(utils.__file__)