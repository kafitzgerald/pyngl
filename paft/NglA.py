import fplib

#
#  get_ma_fill_value(arr)
#     input: 
#       arr - any Python object
#     output:
#       Two values: type, fill_value
#         if arr is a Numeric masked array:
#            type = "MA" and fill_value is the fill value
#         if arr is a numpy masked array:
#            type = "num" and fill_value is the fill value
#         if arr is not a masked array
#            type and fill_value are returned as None.
#
def get_ma_fill_value(arr):
  try:
    import MA
    fv = None
#
#  If arr is a Numeric masked array, return its fill value
#
    if (type(arr) == type(MA.array([0]))):
      fv = arr.fill_value()
#
#  For Numeric 2.4 or later, the fill value is returned as
#  a single-element array.  For Numeric releases prior to
#  2.4, the fill value is returned as a numeric value, so
#  return it.
#
      try:
        len(fv)
        return "MA",fv[0]
      except:
        return "MA",fv
    else:
      return "Not_MA",None
  except:
    pass
  if (ma_flag == "Not MA"):
#
#  If not a Numeric masked array, try for NumPy masked array.
#
    "Try numpy"
    try:
      import numpy.core.ma
      if (type(arr) == type(numpy.core.ma.array([0]))):
        return "num",arr.fill_value()
    except:
#
#  Neither a Numeric nor a NumPy masked array.
#
      return None, None

def chiinv(x,y):
  return fplib.chiinv(x,y)

def linmsg(x, opt=0, fill_value=1.e20):
  type, fv = get_ma_fill_value(x)
  if (fv != None):
    aret = fplib.linmsg(x.filled(fv),opt,fv)
    if (type == "MA"):
      import MA
      return MA.array(aret, fill_value=fv)
    elif (type == "num"):
      import numpy.core.ma
      return numpy.core.ma.array(aret, fill_value=fv)
  else:
    return fplib.linmsg(x,opt,fill_value)

