# opi-mg996r

This is a Python implementation of MG996R servo support for Orange Pi boards (H3 specifically, others untested).
It does not use hardware PWM but instead emulates PWM with primitive `time.sleep()` calls, so don't expect any real-time 
accuracy. And, well, it's Python, after all.

But it does its job and MG996R servo works just fine!

## Usage

- Clone the repo.
- Install dependencies (see [here](requirements.txt)).
- Check out [example.py](example.py) for an example.

You can also just use it from command line like this:
```
./example.py --deg 0
./example.py --deg 180
./example.py --deg 90
```

## Credits

The softpwm implementation was taken the [orangepwm](https://github.com/evergreen-it-dev/orangepwm) project.

## License

MIT