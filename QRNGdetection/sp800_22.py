import numpy as np
import sys
from QRNGdetection import sp800_22_monobit_test
from QRNGdetection import sp800_22_frequency_within_block_test
from QRNGdetection import sp800_22_runs_test
from QRNGdetection import sp800_22_longest_run_ones_in_a_block_test
from QRNGdetection import  sp800_22_binary_matrix_rank_test
from QRNGdetection import sp800_22_dft_test
from QRNGdetection import sp800_22_non_overlapping_template_matching_test
from QRNGdetection import sp800_22_overlapping_template_matching_test
from QRNGdetection import sp800_22_maurers_universal_test
from QRNGdetection import sp800_22_linear_complexity_test
from QRNGdetection import sp800_22_serial_test
from QRNGdetection import sp800_22_approximate_entropy_test
from QRNGdetection import sp800_22_cumulative_sums_test
from QRNGdetection import sp800_22_random_excursion_test
from QRNGdetection import sp800_22_random_excursion_variant_test
import Tool.glo as glo


def all(results,bits):
    try:
        sys.stdout = glo.Logger('../Detect Result.txt')
        print('------------------------------------------------------')
        print('monobit_test')
        success, p, plist = sp800_22_monobit_test.monobit_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('monobit_test', summary_p, summary_result))
        glo.set_value('detectbar', 1)

        print('------------------------------------------------------')
        print('frequency_within_block_test')
        (success, p, plist) = sp800_22_frequency_within_block_test.frequency_within_block_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('frequency_within_block_test', summary_p, summary_result))
        glo.set_value('detectbar', 2)

        print('------------------------------------------------------')
        print('runs_test')
        (success, p, plist) = sp800_22_runs_test.runs_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('runs_test', summary_p, summary_result))
        glo.set_value('detectbar', 3)

        print('------------------------------------------------------')
        print('longest_run_ones_in_a_block_test')
        (success, p, plist) = sp800_22_longest_run_ones_in_a_block_test.longest_run_ones_in_a_block_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('longest_run_ones_in_a_block_test', summary_p, summary_result))
        glo.set_value('detectbar', 4)

        print('------------------------------------------------------')
        print('binary_matrix_rank_test')
        (success, p, plist) = sp800_22_binary_matrix_rank_test.binary_matrix_rank_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('binary_matrix_rank_test', summary_p, summary_result))
        glo.set_value('detectbar', 5)

        print('------------------------------------------------------')
        print('dft_test')
        (success, p, plist) = sp800_22_dft_test.dft_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('dft_test', summary_p, summary_result))
        glo.set_value('detectbar', 6)

        print('------------------------------------------------------')
        print('non_overlapping_template_matching_test')
        (success, p, plist) = sp800_22_non_overlapping_template_matching_test.non_overlapping_template_matching_test(
            bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('non_overlapping_template_matching_test', summary_p, summary_result))
        glo.set_value('detectbar', 7)

        print('------------------------------------------------------')
        print('overlapping_template_matching_test')
        (success, p, plist) = sp800_22_overlapping_template_matching_test.overlapping_template_matching_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('overlapping_template_matching_test', summary_p, summary_result))
        glo.set_value('detectbar', 8)

        print('------------------------------------------------------')
        print('maurers_universal_test')
        (success, p, plist) = sp800_22_maurers_universal_test.maurers_universal_test(bits, None, None)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('maurers_universal_test', summary_p, summary_result))
        glo.set_value('detectbar', 9)

        print('------------------------------------------------------')
        print('linear_complexity_test')
        (success, p, plist) = sp800_22_linear_complexity_test.linear_complexity_test(bits, 500)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('linear_complexity_test', summary_p, summary_result))
        glo.set_value('detectbar', 10)

        print('------------------------------------------------------')
        print('serial_test')
        (success, p, plist) = sp800_22_serial_test.serial_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('serial_test', summary_p, summary_result))
        glo.set_value('detectbar', 11)

        print('------------------------------------------------------')
        print('approximate_entropy_test')
        (success, p, plist) = sp800_22_approximate_entropy_test.approximate_entropy_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            summary_p = str(min(plist))
        results.append(('approximate_entropy_test', summary_p, summary_result))
        glo.set_value('detectbar', 12)

        print('------------------------------------------------------')
        print('cumulative_sums_test')
        (success, p, plist) = sp800_22_cumulative_sums_test.cumulative_sums_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            print('p=', str(min(plist)))
            summary_p = str(min(plist))
        results.append(('cumulative_sums_test', summary_p, summary_result))
        glo.set_value('detectbar', 13)

        print('------------------------------------------------------')
        print('random_excursion_test')
        (success, p, plist) = sp800_22_random_excursion_test.random_excursion_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            print('p=', str(min(plist)))
            summary_p = str(min(plist))
        results.append(('random_excursion_test', summary_p, summary_result))
        glo.set_value('detectbar', 14)

        print('------------------------------------------------------')
        print('random_excursion_variant_test')
        (success, p, plist) = sp800_22_random_excursion_variant_test.random_excursion_variant_test(bits)
        if success:
            print("  PASS")
            summary_result = "PASS"
        else:
            print("  FAIL")
            summary_result = "FAIL"

        if p != None:
            print("  P=" + str(p))
            summary_p = str(p)

        if plist != None:
            print('p=', str(min(plist)))
            summary_p = str(min(plist))
        results.append(('random_excursion_variant_test', summary_p, summary_result))
        glo.set_value('detectbar', 15)
    finally:
        sys.stdout.reset()


if __name__ == "__main__":
    test = ''
    tt_path = 'output.txt'
    f = open(tt_path)
    for line in f.readlines():
        line = line.strip()
        test += line
    nbits = [v for v in test]
    bits = [int(x) for x in nbits]

    results = list()
    all(results, bits)
    print('**************************************************************************')
    f = open("output1.txt", "w")
    for result in results:
        (summary_name, summary_p, summary_result) = result
        print(summary_name.ljust(40), summary_p.ljust(28), summary_result,file=f)
        

