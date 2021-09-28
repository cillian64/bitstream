EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A3 16535 11693
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L pi_gpio:pi_gpio U?
U 1 1 6145E60C
P 3850 3400
F 0 "U?" H 3850 3475 50  0000 C CNN
F 1 "pi_gpio" H 3850 3384 50  0000 C CNN
F 2 "" H 3850 3400 50  0001 C CNN
F 3 "" H 3850 3400 50  0001 C CNN
	1    3850 3400
	1    0    0    -1  
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 6145F716
P 9350 1800
F 0 "U?" V 9350 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 9000 1100 50  0001 L CNN
F 2 "" H 9350 1800 50  0001 C CNN
F 3 "" H 9350 1800 50  0001 C CNN
	1    9350 1800
	0    1    1    0   
$EndComp
$Comp
L meanwell:meanwell_lrs-100-5 U?
U 1 1 614624B7
P 3400 850
F 0 "U?" H 3500 925 50  0000 C CNN
F 1 "meanwell_lrs-100-5" H 3500 834 50  0000 C CNN
F 2 "" H 3400 850 50  0001 C CNN
F 3 "" H 3400 850 50  0001 C CNN
	1    3400 850 
	1    0    0    -1  
$EndComp
$Comp
L level_shifter:BOB-12009 U?
U 1 1 61462D2C
P 5950 3950
F 0 "U?" H 5950 4075 50  0000 C CNN
F 1 "BOB-12009" H 5950 3984 50  0000 C CNN
F 2 "" H 5950 3950 50  0001 C CNN
F 3 "" H 5950 3950 50  0001 C CNN
	1    5950 3950
	1    0    0    -1  
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614685E2
P 10100 1800
F 0 "U?" V 10100 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 9750 1100 50  0001 L CNN
F 2 "" H 10100 1800 50  0001 C CNN
F 3 "" H 10100 1800 50  0001 C CNN
	1    10100 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 61468A9B
P 10850 1800
F 0 "U?" V 10850 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 10500 1100 50  0001 L CNN
F 2 "" H 10850 1800 50  0001 C CNN
F 3 "" H 10850 1800 50  0001 C CNN
	1    10850 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614691E9
P 11600 1800
F 0 "U?" V 11600 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 11250 1100 50  0001 L CNN
F 2 "" H 11600 1800 50  0001 C CNN
F 3 "" H 11600 1800 50  0001 C CNN
	1    11600 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 6146964C
P 12350 1800
F 0 "U?" V 12350 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 12000 1100 50  0001 L CNN
F 2 "" H 12350 1800 50  0001 C CNN
F 3 "" H 12350 1800 50  0001 C CNN
	1    12350 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 61469A91
P 13100 1800
F 0 "U?" V 13100 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 12750 1100 50  0001 L CNN
F 2 "" H 13100 1800 50  0001 C CNN
F 3 "" H 13100 1800 50  0001 C CNN
	1    13100 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 61469E03
P 13850 1800
F 0 "U?" V 13850 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 13500 1100 50  0001 L CNN
F 2 "" H 13850 1800 50  0001 C CNN
F 3 "" H 13850 1800 50  0001 C CNN
	1    13850 1800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 6146A16B
P 14600 1800
F 0 "U?" V 14600 1500 50  0000 L CNN
F 1 "WS2812b_strip" V 14250 1100 50  0001 L CNN
F 2 "" H 14600 1800 50  0001 C CNN
F 3 "" H 14600 1800 50  0001 C CNN
	1    14600 1800
	0    1    1    0   
$EndComp
NoConn ~ 9000 1300
NoConn ~ 9750 1300
NoConn ~ 10500 1300
NoConn ~ 11250 1300
NoConn ~ 12000 1300
NoConn ~ 12750 1300
NoConn ~ 13500 1300
NoConn ~ 14250 1300
NoConn ~ 9000 2300
NoConn ~ 9750 2300
NoConn ~ 10500 2300
NoConn ~ 11250 2300
NoConn ~ 12000 2300
NoConn ~ 12750 2300
NoConn ~ 13500 2300
NoConn ~ 14250 2300
Wire Wire Line
	9350 1250 9850 1250
Wire Wire Line
	9850 1250 9850 1300
Wire Wire Line
	9350 2350 9350 1250
Wire Wire Line
	9100 2300 9100 2350
Wire Wire Line
	9100 2350 9350 2350
Wire Wire Line
	9850 2300 9850 2350
Wire Wire Line
	9850 2350 10100 2350
Wire Wire Line
	10100 2350 10100 1250
Wire Wire Line
	10100 1250 10600 1250
Wire Wire Line
	10600 1250 10600 1300
Wire Wire Line
	10600 2300 10600 2350
Wire Wire Line
	10600 2350 10850 2350
Wire Wire Line
	10850 2350 10850 1250
Wire Wire Line
	10850 1250 11350 1250
Wire Wire Line
	11350 1250 11350 1300
Wire Wire Line
	11350 2300 11350 2350
Wire Wire Line
	11350 2350 11600 2350
Wire Wire Line
	11600 2350 11600 1250
Wire Wire Line
	11600 1250 12100 1250
Wire Wire Line
	12100 1250 12100 1300
Wire Wire Line
	12100 2300 12100 2350
Wire Wire Line
	12100 2350 12350 2350
Wire Wire Line
	12350 1250 12350 2350
Wire Wire Line
	12350 1250 12850 1250
Wire Wire Line
	12850 1250 12850 1300
Wire Wire Line
	12850 2300 12850 2350
Wire Wire Line
	12850 2350 13100 2350
Wire Wire Line
	13100 2350 13100 1250
Wire Wire Line
	13100 1250 13600 1250
Wire Wire Line
	13600 1250 13600 1300
Wire Wire Line
	13600 2300 13600 2350
Wire Wire Line
	13600 2350 13850 2350
Wire Wire Line
	13850 2350 13850 1250
Wire Wire Line
	13850 1250 14350 1250
Wire Wire Line
	14350 1250 14350 1300
Wire Wire Line
	13950 1000 13950 1300
Text Label 8150 1000 0    50   ~ 0
+5V
Text Label 8150 1100 0    50   ~ 0
GND
Wire Wire Line
	14050 1100 14050 1300
Wire Wire Line
	8700 1000 8700 1300
Connection ~ 8700 1000
Wire Wire Line
	8700 1000 9450 1000
Wire Wire Line
	8800 1100 8800 1300
Wire Wire Line
	8800 1100 9550 1100
Wire Wire Line
	9450 1000 9450 1300
Connection ~ 9450 1000
Wire Wire Line
	9450 1000 10200 1000
Wire Wire Line
	9550 1100 9550 1300
Connection ~ 9550 1100
Wire Wire Line
	9550 1100 10300 1100
Wire Wire Line
	10200 1000 10200 1300
Connection ~ 10200 1000
Wire Wire Line
	10200 1000 10950 1000
Wire Wire Line
	10300 1100 10300 1300
Connection ~ 10300 1100
Wire Wire Line
	10300 1100 11050 1100
Wire Wire Line
	10950 1000 10950 1300
Connection ~ 10950 1000
Wire Wire Line
	10950 1000 11700 1000
Wire Wire Line
	11050 1100 11050 1300
Connection ~ 11050 1100
Wire Wire Line
	11050 1100 11800 1100
Connection ~ 11700 1000
Wire Wire Line
	11700 1000 12450 1000
Wire Wire Line
	11800 1100 11800 1300
Connection ~ 11800 1100
Wire Wire Line
	11800 1100 12550 1100
Wire Wire Line
	12450 1000 12450 1300
Connection ~ 12450 1000
Wire Wire Line
	12450 1000 13200 1000
Wire Wire Line
	12550 1100 12550 1300
Connection ~ 12550 1100
Wire Wire Line
	12550 1100 13300 1100
Wire Wire Line
	13200 1000 13200 1300
Connection ~ 13200 1000
Wire Wire Line
	13200 1000 13950 1000
Wire Wire Line
	13300 1100 13300 1300
Connection ~ 13300 1100
Wire Wire Line
	13300 1100 14050 1100
Wire Wire Line
	9100 1300 9100 1200
Text Label 8150 1200 0    50   ~ 0
LEDS_1
NoConn ~ 14350 2300
NoConn ~ 14450 2300
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DC8
P 9350 3800
F 0 "U?" V 9350 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 9000 3100 50  0001 L CNN
F 2 "" H 9350 3800 50  0001 C CNN
F 3 "" H 9350 3800 50  0001 C CNN
	1    9350 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DCE
P 10100 3800
F 0 "U?" V 10100 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 9750 3100 50  0001 L CNN
F 2 "" H 10100 3800 50  0001 C CNN
F 3 "" H 10100 3800 50  0001 C CNN
	1    10100 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DD4
P 10850 3800
F 0 "U?" V 10850 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 10500 3100 50  0001 L CNN
F 2 "" H 10850 3800 50  0001 C CNN
F 3 "" H 10850 3800 50  0001 C CNN
	1    10850 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DDA
P 11600 3800
F 0 "U?" V 11600 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 11250 3100 50  0001 L CNN
F 2 "" H 11600 3800 50  0001 C CNN
F 3 "" H 11600 3800 50  0001 C CNN
	1    11600 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DE0
P 12350 3800
F 0 "U?" V 12350 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 12000 3100 50  0001 L CNN
F 2 "" H 12350 3800 50  0001 C CNN
F 3 "" H 12350 3800 50  0001 C CNN
	1    12350 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DE6
P 13100 3800
F 0 "U?" V 13100 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 12750 3100 50  0001 L CNN
F 2 "" H 13100 3800 50  0001 C CNN
F 3 "" H 13100 3800 50  0001 C CNN
	1    13100 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DEC
P 13850 3800
F 0 "U?" V 13850 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 13500 3100 50  0001 L CNN
F 2 "" H 13850 3800 50  0001 C CNN
F 3 "" H 13850 3800 50  0001 C CNN
	1    13850 3800
	0    1    1    0   
$EndComp
$Comp
L ws2812b_strip:WS2812b_strip U?
U 1 1 614D6DF2
P 14600 3800
F 0 "U?" V 14600 3500 50  0000 L CNN
F 1 "WS2812b_strip" V 14250 3100 50  0001 L CNN
F 2 "" H 14600 3800 50  0001 C CNN
F 3 "" H 14600 3800 50  0001 C CNN
	1    14600 3800
	0    1    1    0   
$EndComp
NoConn ~ 9000 3300
NoConn ~ 9750 3300
NoConn ~ 10500 3300
NoConn ~ 11250 3300
NoConn ~ 12000 3300
NoConn ~ 12750 3300
NoConn ~ 13500 3300
NoConn ~ 14250 3300
NoConn ~ 9000 4300
NoConn ~ 9750 4300
NoConn ~ 10500 4300
NoConn ~ 11250 4300
NoConn ~ 12000 4300
NoConn ~ 12750 4300
NoConn ~ 13500 4300
NoConn ~ 14250 4300
Wire Wire Line
	9350 3250 9850 3250
Wire Wire Line
	9850 3250 9850 3300
Wire Wire Line
	9350 4350 9350 3250
Wire Wire Line
	9100 4300 9100 4350
Wire Wire Line
	9100 4350 9350 4350
Wire Wire Line
	9850 4300 9850 4350
Wire Wire Line
	9850 4350 10100 4350
Wire Wire Line
	10100 4350 10100 3250
Wire Wire Line
	10100 3250 10600 3250
Wire Wire Line
	10600 3250 10600 3300
Wire Wire Line
	10600 4300 10600 4350
Wire Wire Line
	10600 4350 10850 4350
Wire Wire Line
	10850 4350 10850 3250
Wire Wire Line
	10850 3250 11350 3250
Wire Wire Line
	11350 3250 11350 3300
Wire Wire Line
	11350 4300 11350 4350
Wire Wire Line
	11350 4350 11600 4350
Wire Wire Line
	11600 4350 11600 3250
Wire Wire Line
	11600 3250 12100 3250
Wire Wire Line
	12100 3250 12100 3300
Wire Wire Line
	12100 4300 12100 4350
Wire Wire Line
	12100 4350 12350 4350
Wire Wire Line
	12350 3250 12350 4350
Wire Wire Line
	12350 3250 12850 3250
Wire Wire Line
	12850 3250 12850 3300
Wire Wire Line
	12850 4300 12850 4350
Wire Wire Line
	12850 4350 13100 4350
Wire Wire Line
	13100 4350 13100 3250
Wire Wire Line
	13100 3250 13600 3250
Wire Wire Line
	13600 3250 13600 3300
Wire Wire Line
	13600 4300 13600 4350
Wire Wire Line
	13600 4350 13850 4350
Wire Wire Line
	13850 4350 13850 3250
Wire Wire Line
	13850 3250 14350 3250
Wire Wire Line
	14350 3250 14350 3300
Wire Wire Line
	13950 3000 13950 3300
Text Label 8150 3000 0    50   ~ 0
+5V
Text Label 8150 3100 0    50   ~ 0
GND
Wire Wire Line
	14050 3100 14050 3300
Wire Wire Line
	8700 3000 8700 3300
Wire Wire Line
	8700 3000 9450 3000
Wire Wire Line
	8800 3100 8800 3300
Wire Wire Line
	8800 3100 9550 3100
Wire Wire Line
	9450 3000 9450 3300
Connection ~ 9450 3000
Wire Wire Line
	9450 3000 10200 3000
Wire Wire Line
	9550 3100 9550 3300
Connection ~ 9550 3100
Wire Wire Line
	9550 3100 10300 3100
Wire Wire Line
	10200 3000 10200 3300
Connection ~ 10200 3000
Wire Wire Line
	10200 3000 10950 3000
Wire Wire Line
	10300 3100 10300 3300
Connection ~ 10300 3100
Wire Wire Line
	10300 3100 11050 3100
Wire Wire Line
	10950 3000 10950 3300
Connection ~ 10950 3000
Wire Wire Line
	10950 3000 11700 3000
Wire Wire Line
	11050 3100 11050 3300
Connection ~ 11050 3100
Wire Wire Line
	11050 3100 11800 3100
Wire Wire Line
	11700 3000 11700 3300
Connection ~ 11700 3000
Wire Wire Line
	11700 3000 12450 3000
Wire Wire Line
	11800 3100 11800 3300
Connection ~ 11800 3100
Wire Wire Line
	11800 3100 12550 3100
Wire Wire Line
	12450 3000 12450 3300
Connection ~ 12450 3000
Wire Wire Line
	12450 3000 13200 3000
Wire Wire Line
	12550 3100 12550 3300
Connection ~ 12550 3100
Wire Wire Line
	12550 3100 13300 3100
Wire Wire Line
	13200 3000 13200 3300
Connection ~ 13200 3000
Wire Wire Line
	13200 3000 13950 3000
Wire Wire Line
	13300 3100 13300 3300
Connection ~ 13300 3100
Wire Wire Line
	13300 3100 14050 3100
Wire Wire Line
	9100 3300 9100 3200
Text Label 8150 3200 0    50   ~ 0
LEDS_2
NoConn ~ 14350 4300
NoConn ~ 14450 4300
Wire Wire Line
	8100 3200 9100 3200
Wire Wire Line
	7900 1200 7900 4050
Wire Wire Line
	7900 4050 6400 4050
Wire Wire Line
	7900 1200 9100 1200
NoConn ~ 5500 4450
NoConn ~ 5500 4550
NoConn ~ 6400 4450
NoConn ~ 6400 4550
Text Label 4800 4050 0    50   ~ 0
LEDS_1_LV
Text Label 4800 4150 0    50   ~ 0
LEDS_2_LV
Wire Wire Line
	3550 4550 3300 4550
Wire Wire Line
	3300 4550 3300 5650
Wire Wire Line
	3300 5650 4300 5650
Wire Wire Line
	4300 5650 4300 4150
Wire Wire Line
	3550 4450 3200 4450
Wire Wire Line
	3200 4450 3200 5750
Wire Wire Line
	3200 5750 4400 5750
Wire Wire Line
	4400 5750 4400 4050
Text Label 3200 4450 0    50   ~ 0
PWM0
Text Label 3300 4550 0    50   ~ 0
PWM1
Wire Wire Line
	4400 4050 5500 4050
Wire Wire Line
	4300 4150 5500 4150
Wire Wire Line
	3550 3550 3100 3550
Wire Wire Line
	3100 3550 3100 5850
Wire Wire Line
	3100 5850 4500 5850
Wire Wire Line
	4500 5850 4500 4250
Wire Wire Line
	4500 4250 5500 4250
Text Label 4800 4250 0    50   ~ 0
+3V3
Text Label 3300 3550 0    50   ~ 0
+3V3
Wire Wire Line
	6500 3550 6500 4250
Wire Wire Line
	6500 4250 6400 4250
Text Label 4200 3550 0    50   ~ 0
+5V
Wire Wire Line
	5400 3750 5400 4350
Wire Wire Line
	5400 4350 5500 4350
Text Label 4200 3750 0    50   ~ 0
GND
Text Label 4550 2900 1    50   ~ 0
+5V
Text Label 4450 2900 1    50   ~ 0
GND
Wire Wire Line
	3100 1100 1650 1100
Wire Wire Line
	3100 1200 1650 1200
Wire Wire Line
	3100 1300 1650 1300
Text Label 1650 1100 0    50   ~ 0
L
Text Label 1650 1200 0    50   ~ 0
N
Text Label 1650 1300 0    50   ~ 0
G
Wire Notes Line
	2850 3150 2850 6050
Wire Notes Line
	2850 6050 6750 6050
Wire Notes Line
	6750 6050 6750 3150
Wire Notes Line
	6750 3150 2850 3150
Text Notes 5800 6000 0    100  ~ 0
STRIPBOARD
Text Notes 13900 2550 0    100  ~ 0
LX BAR 1
Wire Notes Line
	14700 2600 14700 900 
Wire Notes Line
	14700 900  8550 900 
Wire Notes Line
	8550 900  8550 2600
Wire Notes Line
	8550 2600 14700 2600
Text Notes 13900 4550 0    100  ~ 0
LX BAR 2
Wire Notes Line
	8550 2900 14700 2900
Wire Notes Line
	14700 2900 14700 4600
Wire Notes Line
	14700 4600 8550 4600
Wire Notes Line
	8550 4600 8550 2900
Text Notes 3100 1850 0    100  ~ 0
SCREW\nTERMINALS
Wire Notes Line
	3000 700  3000 1900
$Comp
L graphic:SYM_Flash_Small #SYM?
U 1 1 617185F6
P 2250 900
F 0 "#SYM?" V 2160 900 50  0001 C CNN
F 1 "SYM_Flash_Small" V 2340 900 50  0001 C CNN
F 2 "" H 2250 875 50  0001 C CNN
F 3 "~" H 2650 800 50  0001 C CNN
	1    2250 900 
	1    0    0    -1  
$EndComp
Text Notes 2050 700  0    50   ~ 0
+240V IN
Text Notes 5700 1000 0    50   ~ 0
1.5mm² 2-core flex
Text Notes 5700 1350 0    50   ~ 0
1.5mm² 2-core flex
Text Notes 9650 1000 0    50   ~ 0
Power: 1.5mm² 2-core flex with 8x insulated tap-splice
Text Notes 9650 3000 0    50   ~ 0
Power: 1.5mm² 2-core flex with 8x insulated tap-splice
Text Notes 10500 2450 0    50   ~ 0
8x 2-core JST-SM M-F cables
Text Notes 10500 4450 0    50   ~ 0
8x 2-core JST-SM M-F cables
Text Notes 8550 5500 0    50   ~ 0
Cable list:\n\n- 2x 3m power bus (1.5mm² 2-core, bare stripped cores on one end)\n- 13x 1m daisy chain cable (22AWG 2-core, JST-SM to JST-SM with pigtails to Scotchlock T-taps)\n- 2x 1.5m driver cable (MOLEX KK to JST-SM with pigtails to Scotchlock T-taps)
NoConn ~ 3550 3650
NoConn ~ 3550 3750
NoConn ~ 3550 3850
NoConn ~ 3550 3950
NoConn ~ 3550 4050
NoConn ~ 3550 4150
NoConn ~ 3550 4250
NoConn ~ 3550 4350
NoConn ~ 3550 4650
NoConn ~ 3550 4750
NoConn ~ 3550 4850
NoConn ~ 3550 4950
NoConn ~ 3550 5050
NoConn ~ 3550 5150
NoConn ~ 3550 5250
NoConn ~ 3550 5350
NoConn ~ 3550 5450
NoConn ~ 4150 3650
NoConn ~ 4150 3850
NoConn ~ 4150 3950
NoConn ~ 4150 4050
NoConn ~ 4150 4150
NoConn ~ 4150 4250
NoConn ~ 4150 4350
NoConn ~ 4150 4450
NoConn ~ 4150 4550
NoConn ~ 4150 4650
NoConn ~ 4150 4750
NoConn ~ 4150 4850
NoConn ~ 4150 4950
NoConn ~ 4150 5050
NoConn ~ 4150 5150
NoConn ~ 4150 5250
NoConn ~ 4150 5350
NoConn ~ 4150 5450
Text Notes 3500 5600 0    50   ~ 0
RPI GPIO breakout
Text Notes 7100 4300 0    50   ~ 0
2x 2-core 16/0.2mm
Text Notes 4850 3100 0    50   ~ 0
2-way\nMOLEX KK
Text Notes 6800 4000 0    50   ~ 0
2x 2-way\nMOLEX KK
Text Notes 4550 2650 1    50   ~ 0
2-core 16/0.2mm
Text Notes 14000 1050 0    50   ~ 0
Taps: 22AWG
Text Notes 14000 3050 0    50   ~ 0
Taps: 22AWG
Wire Wire Line
	3900 1300 4000 1300
Wire Wire Line
	4000 1050 8000 1050
Wire Wire Line
	4000 1050 4000 1300
Wire Wire Line
	3900 1100 3950 1100
Wire Wire Line
	3950 1100 3950 1350
Wire Wire Line
	8000 1050 8000 1100
Wire Wire Line
	8000 1100 8800 1100
Connection ~ 8800 1100
Wire Wire Line
	7400 1400 7400 3100
Wire Wire Line
	7400 3100 8800 3100
Connection ~ 8800 3100
Wire Wire Line
	7450 1350 7450 3000
Wire Wire Line
	7450 3000 8700 3000
Wire Wire Line
	3950 1350 7450 1350
Connection ~ 8700 3000
Wire Notes Line
	3000 700  4600 700 
Wire Notes Line
	4600 700  4600 1900
Wire Notes Line
	4600 1900 3000 1900
Wire Wire Line
	9200 2300 9300 2300
Wire Wire Line
	9300 2300 9300 1200
Wire Wire Line
	9300 1200 9950 1200
Wire Wire Line
	9950 1200 9950 1300
Wire Wire Line
	9950 2300 10050 2300
Wire Wire Line
	10050 2300 10050 1200
Wire Wire Line
	10050 1200 10700 1200
Wire Wire Line
	10700 1200 10700 1300
Wire Wire Line
	10700 2300 10800 2300
Wire Wire Line
	10800 2300 10800 1200
Wire Wire Line
	10800 1200 11450 1200
Wire Wire Line
	11450 1200 11450 1300
Wire Wire Line
	11450 2300 11550 2300
Wire Wire Line
	11550 2300 11550 1200
Wire Wire Line
	11700 1000 11700 1300
Wire Wire Line
	11550 1200 12200 1200
Wire Wire Line
	12200 1200 12200 1300
Wire Wire Line
	12200 2300 12300 2300
Wire Wire Line
	12300 2300 12300 1200
Wire Wire Line
	12300 1200 12950 1200
Wire Wire Line
	12950 1200 12950 1300
Wire Wire Line
	12950 2300 13050 2300
Wire Wire Line
	13050 2300 13050 1200
Wire Wire Line
	13050 1200 13700 1200
Wire Wire Line
	13700 1200 13700 1300
Wire Wire Line
	13700 2300 13800 2300
Wire Wire Line
	13800 2300 13800 1200
Wire Wire Line
	13800 1200 14450 1200
Wire Wire Line
	14450 1200 14450 1300
Wire Wire Line
	9200 4300 9300 4300
Wire Wire Line
	9300 4300 9300 3200
Wire Wire Line
	9300 3200 9950 3200
Wire Wire Line
	9950 3200 9950 3300
Wire Wire Line
	9950 4300 10050 4300
Wire Wire Line
	10050 4300 10050 3200
Wire Wire Line
	10050 3200 10700 3200
Wire Wire Line
	10700 3200 10700 3300
Wire Wire Line
	10700 4300 10800 4300
Wire Wire Line
	10800 4300 10800 3200
Wire Wire Line
	10800 3200 11450 3200
Wire Wire Line
	11450 3200 11450 3300
Wire Wire Line
	11450 4300 11550 4300
Wire Wire Line
	11550 4300 11550 3200
Wire Wire Line
	11550 3200 12200 3200
Wire Wire Line
	12200 3200 12200 3300
Wire Wire Line
	12200 4300 12300 4300
Wire Wire Line
	12300 4300 12300 3200
Wire Wire Line
	12300 3200 12950 3200
Wire Wire Line
	12950 3200 12950 3300
Wire Wire Line
	12950 4300 13050 4300
Wire Wire Line
	13050 4300 13050 3200
Wire Wire Line
	13050 3200 13700 3200
Wire Wire Line
	13700 3200 13700 3300
Wire Wire Line
	13700 4300 13800 4300
Wire Wire Line
	13800 4300 13800 3200
Wire Wire Line
	13800 3200 14450 3200
Wire Wire Line
	14450 3200 14450 3300
Wire Wire Line
	6400 4350 6600 4350
Wire Wire Line
	6600 4100 7950 4100
Wire Wire Line
	7950 4100 7950 1250
Wire Wire Line
	9200 1250 9200 1300
Wire Wire Line
	7950 1250 9200 1250
Wire Wire Line
	6600 4350 8150 4350
Wire Wire Line
	8150 4350 8150 3250
Wire Wire Line
	8150 3250 9200 3250
Wire Wire Line
	9200 3250 9200 3300
Connection ~ 6600 4350
Wire Wire Line
	6600 4350 6600 4100
Wire Wire Line
	6400 4150 6650 4150
Wire Wire Line
	6650 4150 6650 4300
Wire Wire Line
	6650 4300 8100 4300
Wire Wire Line
	8100 3200 8100 4300
Wire Wire Line
	3900 1000 8700 1000
Wire Wire Line
	4150 3550 4550 3550
Wire Wire Line
	4550 950  3900 950 
Wire Wire Line
	3900 950  3900 1000
Connection ~ 3900 1000
Wire Wire Line
	3900 1400 7400 1400
Wire Wire Line
	4150 3750 4450 3750
Wire Wire Line
	4550 950  4550 3550
Connection ~ 4550 3550
Wire Wire Line
	4550 3550 6500 3550
Wire Wire Line
	4450 3750 4450 1450
Wire Wire Line
	4450 1450 3900 1450
Wire Wire Line
	3900 1450 3900 1400
Connection ~ 4450 3750
Wire Wire Line
	4450 3750 5400 3750
Connection ~ 3900 1400
$EndSCHEMATC
