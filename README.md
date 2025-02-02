# IMEI Generator

This Python script generates valid IMEI numbers based on a given TAC (Type Allocation Code).

## Usage

To use this script, you need to have Python installed on your system. You can run the script from the command line with the following command:

```sh
python imeigenerator.py --tac <8 digits> --total <total generated imei>
```

### Example

```sh
python imeigenerator.py --tac 12345678 --total 10
```

This command will generate 10 valid IMEI numbers with the TAC `12345678`.

## Arguments

- `--tac`: The TAC number (8 digits) to use for generating IMEI numbers. This argument is required.
- `--total`: The total number of IMEI numbers to generate. This argument is required.

## How It Works

The script uses the Luhn algorithm to calculate the check digit for the IMEI numbers. The main steps are:

1. Generate a random 6-digit serial number.
2. Concatenate the TAC and the serial number to form a 14-digit partial IMEI.
3. Calculate the check digit using the Luhn algorithm.
4. Append the check digit to the partial IMEI to form a complete 15-digit IMEI.

## Example Output

```
123456780123456
123456780123457
123456780123458
...
```

## Author

Written by Jeff Steveanus

## License

This project is licensed under the MIT License. See the LICENSE file for details.
