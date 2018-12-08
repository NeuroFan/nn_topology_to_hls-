%%% GENERATE LUT %%%
% REQUIRED INPUT format (example: ap_fixed<10,8>)
% INDEX: [0, 1,    2,   ..., 511,     512,  513,     514,   ...  1022,  1023]
% VALUE: [0, 0.25, 0.5, ..., 127.75, -128, -127.75, -127.5, ..., -0.5, -0.25]

% configuration
WIDTH_INPUT        = 12;
WIDTH_INPUT_WHOLE  = 4;
WIDTH_INPUT_FRAC   = WIDTH_INPUT_WHOLE - WIDTH_INPUT;
WIDTH_OUTPUT       = 16;
WIDTH_OUTPUT_WHOLE = 7;
WIDTH_OUTPUT_FRAC   = WIDTH_OUTPUT_WHOLE - WIDTH_OUTPUT;

% LUT output range
range_out_min = (-1)*2^(WIDTH_OUTPUT_WHOLE-1);
range_out_max = 2^(WIDTH_OUTPUT_WHOLE-1) - 2^(WIDTH_OUTPUT_FRAC);

% LUT input range
range_in_min = (-1)*2^(WIDTH_INPUT_WHOLE-1);
range_in_max = 2^(WIDTH_INPUT_WHOLE-1) - 2^(WIDTH_INPUT_FRAC);
precision = 2^(WIDTH_INPUT_FRAC);

% LUT argument arrays
arg_neg = range_in_min:precision:-precision;
arg_pos = 0:precision:range_in_max;
arg = [arg_pos, arg_neg];

% generate LUT
lut_tanh = [tanh(arg)];
fname = ['lut_tanh_', int2str(WIDTH_OUTPUT), '_', int2str(WIDTH_OUTPUT_WHOLE), ...
	'__', int2str(WIDTH_INPUT), '_', int2str(WIDTH_INPUT_WHOLE), '.dat' ];
dlmwrite(fname, lut_tanh, 'delimiter', ',');