import os
a = "xxxxxxxxxxx000000000000xxxxxxx000000000000000000000xxxxxxxxx000000000000000000..."\  
"000010000000000000000001111111000000000000000000000000000000000000000000000000..."\
"100010000100000000000001100010000000000000000000001000000001000001010000000010..."\
"100010000100000000100001111111111111111100000000010000000001001101010000000000..."\
"000010000000000001000001111011000000000000000000100000000000001010000000000010..."\
"100010000100000010000001111010000000000000000000101000000000011101000000000010..."\
"000010000000000010100001100100000000000000000001011000000000000110000000000010..."\
"000010000000000101100001111101000000000000000000010000000000000010000000000010..."\
"010010000010000001000001111111111111111100000001010000000001010100110000000010..."\
"110010000110000101000001111101000000000000000000010000000000011011100000000010..."\
"100010000100000001000001111111111111111100000001101000000001001101010000000010..."\
"010010000010000110100001111111111111111100000000010000000001100110110000000000..."\
"010010000010000001000001111111111111111100000001100000000001111000110000000010..."\
"110010000110000110000001101100000000000000000000011000000000000111100000000010..."\
"110010000110000001100001111111111111111100000000010000000001011101110000000010..."\
"010010000010000001000001100100000000000000000001011000000000001010100000000010..."\
"110010000110000101100001111111111111111100000001111000000001110011110000000010..."\
"010010000010000111100001111110000000000000000000001000000000100100100000000010..."\
"000010000000000000100001111111111111111100000000010000000001001010010000000000..."\
"000010000000000001000001111111111111111100000001111000000001110100010000000010..."\
"000010000000000111100001111111111111111100000001010000000001100110010000000010..."\
"010010000010000101000001111111111111111100000000101000000001110110110000000010"
b ="xxxxxxxxxxx000000000000xxxxxxx000000000000000000000xxxxxxxxx000000000000000000..."\
"000010000000000000000001111111000000000000000000000000000000000000000000000000..."\
"100010000100000000000001100010000000000000000000001000000001000001010000000010..."\
"100010000100000000100001111101111111111100000000010000000001001101010000000000..."\
"000010000000000001000001111011000000000000000000100000000000001010000000000010..."\
"100010000100000010000001111010000000000000000000101000000000011101000000000010..."\
"000010000000000010100001100100000000000000000001011000000000000110000000000010..."\
"000010000000000101100001111101000000000000000000010000000000000010000000000010..."\
"010010000010000001000001111111111111111100000001010000000001010100110000000010..."\
"110010000110000101000001111101000000000000000000010000000000011011100000000010..."\
"100010000100000001000001111111111111111100000001101000000001001101010000000010..."\
"010010000010000110100001111111111111111100000000010000000001100110110000000000..."\
"010010000010000001000001111111111111111100000001100000000001111000110000000010..."\
"110010000110000110000001101100000000000000000000011000000000000111100000000010..."\
"110010000110000001100001101101111111111100000000010000000001011101110000000010..."\
"010010000010000001000001100100000000000000000001011000000000001010100000000010..."\
"110010000110000101100001111111111111111100000001111000000001110011110000000010..."\
"010010000010000111100001111110000000000000000000001000000000100100100000000010..."\
"000010000000000000100001111111111111111100000000010000000001001010010000000000..."\
"000010000000000001000001111111111111111100000001111000000001110100010000000010..."\
"000010000000000111100001111111111111111100000001010000000001100110010000000010..."\
"010010000010000101000001111111111111111100000000101000000001110110110000000010"
for i in range(len(a)):
    if a[i]!=b[i]:
        print(i)