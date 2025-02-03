import random
import matplotlib.pyplot as plt
import math

NUM_SAMPLES_1 = 1000
NUM_SAMPLES_2 = 3000

def run_the_thing(samples, rep_dist, demo_dist):
    was_right_for_num_samp = 0

    for _ in range(100):
        result1 = random.choices([1, 0], weights=[rep_dist, demo_dist], k=samples)
        repub_votes = result1.count(1)
        demo_votes = result1.count(0)

        rep_win = (rep_dist > demo_dist)
        guess_win = (repub_votes > demo_votes)

        if (guess_win == rep_win):
            was_right_for_num_samp += 1

    return was_right_for_num_samp;

was_right_for_num_samp_1 = run_the_thing(NUM_SAMPLES_1, 0.48, 0.52)
print(f"The guy was right in {was_right_for_num_samp_1} cases out of 100 for a sample space of {NUM_SAMPLES_1}")

was_right_for_num_samp_2 = run_the_thing(NUM_SAMPLES_2, 0.48, 0.52)
print(f"The guy was right in {was_right_for_num_samp_2} cases out of 100 for a sample space of {NUM_SAMPLES_2}")

was_right_for_diff_dist = run_the_thing(NUM_SAMPLES_2, 0.49, 0.51)
print(f"The guy was right in {was_right_for_diff_dist} cases out of 100 for a sample space of {NUM_SAMPLES_2}")
