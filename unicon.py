import time
def unicon():
    print('Hello, welcome to the Universal Converter!')
    time.sleep(3)
    print("We help you change all kinds of units to other units, how handy!")
    time.sleep(5)
    on = True
    while on == True:
        print('Please insert your information.')
        time.sleep(2)
        unit = str.lower(input('Unit [(Before) to (After)]: '))
        if unit == 'bmi':
            weight = float(input('Weight(kg): '))
            height = float(input('Height(m): '))
            result = weight / (height * height)
            print(result)
        elif unit == 'help':
            print('''
                Commands included:
                BASIC
                1. cm to inches
                2. inches to cm
                3. cm to mm
                4. mm to cm
                5. cm to m
                6. m to cm
                7. cm to km
                8. km to cm
                9. m to km
                10. km to m
                11. mm to m
                12. m to mm
                13. ml to l
                14. l to ml
                15. l to gal
                16. gal to l
                17. g to kg
                18. kg to g
                19. kg to lbs
                20. lbs to kg
                21. mm to km
                22. km to mm
                23. hkd to usd
                24. usd to hkd
                25. hkd to rmb
                26. rmb to hkd
                27. hkd to eur 
                28. eur to hkd
                29. sec to min 
                30. min to sec
                31. min to hr
                32. hr to min
                33. hr to day 
                34. day to hr
                35. c to f (Celsius to  Fahrenheit)
                36. f to c 
                ADVANCED
                1. bmi
                ''')
        elif unit == 'stop':
            break
        else:
            number = float(input('Number: '))
            if unit == 'cm to inches':
                result = number * 0.3937007874
            elif unit == 'inches to cm':
                result = number * 2.54
            elif unit == 'cm to mm':
                result = number * 10
            elif unit == 'mm to cm':
                result = number * 0.1
            elif unit == 'cm to m':
                result = number * 0.01
            elif unit == 'm to cm':
                result = number * 100
            elif unit == 'cm to km':
                result = number * 0.00001
            elif unit == 'km to cm':
                result = number * 100000
            elif unit == 'm to km':
                result = number * 0.001
            elif unit == 'km to m':
                result = number * 1000
            elif unit == 'mm to m':
                result = number * 0.001
            elif unit == 'm to mm':
                result = number * 1000
            elif unit == 'ml to l':
                result = number * 0.001
            elif unit == 'l to ml':
                result = number * 1000
            elif unit == 'l to gal':
                result = number * 0.2641720524
            elif unit == 'gal to l':
                result = number * 3.785411784
            elif unit == 'g to kg':
                result = number * 0.001
            elif unit == 'kg to g':
                result = number * 1000
            elif unit == 'kg to lbs':
                result = number * 2.2046226218
            elif unit == 'lbs to kg':
                result = number * 0.45359237
            elif unit == 'mm to km':
                result = number * 0.000001
            elif unit == 'km to mm':
                result = number * 1000000
            elif unit == 'hkd to usd':
                result = number * 0.13
            elif unit == 'usd to hkd':
                result = number * 7.83
            elif unit == 'hkd to rmb':
                result = number * 0.9
            elif unit == 'rmb to hkd':
                result = number * 1.11
            elif unit == 'hkd to eur':
                result = number * 0.12
            elif unit == 'eur to hkd':
                result = number * 8.63
            elif unit == 'min to sec':
                result = number * 60
            elif unit == 'sec to min':
                result = number / 60
            elif unit == 'min to hr':
                result = number / 60
            elif unit == 'hr to min':
                result = number * 60
            elif unit == 'hr to day':
                result = number / 24
            elif unit == 'day to hr':
                result = number * 24
            elif unit == 'c to f':
                result = number * 1.8 + 32
            elif unit == 'f to c':
                result = (number - 32) * 0.55555555555555555555555


            print (result)
        time.sleep(5)