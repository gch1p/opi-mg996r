#!/usr/bin/env python3
import os, logging
from argparse import ArgumentParser
from mg996r import MG996R

start_degree = 360
state_file = '.servo-state'

if __name__ == '__main__':
    # set logging level
    logging.basicConfig(level=logging.DEBUG)

    # parse arguments
    parser = ArgumentParser()
    parser.add_argument('--deg', type=int, required=True)
    parser.add_argument('--pin', type=str, default='PA6',
                        help='GPIO pin to use')
    parser.add_argument('--reset', action='store_true',
                        help=f'Use clean default state (degree = {start_degree})')
    args = parser.parse_args()

    # restore previous degree from a file
    if not args.reset:
        try:
            if os.path.exists(state_file):
                with open(state_file, 'r') as f:
                    start_degree = int(f.read())
                    if not 0 <= start_degree <= 360:
                        raise ValueError(f'invalid degree value in {state_file}')
        except (IOError, ValueError) as e:
            logging.exception(e)

    servo = MG996R(args.pin, start_degree)
    servo.move(args.deg)

    # save degree to a file
    try:
        with open(state_file, 'w') as f:
            f.write(str(args.deg))
    except IOError as e:
        logging.exception(e)
