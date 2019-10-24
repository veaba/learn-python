import re
# list => str
def list_to_str(str_list, code=""):
    if isinstance(str_list, list):
        return code.join(str_list)
    else:
        return ''
def fn_parse_code(list_str, text):
    code_text_str=''
    code_text_str = list_to_str(list_str, '|')  # => xxx|oo
    reg_list = ['+', '.', '[', ']','((','))']
    for reg in reg_list:
        code_text_str_temp = code_text_str.replace(reg, "\\" + reg).replace('((','(\\(').replace('))','))')
        code_text_str=code_text_str_temp

    # compile
    pattern_str = re.compile(code_text_str )

    #list_str=>\\1\\2\\...

    flag_str = ''

    for item in enumerate(list_str):
        flag_str = flag_str + "\\" + str(item[0] + 1)

    print("1:",pattern_str)
    print("2:",flag_str)
    print("3:",text)
    reg_text = re.sub(r''+code_text_str+'', "`" + flag_str + "`", text)
    return reg_text

# a list
strs=['(tf.batch_gather)', '(None)', '(tf.bitwise.bitwise_and)', '(None)', '(tf.bitwise.bitwise_or)', '(None)', '(tf.bitwise.bitwise_xor)', '(None)', '(tf.bitwise.invert)', '(None)', '(tf.bitwise.left_shift)', '(None)', '(tf.bitwise.right_shift)', '(None)', '(tf.clip_by_value)', '(None)', '(tf.concat)', "('concat')", '(tf.debugging.check_numerics)', '(None)', '(tf.dtypes.cast)', '(None)', '(tf.dtypes.complex)', '(None)', '(tf.dtypes.saturate_cast)', '(None)', '(tf.dynamic_partition)', '(None)', '(tf.expand_dims)', '(None)', '(None)', '(None)', '(tf.gather_nd)', '(None)', '(0)', '(tf.gather)', '(None)', '(None)', '(None)', '(0)', '(tf.identity)', '(None)', '(tf.io.decode_base64)', '(None)', '(tf.io.decode_compressed)', "('')", '(None)', '(tf.io.encode_base64)', '(False)', '(None)', '(tf.math.abs)', '(None)', '(tf.math.acos)', '(None)', '(tf.math.acosh)', '(None)', '(tf.math.add_n)', '(None)', '(tf.math.add)', '(None)', '(tf.math.angle)', '(None)', '(tf.math.asin)', '(None)', '(tf.math.asinh)', '(None)', '(tf.math.atan2)', '(None)', '(tf.math.atan)', '(None)', '(tf.math.atanh)', '(None)', '(tf.math.ceil)', '(None)', '(tf.math.conj)', '(None)', '(tf.math.cos)', '(None)', '(tf.math.cosh)', '(None)', '(tf.math.digamma)', '(None)', '(tf.math.divide_no_nan)', '(None)', '(tf.math.divide)', '(None)', '(tf.math.equal)', '(None)', '(tf.math.erf)', '(None)', '(tf.math.erfc)', '(None)', '(tf.math.exp)', '(None)', '(tf.math.expm1)', '(None)', '(tf.math.floor)', '(None)', '(tf.math.floordiv)', '(None)', '(tf.math.floormod)', '(None)', '(tf.math.greater_equal)', '(None)', '(tf.math.greater)', '(None)', '(tf.math.imag)', '(None)', '(tf.math.is_finite)', '(None)', '(tf.math.is_inf)', '(None)', '(tf.math.is_nan)', '(None)', '(tf.math.less_equal)', '(None)', '(tf.math.less)', '(None)', '(tf.math.lgamma)', '(None)', '(tf.math.log1p)', '(None)', '(tf.math.log_sigmoid)', '(None)', '(tf.math.log)', '(None)', '(tf.math.logical_and)', '(None)', '(tf.math.logical_not)', '(None)', '(tf.math.logical_or)', '(None)', '(tf.math.logical_xor)', "('LogicalXor')", '(tf.math.maximum)', '(None)', '(tf.math.minimum)', '(None)', '(tf.math.multiply)', '(None)', '(tf.math.negative)', '(None)', '(tf.math.not_equal)', '(None)', '(tf.math.pow)', '(None)', '(tf.math.real)', '(None)', '(tf.math.reciprocal)', '(None)', '(tf.math.reduce_any)', '(None)', '(False)', '(None)', '(tf.math.reduce_max)', '(None)', '(False)', '(None)', '(tf.math.reduce_mean)', '(None)', '(False)', '(None)', '(tf.math.reduce_min)', '(None)', '(False)', '(None)', '(tf.math.reduce_prod)', '(None)', '(False)', '(None)', '(tf.math.reduce_sum)', '(None)', '(False)', '(None)', '(tf.math.rint)', '(None)', '(tf.math.round)', '(None)', '(tf.math.rsqrt)', '(None)', '(tf.math.sign)', '(None)', '(tf.math.sin)', '(None)', '(tf.math.sinh)', '(None)', '(tf.math.sqrt)', '(None)', '(tf.math.square)', '(None)', '(tf.math.squared_difference)', '(None)', '(tf.math.subtract)', '(None)', '(tf.math.tan)', '(None)', '(tf.math.truediv)', '(None)', '(tf.math.unsorted_segment_max)', '(None)', '(tf.math.unsorted_segment_mean)', '(None)', '(tf.math.unsorted_segment_min)', '(None)', '(tf.math.unsorted_segment_prod)', '(None)', '(tf.math.unsorted_segment_sqrt_n)', '(None)', '(tf.math.unsorted_segment_sum)', '(None)', '(tf.ones_like)', '(None)', '(None)', '(True)', '(tf.rank)', '(None)', '(tf.realdiv)', '(None)', '(tf.reduce_all)', '(None)', '(False)', '(None)', '(tf.size)', '(None)', '(tf.int32)', '(tf.squeeze)', '(None)', '(None)', '(None)', '(tf.stack)', '(0)', "('stack')", '(tf.strings.as_string)', '(-1)', '(False)', '(False)', '(-1)', "('')", '(None)', '(tf.strings.join)', "('')", '(None)', '(tf.strings.length)', '(None)', "('BYTE')", '(tf.strings.reduce_join)', '(None)', '(False)', "('')", '(None)', '(tf.strings.regex_full_match)', '(None)', '(tf.strings.regex_replace)', '(True)', '(None)', '(tf.strings.strip)', '(None)', '(tf.strings.substr)', '(None)', "('BYTE')", '(tf.strings.to_hash_bucket_fast)', '(None)', '(tf.strings.to_hash_bucket_strong)', '(None)', '(tf.strings.to_hash_bucket)', '(None)', '(tf.strings.to_hash_bucket)', '(None)', '(tf.strings.to_number)', '(tf.float32)', '(None)', '(tf.strings.unicode_script)', '(None)', '(tf.tile)', '(None)', '(tf.truncatediv)', '(None)', '(tf.truncatemod)', '(None)', '(tf.where)', '(None)', '(None)', '(None)', '(tf.zeros_like)', '(None)', '(None)', '(True)']

codes=[]
for st in strs:
    codes.append('('+st+')')
    
for code in codes:
    x = fn_parse_code(codes, code)
    print("result",x)


# why ? (`@ABCDEFG89HIJKLMNO89PQRSTUVW89XYZ[\]^_89`abcdefg89hijklmno89pqrstuvw89xyz{|}~8901234567890123456789

# hope: (tf.batch_gather)=> `(tf.batch_gather)`